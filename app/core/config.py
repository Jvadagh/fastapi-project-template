from pathlib import Path
from typing import Literal
from pydantic_settings import BaseSettings

PROJECT_DIR = Path(__file__).parent.parent.parent


class Settings(BaseSettings):
    ENVIRONMENT: Literal["PRODUCTION", "MIGRATION", "DEVELOPMENT", "MAINTENANCE"]
    TIME_ZONE: str = "Asia/Tehran"

    class Config:
        env_file = f"{PROJECT_DIR}/.env"
        case_sensitive = True
        extra = "allow"


class ProductionEnvironmentSetting(Settings):
    DATABASE_URL: str
    MAINTENANCE_MODE: bool = False
    DEBUG_MODE: bool = False


class DevelopmentEnvironmentSetting(Settings):
    DATABASE_URL: str
    MAINTENANCE_MODE: bool = False
    DEBUG_MODE: bool = True


class MaintenanceEnvironmentSetting(Settings):
    DATABASE_URL: str
    MAINTENANCE_MODE: bool = True
    DEBUG_MODE: bool = True


class MigrationEnvironmentSetting(Settings):
    ALEMBIC_URL: str
    MAINTENANCE_MODE: bool = True
    DEBUG_MODE: bool = False


base_settings = Settings()

if base_settings.ENVIRONMENT == "DEVELOPMENT":
    settings = DevelopmentEnvironmentSetting()

elif base_settings.ENVIRONMENT == "MIGRATION":
    settings = MigrationEnvironmentSetting()

elif base_settings.ENVIRONMENT == "MAINTENANCE":
    settings = MaintenanceEnvironmentSetting()

elif base_settings.ENVIRONMENT == "PRODUCTION":
    settings = ProductionEnvironmentSetting()
