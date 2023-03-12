from flask import Flask, json
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from sqlalchemy.orm import sessionmaker
from werkzeug.routing import BaseConverter
import decimal
from flask_login import LoginManager
from config import load_config


ApplicationConfig = load_config()
app = Flask(__name__)
app.config.from_object(ApplicationConfig)
session = sessionmaker()

check_enviroment = ApplicationConfig.CURRENT_SETTINGS
print(f"starting server with {check_enviroment} settings")






class RegexConverter(BaseConverter):
    def __init__(self, url_map, *items):
        super(RegexConverter, self).__init__(url_map)
        self.regex = items[0]


class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            return float(o)
        return super(DecimalEncoder, self).default(o)


app.url_map.converters['regex'] = RegexConverter
app.json_encoder = DecimalEncoder



session.configure(bind=ApplicationConfig.SQLALCHEMY_DATABASE_URI_0)
db = SQLAlchemy(app)
server_session = Session(app)
ma = Marshmallow(app)
login_manager = LoginManager(app)



# link locations
from .main import main as main_blueprint
app.register_blueprint(main_blueprint, url_prefix='/main')


