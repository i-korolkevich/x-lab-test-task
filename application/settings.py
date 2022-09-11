from pydantic import BaseSettings, BaseModel


class DadataParams(BaseModel):
    url: str
    token: str


class Settings(BaseSettings):
    database_url: str
    redis_url: str
    dadata_params: DadataParams
    cache_lifetime_sec: int

    class Config:
        env_nested_delimiter = '__'


settings = Settings()


def get_settings() -> Settings:
    return settings
