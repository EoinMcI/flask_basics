""" eoincode/config.py"""


class Config(object):
    """
    Common configurations
    """
    DEBUG = False


class DevelopmentConfig(Config):
    """
    Development configurations
    """

    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    DEBUG = True
    WTF_CSRF_ENABLED = False


class ProductionConfig(Config):
    """
    Production configurations
    """

    DEBUG = False
    DEBUG_TB_ENABLED = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(Config):
    """
    Testing configurations
    """
    DEBUG_TB_ENABLED = False
    WTF_CSRF_ENABLED = False
    TESTING = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False

app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig
}
