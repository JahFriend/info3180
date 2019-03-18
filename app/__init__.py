from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "MYKEY"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://user1:test@localhost/WebDev"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning


UPLOAD_FOLDER = "./app/static/uploads"


app.config.from_object(__name__)

db = SQLAlchemy(app)

from app import views