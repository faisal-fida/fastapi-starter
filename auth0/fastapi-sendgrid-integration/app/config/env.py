from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Loads the dotenv file. Including this is necessary to get
    pydantic to load a .env file."""

    SUPPORT_EMAIL_ADDRESS: str
    SENDGRID_API_KEY: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


env = Settings()
