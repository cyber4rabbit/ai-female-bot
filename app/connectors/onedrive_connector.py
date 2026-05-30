import requests
from app.models import ConnectorResult
from app.connectors.base import BaseConnector


class OneDriveConnector(BaseConnector):
    def __init__(self, access_token: str):
        self.access_token = access_token

    def search(self, query: str) -> ConnectorResult:
        try:
            url = "https://graph.microsoft.com/v1.0/me/drive/root/search(q='{}')".format(query)
            headers = {
                "Authorization": f"Bearer {self.access_token}"
            }

            response = requests.get(url, headers=headers, timeout=20)
            response.raise_for_status()

            return ConnectorResult(
                source="OneDrive",
                success=True,
                data=response.json()
            )
        except Exception as e:
            return ConnectorResult(
                source="OneDrive",
                success=False,
                error=str(e)
            )