from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "Customer Analytics"
    DATABASE_URL: str = "mysql+pymysql://root:senha@localhost:3306/customer_analytics"
    
    class Config:
        env_file = ".env"
        
settings = Settings()