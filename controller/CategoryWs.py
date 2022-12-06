import json

from flask import Blueprint, request

from bdd.database import db
from models.Category import Category

category_ws = Blueprint('category', __name__, template_folder='templates')
list_category: list = []


@category_ws.get('/category/')
def get_all_category():  # put application's code here
    data: list[Category] = db.session.query(Category).all()
    return json.dumps(data, default=Category.to_json)


@category_ws.get('/Category/<id_Category>')
def get_category_by_id(id_Category: int):  # put application's code here
    data: Category = db.session.query(Category).filter(Category.id_Category == id_Category).one()
    return json.dumps(data, default=Category.to_json)


@category_ws.post('/Category/')
def create_category():
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        data: Category = Category.from_json(request.get_json())
        db.session.add(data)
        return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}
    return json.dumps({'success': False}), 200, {'ContentType': 'application/json'}


@category_ws.put('/Category/<id_Category>')
def modify_category():
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        data: Category = json.loads(request.data)

        # Préparation de notre Update, on recupere l'ancien objet
        old_Category: Category = db.session \
            .query(Category).filter(Category.id_Category == data.id_Category).one()

        # Changement de l'ancien Category avec le nouveau
        old_Category.libelle = data.libelle
        db.session.commit()

        return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}
    return json.dumps({'success': False}), 200, {'ContentType': 'application/json'}


@category_ws.delete('/Category/<id_Category>')
def delete_category(id_Category: int):
    data: Category = db.session.query(Category).filter(Category.id_Category == id_Category).one()
    if type(data) is not None:
        db.session.delete(data)
        return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}
    return json.dumps({'success': False}), 200, {'ContentType': 'application/json'}
