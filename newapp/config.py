import os
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]


class Config(object):
    '''
    Parent configuration class
    '''
    DEBUG = False
    ASSETS_DEBUG = False
    DEBUG_TB_ENABLED = False
    DEBUG_TB_INTERCEPT_REDIRECT = False

    SECRET_KEY = os.getenv('APP_SECRET')

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')


class DevelopmentConfig(Config):
    '''
    Configuration for development
    '''
    DEBUG = True
    DEBUG_TB_ENABLED = True
    ASSETS_DEBUG = True

    SECRET_KEY = os.getenv('APP_SECRET') or 'newsecret'
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{PROJECT_ROOT.joinpath("dev.db")}'


class TestingConfig(Config):
    '''
    Configuration for testing with a separate database
    '''
    DEBUG = True
    TESTING = True

    SQLALCHEMY_ECHO = False
    # SQLALCHEMY_DATABASE_URI = f'sqlite:///{PROJECT_ROOT.joinpath("test.db")}'
    SQLALCHEMY_DATABASE_URI = 'sqlite://'


class ProductionConfig(Config):
    '''
    Configuration for production
    '''
    DEBUG = False
    TESTING = False


app_config = {
    'dev': DevelopmentConfig,
    'testing': TestingConfig,
    'prod': ProductionConfig
}
