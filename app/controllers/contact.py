import re
import json
from urllib.request import urlopen
from contextlib import closing
from typing import Dict
from flask_mail import Message

from app import db, mail, app
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
    country = get_country(payload.get('ip_addr'))
    new_message = Contact(**payload, country=country)
    try:
        db.session.add(new_message)
        db.session.commit()
    except Exception:
        return False
    return True


def check_email(email: str) -> bool:
    pattern = re.compile(r'^.+@[a-z0-9_+.-]+\.\w{2,4}$', re.I)
    matches = pattern.match(email)
    return matches


def send_email(email: str, message: str):
    with app.app_context():
        msg = Message('New client message')
        msg.html = f"""<h3>Client: <b>{email}</b></h3>
        <h4>Message: 
        {message}</h4>
        """
        msg.sender = 'me@iammehdi.io'
        msg.recipients = ['elmehdirami5@gmail.com']
        mail.send(msg)


def fetch_clients():
    clients = Contact.query.all()
    return [client.as_dict for client in clients]
