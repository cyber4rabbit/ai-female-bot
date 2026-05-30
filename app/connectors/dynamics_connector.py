import requests
from app.settings import settings
from app.models import ConnectorResult
from app.connectors.base import BaseConnector


class DynamicsConnector(BaseConnector):
    def search(self, query: str) -> ConnectorResult:
        try:
            url = f"{settings.dynamics_base_url}/api/data/v9.2/accounts"
            headers = {
                "Authorization": f"Bearer {settings.dynamics_token}",
                "Accept": "application/json"
            }
            params = {
                "$top": 5,
                "$filter": f"contains(name, '{query}')"
            }

            response = requests.get(url, headers=headers, params=params, timeout=20)
            response.raise_for_status()

            return ConnectorResult(
                source="Dynamics365",
                success=True,
                data=response.json()
            )
        except Exception as e:
            return ConnectorResult(
                source="Dynamics365",
                success=False,
                error=str(e)
            )