import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql

pymysql.install_as_MySQLdb()

app = Flask(__name__)

app.secret_key = os.environ.get("SECRET_KEY", "dev")

app.config["SQLALCHEMY_DATABASE_URI"] = (
    f"mysql+pymysql://{os.environ['MYSQL_USER']}:"
    f"{os.environ['MYSQL_PASSWORD']}@"
    f"{os.environ['MYSQL_HOST']}:"
    f"{os.environ['MYSQL_PORT']}/"
    f"{os.environ['MYSQL_DATABASE']}"
)

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SALT"] = os.environ.get("SALT", "12345")

db = SQLAlchemy(app)

from banking_system import routes
