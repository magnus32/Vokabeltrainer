import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'eine_sehr_geheime_schluessel'
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'instance', 'vokabeltrainer.sqlite')
    SQLALCHEMY_TRACK_MODIFICATIONS = False