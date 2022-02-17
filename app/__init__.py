from flask import Flask

from flask_sqlalchemy import SQLAlchemy
from config import ConfigMain


app = Flask(__name__)
app.config.from_object('ConfigMain')
app.config['SQLALCHEMY_DATABASE_URI'] = ConfigMain.SQLALCHEMY_DATABASE_URI_0
app.config['SQLALCHEMY_BINDS'] = ConfigMain.SQLALCHEMY_BINDS


db = SQLAlchemy(app)
