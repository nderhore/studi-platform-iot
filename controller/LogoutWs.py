from flask import Blueprint, request, jsonify
from flask_jwt_extended import unset_jwt_cookies

logout_ws = Blueprint('logoutWs', __name__, template_folder='templates')


@logout_ws.post('/logout')
def logout():
    response = jsonify({'success': True,
                        'message': 'vous êtes bien deconnecte'})
    unset_jwt_cookies(response)
    return response
