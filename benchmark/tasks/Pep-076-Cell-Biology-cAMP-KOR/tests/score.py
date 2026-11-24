import json
from pathlib import Path
GOLD=json.loads((Path(__file__).resolve().parent/'answer.json').read_text())['answer']
def score(prediction):
    return float(isinstance(prediction,str) and prediction.strip().upper()==GOLD)
