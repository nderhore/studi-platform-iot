import json

from flask import Blueprint, request

from models.Device import Device

list_device: list = []

device_ws = Blueprint('deviceWs', __name__, template_folder='templates')


@device_ws.get('/device/')
def get_all_devices():  # put application's code here
    return json.dumps(list_device, default=Device.to_json)


@device_ws.post('/device/')
def create_device():
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        print(request.get_json())
        data: Device = Device.from_json(request.get_json())
        list_device.append(data)
        return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}
    return json.dumps({'success': False}), 200, {'ContentType': 'application/json'}


@device_ws.put('/device/')
def modify_device():
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        data: Device = json.loads(request.data)
        delete_device(data.id_device)
        list_device.append(data)
        return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}
    return json.dumps({'success': False}), 200, {'ContentType': 'application/json'}


@device_ws.delete('/device/<id_device>')
def delete_device(id_device: int):
    print(id_device)
    for device in list_device:
        print(device)
        if int(device.id_device) == int(id_device):
            list_device.remove(device)
            return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}
    return json.dumps({'success': False}), 200, {'ContentType': 'application/json'}
