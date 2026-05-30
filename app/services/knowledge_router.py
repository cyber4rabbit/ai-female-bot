from typing import List
from app.utils.keywords import KEYWORD_TO_SOURCE

class KnowledgeRouter:
    def select_sources(self, question: str) -> List[str]:
        question_lower = question.lower()
        selected = set()

        for keyword, source in KEYWORD_TO_SOURCE.items():
            if keyword in question_lower:
                selected.add(source)

        if not selected:
            selected = {"ServiceNow", "Jira", "SharePoint Online"}

        return list(selected)