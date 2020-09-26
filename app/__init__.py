import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_jwt_extended import JWTManager
from flask_mail import Mail
from rq import Queue
from redis import Redis, from_url

from app.config import Config


app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
api = Api(app)
jwt = JWTManager(app)
mail = Mail(app)

if os.environ.get('REDISTOGO_URL'):
    r = from_url(os.environ.get('REDISTOGO_URL'))
else:
    r = Redis()
q = Queue(connection=r)


from app import routes
