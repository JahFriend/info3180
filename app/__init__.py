from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


SQLALCHEMY_DATABASE_URI = "postgresql://bread:test@localhost/project1"
SQLALCHEMY_TRACK_MODIFICATIONS = False # added just to suppress a warning
UPLOAD_FOLDER = "./app/static/uploads"
SECRET_KEY= "MYKEY"

app.config.from_object(__name__)

db = SQLAlchemy(app)

from app import views