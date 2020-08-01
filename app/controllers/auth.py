import os
from flask import request

def authenticate(req_key: str) -> bool:
    api_key = os.environ.get('API_KEY')

    return req_key == api_key


def identity() -> dict:
    user_ip = request.remote_addr
    user_agent = request.headers.get('User-Agent')

    return { 
        'user_ip' : user_ip,
        'user_agent': user_agent
     }