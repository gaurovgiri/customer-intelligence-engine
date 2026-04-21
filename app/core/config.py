from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_ignore_empty=True
    )

    PROVIDER: str = ""

    GEMINI_API_KEY: str = ""
    GEMINI_CHAT_MODEL: str = ""

    OPENAI_API_KEY: str = ""
    OPENAI_CHAT_MODEL: str = ""


settings = Settings()