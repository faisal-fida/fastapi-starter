from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Loads the dotenv file. Including this is necessary to get
    pydantic to load a .env file."""

    AUTH0_DOMAIN: str
    CLIENT_ID: str
    CLIENT_SECRET: str
    DATABASE_CONNECTION_URI: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


env = Settings()
