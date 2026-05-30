from abc import ABC, abstractmethod
from app.models import ConnectorResult


class BaseConnector(ABC):
    @abstractmethod
    def search(self, query: str) -> ConnectorResult:
        pass