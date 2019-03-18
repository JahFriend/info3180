from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


UPLOAD_FOLDER = "./app/static/uploads"
SECRET_KEY = '1234567890'

app.config.from_object(__name__)

db = SQLAlchemy(app)

from app import views