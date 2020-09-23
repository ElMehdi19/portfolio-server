import os
from flask import request


def authenticate(req_key: str) -> bool:
    api_key = os.environ.get('API_KEY')

    return req_key == api_key


def identity() -> dict:
    user_ip = request.remote_addr

    return {
        'user_ip': user_ip,
        'admin': True
    }


def is_admin(identity) -> bool:
    if not identity:
        return False

    admin = identity.get('admin', False)
    return admin
