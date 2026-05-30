from typing import List
from app.models import ConnectorResult, ChatResponse
from app.settings import settings
from app.services.knowledge_router import KnowledgeRouter
from app.services.aggregator import Aggregator
from app.services.persona_service import PersonaService

from app.connectors.jira_connector import JiraConnector
from app.connectors.servicenow_connector import ServiceNowConnector
from app.connectors.sap_connector import SAPConnector
from app.connectors.dynamics_connector import DynamicsConnector
from app.connectors.sharepoint_connector import SharePointConnector
from app.connectors.onedrive_connector import OneDriveConnector


class BotService:
    def __init__(self, graph_token: str = "mock_graph_token"):
        self.router = KnowledgeRouter()
        self.aggregator = Aggregator()
        self.persona_service = PersonaService()

        self.connectors = {
            "Jira": JiraConnector(),
            "ServiceNow": ServiceNowConnector(),
            "SAP": SAPConnector(),
            "Dynamics365": DynamicsConnector(),
            "SharePoint Online": SharePointConnector(graph_token),
            "OneDrive": OneDriveConnector(graph_token),
        }

    def handle_question(self, question: str) -> ChatResponse:
        selected_sources = self.router.select_sources(question)

        results: List[ConnectorResult] = []
        for source in selected_sources:
            connector = self.connectors.get(source)
            if connector:
                results.append(connector.search(question))

        answer = self.persona_service.build_answer(question, results)
        details = self.aggregator.to_response_details(results)

        return ChatResponse(
            bot_name=settings.bot_name,
            style="female_assistant",
            answer=answer,
            sources=selected_sources,
            details=details
        )