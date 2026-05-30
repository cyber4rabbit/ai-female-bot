import requests
from requests.auth import HTTPBasicAuth
from app.settings import settings
from app.models import ConnectorResult
from app.connectors.base import BaseConnector


class JiraConnector(BaseConnector):
    def search(self, query: str) -> ConnectorResult:
        try:
            url = f"{settings.jira_base_url}/rest/api/3/search"
            jql = f'text ~ "{query}"'
            params = {"jql": jql, "maxResults": 5}
            auth = HTTPBasicAuth(settings.jira_email, settings.jira_api_token)
            headers = {"Accept": "application/json"}

            response = requests.get(url, headers=headers, params=params, auth=auth, timeout=20)
            response.raise_for_status()

            issues = response.json().get("issues", [])
            return ConnectorResult(
                source="Jira",
                success=True,
                data={"issues": issues}
            )
        except Exception as e:
            return ConnectorResult(
                source="Jira",
                success=False,
                error=str(e)
            )