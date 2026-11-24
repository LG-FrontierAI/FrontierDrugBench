import json
from pathlib import Path
GOLD=json.loads((Path(__file__).resolve().parent/"answer.json").read_text(encoding="utf-8"))["answer"]
def score(prediction):
    try:
        pred=json.loads(prediction) if isinstance(prediction,str) else prediction
    except Exception:
        return 0.0
    if not isinstance(pred,list) or len(pred)!=len(GOLD): return 0.0
    if not all(isinstance(candidate, str) for candidate in pred): return 0.0
    if len(set(pred))!=len(pred) or set(pred)!=set(GOLD): return 0.0
    n=len(GOLD); d=sum(1 for i in range(n) for j in range(i+1,n) if (pred.index(GOLD[i])-pred.index(GOLD[j]))*(i-j)<0)
    pairs=n*(n-1)//2
    return 1.0 if pairs==0 else 1-d/pairs
if __name__=="__main__": print({"gold":GOLD,"score":score(json.dumps(GOLD))})
