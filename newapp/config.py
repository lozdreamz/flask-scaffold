import os
from dotenv import load_dotenv
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
load_dotenv(PROJECT_ROOT.joinpath('.env'))


class Config(object):
    '''
    Parent configuration class
    '''
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'somesecretbytes'
    DEBUG = False
    ASSETS_DEBUG = False
    DEBUG_TB_ENABLED = False
    DEBUG_TB_INTERCEPT_REDIRECT = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    '''
    Configuration for development
    '''
    DEBUG = True
    DEBUG_TB_ENABLED = True
    ASSETS_DEBUG = True
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
