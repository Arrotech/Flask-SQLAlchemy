import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    """Allow debug to restart after changes."""

    DEBUG = True
    TESTING = False


class TestingConfig(Config):
    """Testing the application."""

    DEBUG = True
    TESTING = True
    DB_NAME = os.getenv('DB_TEST_NAME')


class StagingConfig(Config):
    """Configurations for Staging."""

    DEBUG = True


class ReleaseConfig(Config):
    """Releasing app configurations."""

    DEBUG = False
    TESTING = False


class ProductionConfig(Config):
    """Production configurations."""

    pass


app_config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,
    "default": DevelopmentConfig
}