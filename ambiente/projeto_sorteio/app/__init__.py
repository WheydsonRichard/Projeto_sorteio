#Configuraçao da REST API E Webhooks
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from ..config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

from app.routes import api
app.register_blueprint(api, url_prefix='/api')