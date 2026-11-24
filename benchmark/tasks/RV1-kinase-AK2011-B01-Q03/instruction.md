---
bench_id: "RV1-kinase-AK2011-B01-Q03"
category: "Disease-Biology"
title: "Biochemical/cellular phenotype and candidate activity prediction (Pairwise): Predict which candidate has the lower hidden"
format: "mcq"
input_mode: "inline_prompt"
---

# Prompt

## Instructions

Answer this biological benchmark using only the content, definitions, evidence and numerical data supplied in this question. Do not browse, search, retrieve, call tools, use external files, consult previous questions or conversations, or use remembered publications, experimental outcomes, drug facts, or outside factual knowledge as evidence. Reason only from the supplied information. No tools are available. Return only the final option code, ordered candidate-ID JSON array, or candidate-ID set JSON array specified in the question. Do not include explanation, reasoning, confidence, citations, Markdown or any additional fields.

## Task

{"assay":{"ATP_uM":10,"CAS":"879127-07-8","compound":"EGFR Inhibitor","compound_uM":0.5,"endpoint":"R = remaining substrate phosphorylation (% of solvent control), background corrected, published duplicate means; lower means stronger inhibition","limits":"Not Kd, IC50 or cellular drug response. Construct/substrate differences retained; individual replicate errors unavailable. >100% is not automatically activation.","platform":"HotSpot radiometric recombinant human kinase functional assay","preincubation_minutes_approx":20,"reaction":"120 minutes at room temperature"},"candidates":[{"construct":"aa 1-473","expression":"Baculovirus infected insect cells","id":"C1","kinase":"MRCKa/CDC42BPA","mutation":"-","substrate":"Long S6 Kinase substrate peptide","symbol":"CDC42BPA","tag":"C-terminal 6X-His tag"},{"construct":"cytoplasmic","expression":"Insect","id":"C2","kinase":"EGFR","mutation":"-","substrate":"pEY + Mn","symbol":"EGFR","tag":"N-terminal GST"}],"id":"RV1-kinase-AK2011-B01-Q03","language":"en","mechanism":"The compound is annotated as an EGFR-directed kinase inhibitor. Related receptor-kinase ATP pockets motivate comparison, but ErbB-family membership does not imply identical binding or catalytic inhibition. The reference compounds measure how the candidate constructs differ under the same functional assay.","options":{"A":"C2 has lower R","B":"C1 has lower R"},"output_instruction":"Return only one option code.","question":"Predict which candidate has the lower hidden remaining catalytic activity R.","reference_compounds":[{"CAS":"183319-69-9","R":88.48938036348294,"compound":"Erlotinib","kinase":"MRCKa/CDC42BPA"},{"CAS":"183319-69-9","R":4.208336486907063,"compound":"Erlotinib","kinase":"EGFR"},{"CAS":"220127-57-1","R":86.68347817163743,"compound":"Imatinib","kinase":"MRCKa/CDC42BPA"},{"CAS":"220127-57-1","R":92.02543420944863,"compound":"Imatinib","kinase":"EGFR"},{"CAS":"146986-50-7","R":83.35175103298513,"compound":"ROCK Inhibitor, Y-27632","kinase":"MRCKa/CDC42BPA"},{"CAS":"146986-50-7","R":96.0733509947863,"compound":"ROCK Inhibitor, Y-27632","kinase":"EGFR"}],"reference_selection":"Same target compound on other kinases from the listed biologically related families; same candidate constructs with preselected class-relevant reference compounds. All pool target cells globally masked; no response-based reference selection. A dash in source mutation metadata does not establish wild type.","related_families":["EGFR","ERBB","FGFR","PDGFR","IR","MRCK","ROCK"],"same_compound_other_kinases":[{"R":102.91035373854655,"kinase":"FGFR1"},{"R":104.68880025218077,"kinase":"FGFR2"},{"R":102.05021689934875,"kinase":"FGFR3"},{"R":101.79036015414832,"kinase":"FGFR4"},{"R":103.14719034008488,"kinase":"IR"},{"R":110.96005090742247,"kinase":"IRAK1"},{"R":104.42347180411375,"kinase":"IRAK4"},{"R":101.16055726288147,"kinase":"IRR/INSRR"},{"R":97.36950642723954,"kinase":"MRCKb/CDC42BPB"},{"R":86.35886869774487,"kinase":"PDGFRa"},{"R":101.1589990020983,"kinase":"PDGFRb"},{"R":98.66676843140357,"kinase":"ROCK1"},{"R":99.19613991322439,"kinase":"ROCK2"}],"task_type":"Pairwise"}

## Options

A. C2 has lower R
B. C1 has lower R
