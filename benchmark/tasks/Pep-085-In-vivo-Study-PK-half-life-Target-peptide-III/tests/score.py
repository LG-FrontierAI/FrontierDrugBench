import json, math, re
from pathlib import Path
HERE=Path(__file__).resolve().parent
DATA=json.loads((HERE/'answer.json').read_text())
GOLD=DATA['answer']
def score(prediction):
    if isinstance(prediction,str):
        prediction=prediction.strip()
        fence=re.fullmatch(r'```(?:json)?\s*\n([\s\S]*?)\n```',prediction)
        if fence:prediction=fence.group(1).strip()
        try: prediction=json.loads(prediction)
        except (ValueError,TypeError): return 0.0
    if not isinstance(prediction,list) or not all(isinstance(x,str) for x in prediction): return 0.0
    if len(prediction)!=len(GOLD) or len(set(prediction))!=len(prediction) or set(prediction)!=set(GOLD): return 0.0
    ranks={x:float(i) for i,x in enumerate(GOLD)}
    for group in DATA.get('tie_groups',[]):
        mean=sum(ranks[x] for x in group)/len(group)
        for x in group:ranks[x]=mean
    x=[ranks[v] for v in prediction];y=list(range(len(x)));n=len(x)
    if n<2:return 1.0
    mx=sum(x)/n;my=sum(y)/n
    denominator=math.sqrt(sum((v-mx)**2 for v in x)*sum((v-my)**2 for v in y))
    if not denominator:return 1.0
    rho=sum((a-mx)*(b-my) for a,b in zip(x,y))/denominator
    # Normalize by maximum attainable rho for this gold tie pattern.
    sorted_x=sorted(x)
    maximum=sum((a-mx)*(b-my) for a,b in zip(sorted_x,y))/denominator
    return max(0.0,min(1.0,(rho/maximum+1)/2))
