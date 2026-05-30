from typing import List, Dict, Any
from app.models import ConnectorResult


class Aggregator:
    def to_response_details(self, results: List[ConnectorResult]) -> Dict[str, Any]:
        payload = {}
        for result in results:
            payload[result.source.lower().replace(" ", "_")] = {
                "success": result.success,
                "data": result.data,
                "error": result.error
            }
        return payload