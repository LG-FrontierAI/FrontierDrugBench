"""Offline case scoring for the exported structure benchmark."""

from __future__ import annotations

from collections.abc import Callable
import json
import re
from typing import Any


# Source: analyse_ca/api_response_capture.py

class APIResponseError(RuntimeError):
    """Display provider data verbatim, keeping HTTP status out of its message."""

    def __init__(self, message: str, *, http_status: int | None = None):
        super().__init__(message)
        self.http_status = http_status


# Source: analyse_ca/json_bracket_repair.py

MAX_BRACKET_EDITS = 4


MAX_REPAIR_STATES = 256


BRACKETS = "{}[]"


MATCHING_CLOSE = {"{": "}", "[": "]"}


JSON_STRINGS = re.compile(r'"(?:[^"\\]|\\.)*"')


def minimum_balance_edits(text: str) -> int:
    outside_strings = JSON_STRINGS.sub("", text)
    return sum(abs(outside_strings.count(opening) - outside_strings.count(closing))
               for opening, closing in MATCHING_CLOSE.items())


def bracket_context(text: str, end: int):
    """Inspect structural brackets, ignoring quoted/escaped string contents."""
    stack = []
    in_string = False
    escaped = False
    last_closed = None
    last_value = None
    mismatch = None
    for pos, char in enumerate(text[:end]):
        if in_string:
            if escaped:
                escaped = False
            elif char == "\\":
                escaped = True
            elif char == '"':
                in_string = False
            continue
        if char == '"':
            in_string = True
        elif char == ":":
            last_value = pos + 1
            while last_value < len(text) and text[last_value].isspace():
                last_value += 1
        elif char in "{[":
            stack.append((char, pos))
        elif char in "}]":
            if stack and MATCHING_CLOSE[stack[-1][0]] == char:
                last_closed = stack.pop()[1]
            elif mismatch is None:
                mismatch = pos
    return stack, last_closed, last_value, mismatch, in_string


def bracket_edits(text: str, error: json.JSONDecodeError):
    """Propose edits at the error or nearby container boundaries, never values."""
    pos = error.pos
    # An explicit trailing comma is not a missing-bracket error. Do not turn
    # it into a fabricated empty container such as [1, []].
    if error.msg == "Expecting value" and pos < len(text) and text[pos] in "}]":
        if text[:pos].rstrip().endswith(","):
            return
    stack, last_closed, last_value, _, in_string = bracket_context(text, pos)
    if in_string:
        return  # Never repair quotes or unterminated strings.
    if pos < len(text) and text[pos] in BRACKETS:
        yield text[:pos] + text[pos + 1:], 1
    for char in BRACKETS:
        yield text[:pos] + char + text[pos:], 1

    # Missing opening brackets may first be detected after their contents:
    # e.g. a coordinate row closes before its surrounding array was opened.
    anchors = {0, last_closed, last_value}
    if stack:
        anchors.add(stack[-1][1])
    for anchor in sorted(value for value in anchors if value is not None and value < pos):
        for char in "{[":
            yield text[:anchor] + char + text[anchor:], 1

    # A complete value followed only by missing closing brackets is common.
    full_stack, _, _, mismatch, open_string = bracket_context(text, len(text))
    if full_stack and mismatch is None and not open_string:
        suffix = "".join(MATCHING_CLOSE[char] for char, _ in reversed(full_stack))
        yield text + suffix, len(suffix)


def repair_json_brackets(
    text: str, validator: Callable[[dict[str, Any]], Any] | None = None,
) -> dict[str, Any] | None:
    """Return a unique minimum-edit object, or fail closed on ambiguity/limits.

    No non-bracket character is changed. The validator may check the model's
    input contract (roles, IDs and coordinate counts), not reference coordinates
    or prediction quality. Multiple distinct valid minimum-edit objects are
    ambiguous and are rejected.
    """
    levels: list[set[str]] = [set() for _ in range(MAX_BRACKET_EDITS + 1)]
    levels[0].add(text)
    visited: dict[str, int] = {text: 0}
    examined = 0
    for distance, candidates in enumerate(levels):
        valid: dict[str, dict[str, Any]] = {}
        errors = []
        for candidate in sorted(candidates):
            if visited[candidate] < distance:
                continue
            examined += 1
            if examined > MAX_REPAIR_STATES:
                return None
            try:
                payload = json.loads(candidate)
            except json.JSONDecodeError as error:
                errors.append((candidate, error))
                continue
            if not isinstance(payload, dict):
                continue
            try:
                if validator is not None:
                    validator(payload)
            except (ValueError, TypeError, KeyError):
                continue
            identity = json.dumps(payload, sort_keys=True, separators=(",", ":"))
            valid[identity] = payload
            if len(valid) > 1:
                return None
        if valid:
            return next(iter(valid.values()))
        if distance == MAX_BRACKET_EDITS:
            continue
        for candidate, error in errors:
            for repaired, cost in bracket_edits(candidate, error):
                new_distance = distance + cost
                if new_distance + minimum_balance_edits(repaired) > MAX_BRACKET_EDITS:
                    continue
                if repaired not in visited or new_distance < visited[repaired]:
                    if len(visited) >= MAX_REPAIR_STATES:
                        return None
                    visited[repaired] = new_distance
                    levels[new_distance].add(repaired)
    return None


