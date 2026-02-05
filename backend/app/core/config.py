from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    env: str = "development"
    database_url: str = "sqlite:///./moss.db"
    log_level: str = "INFO"

    model_config = SettingsConfigDict(
        env_prefix="MOSS_",
        case_sensitive=False,
    )


settings = Settings()
