import pickle
from typing import List, Any


class RecommendService:
    def __init__(self, model_path: str):
        with open(model_path, "rb") as f:
            data = pickle.load(f)

        # load components
        self.svd = data["model"]
        self.all_services = data["services"]
        self.scaler = data.get("scaler")
        self.le = data.get("le")

    def recommend(self, customer_id: Any, n: int = 3) -> List[str]:
        customer_id = str(customer_id)

        scores = [
            (svc, self.svd.predict(customer_id, svc).est)
            for svc in self.all_services
        ]

        scores.sort(key=lambda x: x[1], reverse=True)

        return [svc for svc, _ in scores[:n]]