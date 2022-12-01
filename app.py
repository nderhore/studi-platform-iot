import json

from flask import Flask, request

from models.Device import Device

app = Flask(__name__)

list_device: list = []


# un get , renvoie une donnée
@app.route('/', methods=['GET'])
def get_all_devices():  # put application's code here
    return json.dumps(list_device,default= Device.to_json)


# le POST il va crée une donnée
@app.route('/', methods=['POST'])
def create_object():
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        print(request.get_json())
        data: Device = Device.from_json(request.get_json())
        list_device.append(data)
        return json.dumps({'success':True}), 200, {'ContentType':'application/json'}
    return json.dumps({'success': False}), 200, {'ContentType': 'application/json'}


# le PUT modifie un objet
@app.route('/', methods=['PUT'])
def modify_object():
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        data : Device = json.loads(request.data)
        delete_object(data.id_device)
        list_device.append(data)
        return json.dumps({'success':True}), 200, {'ContentType':'application/json'}
    return json.dumps({'success': False}), 200, {'ContentType': 'application/json'}


@app.route('/<id_device>', methods=['DELETE'])
def delete_object(id_device: int):
    print(id_device)
    for device in list_device:
        print(device)
        if int(device.id_device) == int(id_device):
            list_device.remove(device)
            return json.dumps({'success':True}), 200, {'ContentType':'application/json'}
    return json.dumps({'success': False}), 200, {'ContentType': 'application/json'}

if __name__ == '__main__':
    app.run()
