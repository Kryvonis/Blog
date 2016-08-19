import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECREY_KEY = os.environ.get('SECRET_KEY') or 'hfasfuahfjanbxvpqrwtqtkljbmcx,vxnxjiree'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
    FLASKY_MAIL_SENDER = ''

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 487


class TestingConfig(Config):
    TESTING = True


# class ProductionConfig(Config):

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
}
