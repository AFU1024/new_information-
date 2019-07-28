from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_session import Session
import redis
import logging

from config import Config_cho

db = SQLAlchemy()


def create_app(config_name):
    config = Config_cho[config_name]
    setup_log(config)
    app = Flask(__name__)
    app.config.from_object(config)
    db.init_app(app)
    redis_store = redis.StrictRedis(host=config.REDIS_HOST, port=config.REDIS_PORT)
    CSRFProtect(app)
    Session(app)
    return app


def setup_log(config_name):
    logger = logging.getLogger("info")
    logger.setLevel(config_name.LOG_LEVEL)

    fh = logging.FileHandler(r"Logs\log.log", encoding="utf-8")
    ch = logging.StreamHandler()

    formatter = logging.Formatter(
        fmt="%(asctime)s %(name)s %(filename)s %(message)s",
        datefmt="%Y/%m/%d %X"
    )
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)

    logger.addHandler(fh)
    logger.addHandler(ch)


