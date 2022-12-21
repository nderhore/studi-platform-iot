import json

from flask import Blueprint, request, render_template
from flask_jwt_extended import jwt_required

from bdd.database import db
from models.Device import Device

device_ws = Blueprint('deviceWs', __name__, template_folder='templates')


@device_ws.get('/device/')
@jwt_required()
def get_all_devices():  # put application's code here
    data: list[Device] = db.session.query(Device).all()
    return json.dumps(data, default=Device.to_json)


@device_ws.get('/device/<id_device>')
@jwt_required()
def get_device_by_id(id_device: int):  # put application's code here
    data: Device = Device.query.get(id_device)
    return json.dumps(data, default=Device.to_json)


@device_ws.post('/device/')
@jwt_required()
def create_device():
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        data: Device = Device.from_json(request.get_json())
        db.session.add(data)
        db.session.commit()
        return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}
    return json.dumps({'success': False}), 200, {'ContentType': 'application/json'}


@device_ws.put('/device/<id_device>')
@jwt_required()
def modify_device(id_device: int):
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        data: Device = Device.from_json(request.get_json())
        data_old = Device.query.get(id_device)
        if data_old is not None:
            data_old.nom = data.nom
            data_old.marque = data.marque
            data_old.type = data.type
            data_old.type = data.category_id
            db.session.commit()
        else:
            data.id_device = None
            db.session.add(data)
            db.session.commit()
        return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}
    return json.dumps({'success': False}), 200, {'ContentType': 'application/json'}


@device_ws.delete('/device/<id_device>')
@jwt_required()
def delete_device(id_device: int):
    data = Device.query.get(id_device)
    if type(data) is not None:
        db.session.delete(data)
        db.session.commit()
        return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}
    return json.dumps({'success': False}), 200, {'ContentType': 'application/json'}
