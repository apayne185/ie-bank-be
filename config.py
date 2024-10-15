# from dotenv import load_dotenv
import os

# load_dotenv()


class Config(object):
    # SECRET_KEY = 'this-really-needs-to-be-changed'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = False


class LocalConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///local.db'
    DEBUG = True


class GithubCIConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'
    DEBUG = True


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql://{dbuser}:{dbpass}@{dbhost}/{dbname}'.format(
        dbuser=os.getenv('DBUSER'),
        dbpass=os.getenv('DBPASS'),
        dbhost=os.getenv('DBHOST'),
        dbname=os.getenv('DBNAME')
    )
    DEBUG = True

class UatConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql://{dbuser}:{dbpass}@{dbhost}/{dbname}'.format(
    dbuser=os.getenv('UAT_DBUSER'),
    dbpass=os.getenv('UAT_DBPASS'),
    dbhost=os.getenv('UAT_DBHOST'),
    dbname=os.getenv('UAT_DBNAME')
    )
    DEBUG = False