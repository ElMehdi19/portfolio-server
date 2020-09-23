from flask import make_response, request
from app import app, q
from app.controllers.contact import check_email, send_email, add_message


@app.route('/api/contact', methods=['POST'])
def contact():
    if not all(['email' in request.json, 'message' in request.json]):
        return make_response({'success': False, 'message': 'missing required fields'}, 401)

    if not all([request.json['email'], request.json['message']]):
        return make_response({'success': False, 'message': 'missing required fields'}, 401)

    payload = {'email': request.json['email'],
               'message': request.json['message'],
               'ip_addr': request.remote_addr}
    q.enqueue(add_message, payload)

    if check_email(payload['email']):
        mail_payload = {
            'email': payload.get('email'),
            'message': payload.get('message')}
        q.enqueue(send_email, **mail_payload)

    return make_response({'success': True}, 200)
