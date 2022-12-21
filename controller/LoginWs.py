import json

from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, create_refresh_token, set_access_cookies, set_refresh_cookies

login_ws = Blueprint('loginWs', __name__, template_folder='templates')


@login_ws.post('/api/')
def authenticator():
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        username = request.json.get('username')

        access_token = create_access_token(username)
        refresh_token = create_refresh_token(username)

        response = jsonify({'success': True})
        set_access_cookies(response, access_token)
        set_refresh_cookies(response, refresh_token)
        return response
    return json.dumps({'success': False}), 200, {'ContentType': 'application/json'}


