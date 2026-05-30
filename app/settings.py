from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Female Enterprise Assistant"
    bot_name: str = "Alicja"

    jira_base_url: str = ""
    jira_email: str = ""
    jira_api_token: str = ""

    servicenow_base_url: str = ""
    servicenow_user: str = ""
    servicenow_password: str = ""

    ms_tenant_id: str = ""
    ms_client_id: str = ""
    ms_client_secret: str = ""

    sharepoint_site_id: str = ""
    onedrive_drive_id: str = ""

    dynamics_base_url: str = ""
    dynamics_token: str = ""

    sap_base_url: str = ""
    sap_api_key: str = ""

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


settings = Settings()