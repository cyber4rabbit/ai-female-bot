from typing import List
from app.models import ConnectorResult
from app.settings import settings


class PersonaService:
    def build_answer(self, question: str, results: List[ConnectorResult]) -> str:
        successful = [r for r in results if r.success]
        failed = [r for r in results if not r.success]

        if not successful:
            return (
                f"Jestem {settings.bot_name}. Nie udało mi się pobrać danych z żadnego źródła. "
                f"Sprawdź konfigurację konektorów i poświadczenia dostępowe."
            )

        parts = [f"Jestem {settings.bot_name} i sprawdziłam dostępne systemy."]

        for result in successful:
            if result.source == "ServiceNow":
                count = len(result.data.get("incidents", []))
                parts.append(f"W ServiceNow znalazłam {count} pasujących zgłoszeń.")
            elif result.source == "Jira":
                count = len(result.data.get("issues", []))
                parts.append(f"W Jira znalazłam {count} powiązanych zadań.")
            else:
                parts.append(f"Pobrałam również dane ze źródła: {result.source}.")

        if failed:
            failed_names = ", ".join([r.source for r in failed])
            parts.append(f"Nie udało mi się połączyć z: {failed_names}.")

        return " ".join(parts)