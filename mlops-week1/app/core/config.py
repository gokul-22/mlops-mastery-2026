from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import List

class Settings(BaseSettings):
    """
    Project settings and configuration management using Pydantic V2.
    """
    
    # Project Information
    PROJECT_NAME: str = "Image Classification API"
    VERSION: str = "1.0.0"
    API_V1_STR: str = "/api/v1"
    
    # Model Configuration
    MODEL_NAME: str = "mobilenet_v3_small"
    TOP_K: int = 3
    
    # Server Configuration
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    DEBUG: bool = False
    
    # CORS Configuration
    BACKEND_CORS_ORIGINS: List[str] = ["http://localhost:3000"]

    # Env File Configuration (Pydantic V2 way)
    model_config = SettingsConfigDict(
        case_sensitive=True,
        env_file=".env",
        env_file_encoding="utf-8"
    )

# Instantiate a global settings object for the entire app
settings = Settings()
