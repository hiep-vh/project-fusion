import os
from urllib.parse import quote_plus

class Config:
    password = quote_plus(os.getenv('POSTGRES_PASSWORD', 'Aa@123456'))
    SQLALCHEMY_DATABASE_URI = f"postgresql://root:{password}@host.docker.internal:5432/projects_fusion"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # SECRET_KEY = os.getenv('SECRET_KEY', 'dev')
