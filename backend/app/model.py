from typing import List, Dict

class EmojiModel:
    def __init__(self):
        # TODO: 실제 모델/가중치 로딩 (예: Hugging Face, 로컬 모델 경로 등)
        # 무거운 로드는 필요 시 지연 로딩으로 전환 가능
        pass

    def predict(self, text: str) -> List[Dict]:
        # TODO: 실제 추론 로직 대체
        # 아래는 데모용 더미 결과
        baseline = [
            {"emoji": "🙂", "score": 0.85},
            {"emoji": "🤔", "score": 0.10},
            {"emoji": "😢", "score": 0.05},
        ]
        # 간단한 규칙 데모
        if any(w in text.lower() for w in ["sad", "tired", "cry", "down"]):
            baseline[0] = {"emoji": "😢", "score": 0.88}
        if any(w in text.lower() for w in ["lol", "haha", "funny"]):
            baseline[0] = {"emoji": "😂", "score": 0.90}
        if any(w in text.lower() for w in ["angry", "mad"]):
            baseline[0] = {"emoji": "😡", "score": 0.87}
        return baseline
