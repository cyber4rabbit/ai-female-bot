import requests
from app.settings import settings
from app.models import ConnectorResult
from app.connectors.base import BaseConnector


class SAPConnector(BaseConnector):
    def search(self, query: str) -> ConnectorResult:
        try:
            url = f"{settings.sap_base_url}/search"
            headers = {
                "x-api-key": settings.sap_api_key,
                "Accept": "application/json"
            }
            payload = {
                "query": query,
                "limit": 5
            }

            response = requests.post(url, headers=headers, json=payload, timeout=20)
            response.raise_for_status()

            return ConnectorResult(
                source="SAP",
                success=True,
                data=response.json()
            )
        except Exception as e:
            return ConnectorResult(
                source="SAP",
                success=False,
                error=str(e)
            )