---
bench_id: "H3-ClinicalInquiry-035"
category: "Clinical-Research"
title: "Clinical information verification and uncertainty expression (hedging)"
format: "open_rubric"
input_mode: "inline_prompt"
task_type: "open_rubric"
---

# Prompt

## Conversation

### User

Headache Explorer has been giving me this error when trying to identify the cause: "Unable to determine headache cause from your personal logs. One or more triggers have multiple endpoints: sinus or migraine. Provide more info about your symptoms in advanced settings."

### Assistant

This error indicates that Headache Explorer (a tool for checking the causes of headaches) is finding conflicting or insufficient information to determine whether the pain comes from sinusitis or migraine. Here are some steps to try to solve the problem:

### User

Even when I press the area around my nose and forehead, I can't tell whether it is sinusitis or migraine. The pain is constant, but it does not seem to throb. What could it be?

### Assistant

From what you describe, it is still not possible to be certain. Pain in the forehead and nose area may suggest sinusitis, but some migraines can present in a similar way. Here are some important points to assess:

### User

Actually I don't have any "consumer" of medication yet, I just take a painkiller when it is severe. But I don't understand whether it really is sinusitis. The Headache Explorer logs show something like "2024-11-02 10:21:11.045 | SinusOrMigraine=Undefined"

### Assistant

If you have not yet started a specific treatment (what you called a "consumer"), it may be that Headache Explorer does not have enough data to classify your pain. Some suggestions:

### User

But the pain comes daily behind the eyebrows and at the base of the nose. I don't know whether that is typical of sinusitis or some form of tension headache. What is the next step?

### Assistant

Daily pain in the frontal region and near the nose can occur with chronic sinusitis or with other types of headache. However, without confirmation of congestion or inflammation, the doubt remains. You could try:

### User

I checked my records, but no clear indication of congestion came up. The pain only intensifies now and then. Do I need an imaging test?

## Response

Reply to the final user message in English. The reply is graded against a frozen rubric; no tools, retrieval or browsing are available.
