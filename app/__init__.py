from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_jwt_extended import JWTManager
from flask_mail import Mail
from rq import Queue
from redis import Redis

from app.config2 import Config


app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
api = Api(app)
jwt = JWTManager(app)
r = Redis()
q = Queue(connection=r)
mail = Mail(app)

# print(app.config)

from app import routes