# Source: analyse_ca/json_output_parser.py

def parse_model_json(
    text: str, *, validator: Callable[[dict[str, Any]], Any] | None = None,
) -> tuple[dict[str, Any], str, bool]:
    stripped = text.strip()
    try:
        payload = json.loads(stripped)
        parse_mode = "strict_json"
        strict = True
    except json.JSONDecodeError as strict_error:
        blocks = re.findall(
            r"```(?:json)?\s*(.*?)\s*```", stripped,
            flags=re.IGNORECASE | re.DOTALL,
        )
        source = blocks[0].strip() if len(blocks) == 1 else stripped
        try:
            payload = json.loads(source)
            parse_mode = "markdown_json_code_block"
        except json.JSONDecodeError:
            payload = repair_json_brackets(source, validator)
            if payload is None:
                raise strict_error
            parse_mode = (
                "markdown_json_code_block_recovered_brackets"
                if len(blocks) == 1 else "recovered_brackets"
            )
        strict = False
    if not isinstance(payload, dict):
        raise ValueError("model output must be a JSON object")
    return payload, parse_mode, strict


# Source: analyse_ca/run_ca_benchmark.py

def text_from_nonstream_response(response: dict[str, Any], api_style: str) -> str:
    if api_style == "chat_completions":
        choices = response.get("choices", [])
        if choices:
            content = choices[0].get("message", {}).get("content")
            if isinstance(content, str):
                return content

    if api_style == "responses":
        if isinstance(response.get("output_text"), str):
            return response["output_text"]
        parts = []
        for item in response.get("output", []):
            if not isinstance(item, dict):
                continue
            for content in item.get("content", []):
                if isinstance(content, dict) and content.get("type") in {
                    "output_text",
                    "text",
                }:
                    text = content.get("text")
                    if isinstance(text, str):
                        parts.append(text)
        if parts:
            return "".join(parts)

    if api_style == "anthropic_messages":
        parts = [
            block["text"]
            for block in response.get("content", [])
            if isinstance(block, dict)
            and block.get("type") == "text"
            and isinstance(block.get("text"), str)
        ]
        if parts:
            return "".join(parts)

    # Proxy compatibility fallbacks.
    if isinstance(response.get("output_text"), str):
        return response["output_text"]
    choices = response.get("choices", [])
    if choices and isinstance(choices[0].get("message", {}).get("content"), str):
        return choices[0]["message"]["content"]
    content = response.get("content")
    if isinstance(content, str):
        return content
    raise ValueError(f"cannot extract model text for api_style={api_style}")


def text_from_stream_events(events: list[dict[str, Any]], api_style: str) -> str:
    parts = []
    for event in events:
        if api_style == "chat_completions":
            choices = event.get("choices", [])
            if choices:
                delta = choices[0].get("delta", {}).get("content")
                if isinstance(delta, str):
                    parts.append(delta)
        elif api_style == "responses":
            if event.get("type") == "response.output_text.delta" and isinstance(
                event.get("delta"), str
            ):
                parts.append(event["delta"])
        else:
            delta = event.get("delta", {})
            if event.get("type") == "content_block_delta" and isinstance(
                delta.get("text"), str
            ):
                parts.append(delta["text"])
    if not parts:
        for event in reversed(events):
            if event.get("type") == "message_delta" and isinstance(event.get("delta"), dict):
                raise APIResponseError(json.dumps(event["delta"], ensure_ascii=False))
        raise ValueError(f"cannot extract streamed text for api_style={api_style}")
    return "".join(parts)


def raise_provider_error(response: dict[str, Any]) -> None:
    """Surface the provider's error/stop data before attempting JSON extraction."""
    events = response.get("events", []) if response.get("stream") is True else [response]
    for event in events:
        if not isinstance(event, dict):
            continue
        nested = event.get("response")
        candidates = [event] + ([nested] if isinstance(nested, dict) else [])
        for candidate in candidates:
            if candidate.get("error"):
                error = candidate["error"]
                raise APIResponseError(error if isinstance(error, str) else json.dumps(error, ensure_ascii=False))
            if candidate.get("incomplete_details"):
                raise APIResponseError(json.dumps(candidate["incomplete_details"], ensure_ascii=False))
            if candidate.get("stop_reason") in {"refusal", "max_tokens"}:
                stop = {key: value for key, value in candidate.items() if key.startswith("stop_")}
                raise APIResponseError(json.dumps(stop, ensure_ascii=False))
        delta = event.get("delta")
        if isinstance(delta, dict) and delta.get("stop_reason") in {"refusal", "max_tokens"}:
            raise APIResponseError(json.dumps(delta, ensure_ascii=False))
        for choice in event.get("choices", []):
            if choice.get("finish_reason") in {"length", "content_filter", "refusal"}:
                raise APIResponseError(json.dumps({"finish_reason": choice["finish_reason"]}, ensure_ascii=False))
            message = choice.get("message") or choice.get("delta") or {}
            if message.get("refusal"):
                raise APIResponseError(json.dumps({"type": "refusal", "refusal": message["refusal"]}, ensure_ascii=False))
        for item in event.get("output", []):
            for content in item.get("content", []) if isinstance(item, dict) else []:
                if isinstance(content, dict) and content.get("type") == "refusal":
                    raise APIResponseError(json.dumps(content, ensure_ascii=False))


