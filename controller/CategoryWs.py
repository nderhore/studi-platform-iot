import json
import pickle

from flask import Blueprint, request
from flask_jwt_extended import jwt_required

from bdd.database import db
from models.Category import Category

category_ws = Blueprint('category', __name__, template_folder='templates')


@category_ws.get('/category/')
@jwt_required()
def get_all_category():  # put application's code here
    data: list[Category] = db.session.query(Category).all()
    return json.dumps(data, default=Category.to_json)


@category_ws.get('/Category/<id_Category>')
@jwt_required()
def get_category_by_id(id_Category: int):  # put application's code here
    data: Category = Category.query.get(id_Category)
    return json.dumps(data, default=Category.to_json)


@category_ws.post('/Category/')
@jwt_required()
def create_category():
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        data: Category = Category.from_json(request.get_data())
        db.session.add(data)
        db.session.commit()
        return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}
    return json.dumps({'success': False}), 200, {'ContentType': 'application/json'}


@category_ws.put('/Category/<id_Category>')
@jwt_required()
def modify_category(id_Category: int):
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        data: Category = json.loads(request.data)

        # Préparation de notre Update, on recupere l'ancien objet
        old_Category = Category.query.get(id_Category)

        # Changement de l'ancien Category avec le nouveau
        if old_Category is not None:
            old_Category.libelle = data.libelle
            db.session.commit()

            return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}
    return json.dumps({'success': False}), 200, {'ContentType': 'application/json'}


@category_ws.delete('/Category/<id_Category>')
@jwt_required()
def delete_category(id_Category: int):
    data = Category.query.get(id_Category)
    if type(data) is not None:
        db.session.delete(data)
        db.session.commit()
        return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}
    return json.dumps({'success': False}), 200, {'ContentType': 'application/json'}
