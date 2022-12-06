import json

from flask import Blueprint, request, render_template
from bdd.database import db
from models.Device import Device

device_ws = Blueprint('deviceWs', __name__, template_folder='templates')


@device_ws.get('/device/')
def get_all_devices():  # put application's code here
    #data: list[Device] = db.session.query(Device).all()
    #return json.dumps(data, default=Device.to_json)
    return render_template('device/all_device.html',
                           title="Flask")


@device_ws.get('/device/<id_device>')
def get_device_by_id(id_device: int):  # put application's code here
    data: Device = db.session.query(Device).filter(Device.id_device == id_device).one()
    return json.dumps(data, default=Device.to_json)


@device_ws.post('/device/')
def create_device():
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        data: Device = Device.from_json(request.get_json())
        db.session.add(data)
        return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}
    return json.dumps({'success': False}), 200, {'ContentType': 'application/json'}


@device_ws.put('/device/')
def modify_device():
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        data: Device = json.loads(request.get_json())

        # Préparation de notre Update, on recupere l'ancien objet
        old_device: Device = db.session.query(Device).filter(Device.id_device == data.id_device).one()

        # Changement de l'ancien device avec le nouveau
        old_device.nom = data.nom
        old_device.type = data.type
        old_device.marque = data.marque
        old_device.category_id = data.category_id
        db.session.commit()

        return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}
    return json.dumps({'success': False}), 200, {'ContentType': 'application/json'}


@device_ws.delete('/device/<id_device>')
def delete_device(id_device: int):
    data: Device = db.session.query(Device).filter(Device.id_device == id_device).one()
    if type(data) is not None:
        db.session.delete(data)
        return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}
    return json.dumps({'success': False}), 200, {'ContentType': 'application/json'}
