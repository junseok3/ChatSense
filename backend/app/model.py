from typing import List, Dict


class EmojiModel:
    def __init__(self):
        
        pass

    def predict(self, text: str) -> List[Dict]:
       
        baseline = [
            {"emoji": "🙂", "score": 0.85},
            {"emoji": "🤔", "score": 0.10},
            {"emoji": "😢", "score": 0.05},
        ]
       
        if any(w in text.lower() for w in ["sad", "tired", "cry", "down"]):
            baseline[0] = {"emoji": "😢", "score": 0.88}
        if any(w in text.lower() for w in ["lol", "haha", "funny"]):
            baseline[0] = {"emoji": "😂", "score": 0.90}
        if any(w in text.lower() for w in ["angry", "mad"]):
            baseline[0] = {"emoji": "😡", "score": 0.87}
        return baseline
