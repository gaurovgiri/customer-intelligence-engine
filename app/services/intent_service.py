import pickle
from pathlib import Path
from typing import Optional, Tuple


class IntentService:
    def __init__(self, pipeline=None, threshold: float = 0.55):
        self.pipeline = pipeline
        self.threshold = threshold

    @classmethod
    def from_path(cls, model_path: str, threshold: float = 0.55):
        if not model_path:
            return cls(pipeline=None, threshold=threshold)

        path = Path(model_path)
        if not path.exists() or not path.is_file():
            return cls(pipeline=None, threshold=threshold)

        with path.open("rb") as f:
            loaded_obj = pickle.load(f)

        pipeline = loaded_obj
        if isinstance(loaded_obj, dict):
            # Some serialized artifacts store metadata and keep the trained model in `pipeline`.
            pipeline = loaded_obj.get("pipeline")

        if pipeline is None or not hasattr(pipeline, "predict"):
            return cls(pipeline=None, threshold=threshold)

        return cls(pipeline=pipeline, threshold=threshold)

    def _confidence(self, text: str, predicted_label: str) -> float:
        if self.pipeline is None:
            return 0.0

        if not hasattr(self.pipeline, "predict_proba"):
            return 1.0

        try:
            probabilities = self.pipeline.predict_proba([text])[0]
            classes = getattr(self.pipeline, "classes_", None)

            if classes is None:
                return float(max(probabilities))

            class_to_idx = {label: idx for idx, label in enumerate(classes)}
            idx = class_to_idx.get(predicted_label)
            if idx is None:
                return float(max(probabilities))

            return float(probabilities[idx])
        except (AttributeError, TypeError, ValueError):
            return 0.0

    def predict(self, text: str) -> Tuple[Optional[str], float]:
        if self.pipeline is None:
            return None, 0.0

        try:
            intent = str(self.pipeline.predict([text])[0])
        except (AttributeError, TypeError, ValueError):
            return None, 0.0

        confidence = self._confidence(text, intent)
        return intent, confidence
