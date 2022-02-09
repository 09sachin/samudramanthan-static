from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from decouple import config
app=Flask(__name__,template_folder="templates")
app.secret_key=config("app_secret_key")
app.config["SQLALCHEMY_DATABASE_URI"]='sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db=SQLAlchemy(app)
from . import routes