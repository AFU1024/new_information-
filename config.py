import redis


class Config(object):
    """工程配置信息"""

    # mysql数据库配置
    SQLALCHEMY_DATABASE_URI = "mysql://root:msyql@192.168.47.134:3306/information22"
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    # redis数据库配置
    REDIS_HOST = "192.168.47.134"
    REDIS_PORT = 6379

    SECRET_KEY = "E24RE4T314HRTSHRTT55WHRTHuE4DFG2kTfQUs8yCM6xX9Yjq52v54g+HVoknA"
    SESSION_TYPE = "redis"
    SESSION_USE_SIGNER = True
    SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT)
    PERMANENT_SESSION_LIFETIME = 86400


class DevelopConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    pass


Config_cho = {
    "develop": DevelopConfig,
    "production": ProductionConfig
}