def extract_response_text(response: dict[str, Any], api_style: str) -> str:
    raise_provider_error(response)
    if response.get("stream") is True and isinstance(response.get("events"), list):
        if api_style == "chat_completions":
            choices = [choice for event in response["events"] if isinstance(event, dict)
                       for choice in event.get("choices", []) if isinstance(choice, dict)]
            if not any(choice.get("finish_reason") == "stop" for choice in choices):
                raise ValueError("incomplete chat completion stream: no normal finish_reason=stop")
        if api_style == "anthropic_messages" and not any(
            event.get("type") == "message_stop" for event in response["events"]
        ):
            raise ValueError("stream ended before message_stop")
        text = text_from_stream_events(response["events"], api_style)
        if not text.strip():
            raise ValueError("completed response has empty final content")
        return text
    return text_from_nonstream_response(response, api_style)


def usage_from_response(response: dict[str, Any]) -> tuple[Any, Any]:
    candidates = [response]
    if response.get("stream") is True:
        candidates = list(reversed(response.get("events", [])))
    for candidate in candidates:
        usage = candidate.get("usage") if isinstance(candidate, dict) else None
        if not isinstance(usage, dict):
            response_object = candidate.get("response", {})
            usage = response_object.get("usage") if isinstance(response_object, dict) else None
        if not isinstance(usage, dict):
            continue
        input_tokens = usage.get("input_tokens", usage.get("prompt_tokens"))
        output_tokens = usage.get("output_tokens", usage.get("completion_tokens"))
        if input_tokens is not None or output_tokens is not None:
            return input_tokens, output_tokens
    return "", ""


def token_count(value: Any) -> int:
    if value in (None, ""):
        return 0
    return int(value)


def response_style(payload, preferred):
    if not isinstance(payload, dict):
        return None
    if payload.get("stream") is True and isinstance(payload.get("events"), list):
        if preferred:
            return preferred
        events = [event for event in payload["events"] if isinstance(event, dict)]
        if any(str(event.get("type", "")).startswith("response.") for event in events):
            return "responses"
        if any(str(event.get("type", "")).startswith(("message_", "content_block_")) for event in events):
            return "anthropic_messages"
        return "chat_completions"
    if "choices" in payload:
        return "chat_completions"
    if "output" in payload or "output_text" in payload:
        return "responses"
    if "content" in payload:
        return preferred or "anthropic_messages"
    if any(key in payload for key in ("error", "incomplete_details", "stop_reason")):
        return preferred or "chat_completions"
    return None


class RawReply:
    """Decode the API envelope and retain parsing diagnostics for the result files."""

    def __init__(self, raw, api_style=None):
        self.raw = raw
        self.preferred_style = api_style
        self.api_style = "model_json"
        self.input_tokens = 0
        self.output_tokens = 0
        self.text = None
        self.parsed = None
        self.parse_mode = ""
        self.strict = False

    def parse(self, validator):
        text = self.raw.decode("utf-8-sig")
        try:
            envelope = json.loads(text)
        except json.JSONDecodeError:
            envelope = None  # The task parser may recover structural brackets.
        style = response_style(envelope, self.preferred_style)
        if style:
            self.api_style = style
            self.input_tokens, self.output_tokens = map(token_count, usage_from_response(envelope))
            text = extract_response_text(envelope, style)
        elif isinstance(envelope, str):
            text = envelope
        self.text = text
        self.parsed, self.parse_mode, self.strict = parse_model_json(text, validator=validator)
        return self.parsed


def is_refusal_evidence(value):
    """Recognize explicit refusal markers in saved provider envelopes."""
    if isinstance(value, dict):
        if value.get("stop_reason") == "refusal" or value.get("code") == "upstream_refusal":
            return True
        if value.get("type") == "refusal" or value.get("finish_reason") == "refusal":
            return True
        return any(is_refusal_evidence(value[key]) for key in
                   ("events", "response", "error", "delta", "message", "stop_details", "choices")
                   if key in value)
    if isinstance(value, list):
        return any(is_refusal_evidence(item) for item in value)
    if isinstance(value, str):
        try:
            parsed = json.loads(value)
        except json.JSONDecodeError:
            return False
        return isinstance(parsed, (dict, list)) and is_refusal_evidence(parsed)
    return False


def resolve_prediction(prediction, validator):
    if isinstance(prediction, RawReply):
        return prediction.parse(validator)
    if isinstance(prediction, str):
        return json.loads(prediction)
    return prediction
