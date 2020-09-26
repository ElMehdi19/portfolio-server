from flask import make_response, request
from flask_restful import Resource, reqparse
from flask_jwt_extended import (
    jwt_required,
    create_access_token,
    get_jwt_identity
)

from app import app, q
from app.controllers.auth import is_admin
from app.controllers.contact import (
    check_email,
    send_email,
    add_message,
    fetch_clients
)


class Contact(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(
            'email', type=str, required=True, location='json')
        self.reqparse.add_argument(
            'message', type=str, required=True, location='json')

    def get(self):
        token = create_access_token({'user': request.remote_addr})
        return make_response({'token': token})

    @jwt_required
    def post(self):
        args = self.reqparse.parse_args()
        payload = {
            'email': args.get('email'),
            'message': args.get('message'),
            'ip_addr': request.remote_addr
        }
        q.enqueue(add_message, payload)

        if check_email(payload['email']):
            mail_payload = {
                'email': payload.get('email'),
                'message': payload.get('message')
            }
            q.enqueue(send_email, **mail_payload)

        return make_response({'success': True}, 200)


class Clients(Resource):
    @jwt_required
    def get(self):
        identity = get_jwt_identity()
        if not is_admin(identity):
            return make_response({'success': False}, 401)

        clients = fetch_clients()
        return make_response({'success': True, 'clients': clients}, 200)
