from pydantic import BaseSettings

class Settings(BaseSettings):
    EMAIL_TEMPLATES_DIR: str = "/app/app/core/shared/email_templates/build"

settings = Settings()
