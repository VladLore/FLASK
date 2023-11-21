from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()


class Setting(BaseSettings):
    DATABASE_URL: str

    class Config:
        env_file = ".env"


settings = Setting()
