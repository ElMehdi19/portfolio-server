from flask import make_response
from flask_restful import Resource, reqparse
from flask_jwt_extended import create_access_token

from app.controllers.auth import authenticate, identity

class Login(Resource):

    def __init__(self):

        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('key', type=str, required=True, location='json')

    def post(self):
        
        req_args = self.reqparse.parse_args()
        req_key = req_args['key']

        if not authenticate(req_key):
            return make_response({ 'success': False, 'data': 'Invalid API Key' }, 401)

        access_token = create_access_token(identity())
        
        return make_response({ 'success': True, 'token': access_token }, 200)