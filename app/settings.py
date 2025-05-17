from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql+psycopg2://postgres:Rahul5.7@postgres:5432/notification"
    RABBITMQ_BROKER: str = "amqp://guest:guest@rabbitmq:5672//"
    EMAIL_FROM: str = "no-reply@example.com"
    RETRY_BACKOFF: int = 30
    MAX_RETRIES: int = 3

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
