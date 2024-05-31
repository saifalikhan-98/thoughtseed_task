from typing import List, Union
from pydantic.networks import AnyHttpUrl
from pydantic.v1 import BaseSettings

"""
    This class contains all the configuration required for the project
"""
class Settings(BaseSettings):
    # General Settings
    DEBUG: bool = True
    PROJECT_NAME: str = "Thought Seed Assignment"
    ALLOWED_HOSTS: List[str] = ["*"]
    BACKEND_CORS_ORIGINS: List[Union[str, AnyHttpUrl]] = [
        "http://localhost:8000",
        "http://localhost:3000",
    ]


settings = Settings()