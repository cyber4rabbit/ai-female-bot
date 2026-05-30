import requests
from app.settings import settings
from app.models import ConnectorResult
from app.connectors.base import BaseConnector


class ServiceNowConnector(BaseConnector):
    def search(self, query: str) -> ConnectorResult:
        try:
            url = f"{settings.servicenow_base_url}/api/now/table/incident"
            params = {
                "sysparm_query": f"number={query}^ORshort_descriptionLIKE{query}",
                "sysparm_limit": 5
            }

            response = requests.get(
                url,
                auth=(settings.servicenow_user, settings.servicenow_password),
                params=params,
                timeout=20
            )
            response.raise_for_status()

            result = response.json().get("result", [])
            return ConnectorResult(
                source="ServiceNow",
                success=True,
                data={"incidents": result}
            )
        except Exception as e:
            return ConnectorResult(
                source="ServiceNow",
                success=False,
                error=str(e)
            )