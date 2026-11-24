---
bench_id: "RV1-kinase-AK2011-B07-Q01"
category: "Disease-Biology"
title: "Biochemical/cellular phenotype and candidate activity prediction (Binary): Predict the hidden operational inhibition cat"
format: "mcq"
input_mode: "inline_prompt"
---

# Prompt

## Instructions

Answer this biological benchmark using only the content, definitions, evidence and numerical data supplied in this question. Do not browse, search, retrieve, call tools, use external files, consult previous questions or conversations, or use remembered publications, experimental outcomes, drug facts, or outside factual knowledge as evidence. Reason only from the supplied information. No tools are available. Return only the final option code, ordered candidate-ID JSON array, or candidate-ID set JSON array specified in the question. Do not include explanation, reasoning, confidence, citations, Markdown or any additional fields.

## Task

{"assay":{"ATP_uM":10,"CAS":"913844-45-8","compound":"Rho Kinase Inhibitor IV","compound_uM":0.5,"endpoint":"R = remaining substrate phosphorylation (% of solvent control), background corrected, published duplicate means; lower means stronger inhibition","limits":"Not Kd, IC50 or cellular drug response. Construct/substrate differences retained; individual replicate errors unavailable. >100% is not automatically activation.","platform":"HotSpot radiometric recombinant human kinase functional assay","preincubation_minutes_approx":20,"reaction":"120 minutes at room temperature"},"candidates":[{"construct":"aa 1-535","expression":"Insect","id":"C1","kinase":"ROCK1","mutation":"-","substrate":"Long S6 Kinase substrate peptide","symbol":"ROCK1","tag":"N-terminal GST"}],"id":"RV1-kinase-AK2011-B07-Q01","language":"en","mechanism":"The compound is annotated as Rho Kinase Inhibitor IV. ROCK-family ATP-pocket similarity supplies a mechanistic prior; activity on other AGC kinases must be inferred from comparative functional profiles, not the catalog name. Differences in constructs and substrates remain relevant.","options":{"A":"R >= 50%","B":"R < 50%"},"output_instruction":"Return only one option code.","question":"Predict the hidden operational inhibition category of C1.","reference_compounds":[{"CAS":"146986-50-7","R":31.5176827406219,"compound":"ROCK Inhibitor, Y-27632","kinase":"ROCK1"},{"CAS":"62996-74-1","R":0.6112952101132205,"compound":"Staurosporine, Streptomyces sp.","kinase":"ROCK1"}],"reference_selection":"Same target compound on other kinases from the listed biologically related families; same candidate constructs with preselected class-relevant reference compounds. All pool target cells globally masked; no response-based reference selection. A dash in source mutation metadata does not establish wild type.","related_families":["ROCK","PRKX","PKA","PKG","PKC","RSK"],"same_compound_other_kinases":[{"R":99.47193149743885,"kinase":"PKA"},{"R":111.92430225943068,"kinase":"PKAcg"},{"R":108.72104149864455,"kinase":"PKCa"},{"R":99.4352050466202,"kinase":"PKCb1"},{"R":91.27416833347004,"kinase":"PKCb2"},{"R":52.3698095036151,"kinase":"PKCepsilon"},{"R":34.42808089234184,"kinase":"PKCeta"},{"R":100.80339495146166,"kinase":"PKCg"},{"R":87.44297211531679,"kinase":"PKCiota"},{"R":96.69459499121157,"kinase":"PKCmu/PRKD1"},{"R":85.42378610490128,"kinase":"PKCnu/PRKD3"},{"R":105.1257026443357,"kinase":"PKCtheta"},{"R":91.24884221189495,"kinase":"PKCzeta"},{"R":78.6905498549197,"kinase":"PKG1a"},{"R":85.03694759216539,"kinase":"PKG1b"},{"R":88.05731218271583,"kinase":"PKG2/PRKG2"},{"R":3.2245236342477677,"kinase":"ROCK2"},{"R":90.44425629738325,"kinase":"RSK1"},{"R":91.8184293291273,"kinase":"RSK2"},{"R":89.17474828764088,"kinase":"RSK3"},{"R":104.51301714242697,"kinase":"RSK4"}],"task_type":"Binary"}

## Options

A. R >= 50%
B. R < 50%
