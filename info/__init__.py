from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_session import Session
import redis

from config import Config_cho

db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(Config_cho[config_name])
    db.init_app(app)
    redis_store = redis.StrictRedis(host=Config_cho[config_name].REDIS_HOST, port=Config_cho[config_name].REDIS_PORT)
    CSRFProtect(app)
    Session(app)

    return app
