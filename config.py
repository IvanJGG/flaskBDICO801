import os 
from sqlalchemy import create_engine

class Config(object):
    SECRET_KEY = "clave_secreta"
    SESSION_COOKIE_sECURE = False

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://jesus:rootwan@localhost/ico801'
    SQLALCHEMY_TRACK_MODIFICATIONS = False