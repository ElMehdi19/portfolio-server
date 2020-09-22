import json
from urllib.request import urlopen
from contextlib import closing
from typing import Dict
from flask import request

from app import db
from app.models.contact import Contact


def get_country(ip: str):

    ip = ip if ip not in ['127.0.0.1', '::1'] else '41.251.158.200'

    base = f'http://www.geoplugin.net/json.gp?ip={ip}'
    try:
        with closing(urlopen(base)) as resp:
            plain = resp.read().decode()
            data = json.loads(plain)
    except Exception:
        return None

    return data.get('geoplugin_countryName', None)


def add_message(payload: Dict[str, str]) -> bool:
    country = get_country(request.remote_addr)
    new_message = Contact(**payload, country=country)
    print(new_message)
    # try:
    #     db.session.add(new_message)
    #     db.session.commit()
    # except Exception:
    #     return False
    return True
