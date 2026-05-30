import requests
from app.settings import settings
from app.models import ConnectorResult
from app.connectors.base import BaseConnector


class SharePointConnector(BaseConnector):
    def __init__(self, access_token: str):
        self.access_token = access_token

    def search(self, query: str) -> ConnectorResult:
        try:
            url = "https://graph.microsoft.com/v1.0/search/query"
            headers = {
                "Authorization": f"Bearer {self.access_token}",
                "Content-Type": "application/json"
            }
            payload = {
                "requests": [
                    {
                        "entityTypes": ["driveItem"],
                        "query": {
                            "queryString": f"{query}"
                        },
                        "from": 0,
                        "size": 5
                    }
                ]
            }

            response = requests.post(url, headers=headers, json=payload, timeout=20)
            response.raise_for_status()

            return ConnectorResult(
                source="SharePoint Online",
                success=True,
                data=response.json()
            )
        except Exception as e:
            return ConnectorResult(
                source="SharePoint Online",
                success=False,
                error=str(e)
            )