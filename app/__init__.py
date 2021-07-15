import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_jwt_extended import JWTManager
from flask_mail import Mail
from flask_cors import CORS
from flask_migrate import Migrate
from rq import Queue

from app.config import Config
from app.worker import conn

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
api = Api(app)
jwt = JWTManager(app)
mail = Mail(app)
cors = CORS(app, resources={r'/api/*': {'origins': '*'}})
migrate = Migrate(app, db)

q = Queue(connection=conn)


from app import routes
