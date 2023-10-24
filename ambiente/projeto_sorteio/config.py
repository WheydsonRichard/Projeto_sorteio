# configuraçao do banco de dados
import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get('URL_BANCO_DE_DADOS') or 'sqlite:///site.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False