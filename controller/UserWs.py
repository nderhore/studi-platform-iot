import json

from flask import Blueprint, request, jsonify
from flask_jwt_extended import unset_jwt_cookies

from bdd.database import db
from models.User import User

user_ws = Blueprint('userWs', __name__, template_folder='templates')


@user_ws.post('/createUser')
def create_user():
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        data: User = User.from_json(request.get_json())
        db.session.add(data)
        db.session.commit()
        return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}
    return json.dumps({'success': False}), 200, {'ContentType': 'application/json'}





