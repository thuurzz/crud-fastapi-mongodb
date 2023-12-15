from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # Configurações do banco de dados
    DATABASE_URL: str

    # Outras configurações gerais
    APP_NAME: str
    APP_VERSION: str

    class Config:
        # Este atributo indica se as variáveis de ambiente devem ser lidas
        # caso as mesmas não sejam passadas explicitamente na criação da instância de Settings.
        env_file = ".env"

settings = Settings()

