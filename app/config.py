import os


class Config:

    SECRET_KEY = os.environ.get('SECRET_KEY')
    # os.environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_DATABASE_URI = "sqlite:///portfolio.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_USERNAME = 'lbiggboss19@gmail.com'
    MAIL_PASSWORD = 'coadqjvxcejxpiad'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
