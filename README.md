# Female Enterprise Assistant AI 👩‍💼

Prototyp inteligentnej asystentki biznesowej (bota) zbudowany w Pythonie z użyciem frameworka FastAPI. Aplikacja przyjmuje zapytania użytkownika, przeszukuje zintegrowane systemy biznesowe (m.in. ServiceNow, Jira, SharePoint) na podstawie analizy słów kluczowych, a następnie agreguje wyniki i zwraca spersonalizowaną odpowiedź w stylu komunikacji asystentki (np. "Alicji").

## 🚀 Możliwości

* **Pojedynczy punkt wejścia (API Layer):** Prosty endpoint HTTP do komunikacji z botem.
* **Inteligentny routing (Knowledge Router):** Dynamiczne dobieranie źródeł danych na podstawie słów kluczowych w zapytaniu (np. słowo "zgłoszenie" kieruje do ServiceNow, a "ticket" do Jira).
* **Agregacja danych:** Łączenie i standaryzacja wyników pochodzących z wielu różnych systemów.
* **Rozszerzalna architektura:** Gotowe klasy bazowe konektorów ułatwiające dodawanie nowych integracji (obecnie wbudowane szkielety dla SAP, Dynamics 365, OneDrive).
* **Personalizacja (Persona Layer):** Przetwarzanie suchych danych technicznych na naturalne, czytelne komunikaty.

## 🛠️ Technologie

* **Python 3.11+**
* **FastAPI** & **Uvicorn** (szybki serwer i automatyczna dokumentacja OpenAPI)
* **Pydantic** (walidacja danych i zarządzanie konfiguracją)
* **Requests / HTTPX** (komunikacja z zewnętrznymi API)
* **Pytest** (testy jednostkowe)

---

## ⚙️ Wymagania wstępne

Aby uruchomić projekt lokalnie lub w chmurze (np. GitHub Codespaces), potrzebujesz:
* Zainstalowanego środowiska Python w wersji 3.11 lub nowszej.
* Zrozumienia podstaw tworzenia środowisk wirtualnych (`venv`).

## 📥 Instalacja i konfiguracja środowiska

**1. Sklonuj repozytorium**
```bash
git clone [https://github.com/TWOJA_NAZWA_UZYTKOWNIKA/ai-female-bot.git](https://github.com/TWOJA_NAZWA_UZYTKOWNIKA/ai-female-bot.git)
cd ai-female-bot
2. Utwórz i aktywuj środowisko wirtualne

Na systemach Linux / macOS / Codespaces:

Bash
python -m venv .venv
source .venv/bin/activate
Na systemach Windows (PowerShell):

PowerShell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
3. Zainstaluj zależności

Bash
pip install -r requirements.txt
4. Skonfiguruj zmienne środowiskowe
Utwórz plik .env w głównym katalogu projektu i uzupełnij go swoimi danymi dostępowymi do systemów zewnętrznych. Szablon pliku:

Fragment kodu
APP_NAME=Female Enterprise Assistant
BOT_NAME=Alicja

# Jira
JIRA_BASE_URL=[https://yourcompany.atlassian.net](https://yourcompany.atlassian.net)
JIRA_EMAIL=student@company.com
JIRA_API_TOKEN=your_jira_token

# ServiceNow
SERVICENOW_BASE_URL=[https://instance.service-now.com](https://instance.service-now.com)
SERVICENOW_USER=admin
SERVICENOW_PASSWORD=your_password

# Microsoft Graph (SharePoint/OneDrive)
MS_TENANT_ID=your_tenant_id
MS_CLIENT_ID=your_client_id
MS_CLIENT_SECRET=your_client_secret
SHAREPOINT_SITE_ID=your_sharepoint_site_id
ONEDRIVE_DRIVE_ID=your_drive_id

# Inne systemy
DYNAMICS_BASE_URL=[https://yourorg.crm4.dynamics.com](https://yourorg.crm4.dynamics.com)
DYNAMICS_TOKEN=your_dynamics_token
SAP_BASE_URL=[https://your-sap-api.company.com](https://your-sap-api.company.com)
SAP_API_KEY=your_sap_api_key
🚦 Uruchomienie aplikacji
Aby uruchomić serwer developerski FastAPI, wykonaj komendę:

Bash
uvicorn app.main:app --reload
Aplikacja będzie dostępna pod adresem: http://127.0.0.1:8000.
Główny adres przekierowuje automatycznie do interaktywnej dokumentacji Swagger UI (/docs), gdzie można przetestować działanie API.

💬 Przykładowe użycie (Endpoint /chat)
Możesz użyć interfejsu Swagger UI (/docs) lub wysłać żądanie cURL:

Żądanie (Request):

Bash
curl -X 'POST' \
  '[http://127.0.0.1:8000/chat](http://127.0.0.1:8000/chat)' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "user_id": "student01",
  "question": "Sprawdź zgłoszenie INC1024 i powiązane zadania z Jira"
}'
Odpowiedź (Response):

JSON
{
  "bot_name": "Alicja",
  "style": "female_assistant",
  "answer": "Jestem Alicja i sprawdziłam dostępne systemy. W ServiceNow znalazłam 1 pasujących zgłoszeń. Nie udało mi się połączyć z: Jira.",
  "sources": [
    "ServiceNow",
    "Jira"
  ],
  "details": {
    "servicenow": {
      "success": true,
      "data": { "incidents": [...] },
      "error": null
    },
    "jira": {
      "success": false,
      "data": {},
      "error": "Błąd autoryzacji / Brak tokenu"
    }
  }
}
🧪 Testy automatyczne
Projekt zawiera podstawowy zestaw testów jednostkowych napisanych przy pomocy pytest. Aby sprawdzić poprawność działania kluczowych endpointów, upewnij się, że masz dodany pusty plik conftest.py w głównym katalogu, a następnie uruchom:

Bash
pytest tests/test_chat.py
