import os
from dotenv import load_dotenv

# 루트 폴더의 .env 파일 로드
load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'secret_key_1234!@#$')
    DB_HOST = os.getenv('DB_HOST', 'localhost')
    DB_USER = os.getenv('DB_USER', 'root')
    DB_PASSWORD = os.getenv('DB_PASSWORD', '1234')
    DB_NAME = os.getenv('DB_NAME', 'test')
    DB_PORT = int(os.getenv('DB_PORT', 3306))

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False

config_dict = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}