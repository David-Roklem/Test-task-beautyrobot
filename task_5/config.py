from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_title: str = 'Webhook handler example app'

    WEBHOOK_SECRET: str

    model_config = SettingsConfigDict(env_file='.env', extra='ignore')


settings = Settings()
