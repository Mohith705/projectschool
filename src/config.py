from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    DATABASE_URL: str
    REDIS_HOST: str
    REDIS_PORT: int
    REDIS_DB: int
    REDIS_URL: str = "redis://localhost:6379/0"
    CLOUDINARY_CLOUD_NAME: str
    CLOUDINARY_API_KEY: str
    CLOUDINARY_API_SECRET: str

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )

Config = Settings()