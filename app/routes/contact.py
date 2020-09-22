from flask import make_response
from flask_restful import Resource, reqparse
from app.controllers.contact import add_message
from app import q


class Contact(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(
            'email', type=str, required=True, location='json')
        self.reqparse.add_argument(
            'message', type=str, required=True, location='json')

    def post(self):
        args = self.reqparse.parse_args()
        new_message = q.enqueue(add_message, args)  # add_message(args)

        print(q.all())
        print(len(q))

        return make_response({'success': True}, 200)
