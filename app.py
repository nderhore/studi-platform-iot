import json

from flask import Flask, request

from models.Device import Device

app = Flask(__name__)

list_device: list = []


# un get , renvoie une donnée
@app.route('/', methods=['GET'])
def get_all_devices():  # put application's code here
    return json.dumps(list_device)


# le POST il va crée une donnée
@app.route('/', methods=['POST'])
def create_object():
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        data: Device = json.loads(request.data)
        monDevice: Device = Device(data['id'], data['nom'], data['marque'], data['type'])
        list_device.append(monDevice)
        return True
    return False


# le PUT modifie un objet
@app.route('/', methods=['PUT'])
def modify_object():
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        data = json.loads(request.data)
        monDevice: Device = Device(data['id'], data['nom'], data['marque'], data['type'])
        delete_object(monDevice.id)
        list_device.append(monDevice)
        return True
    return False


@app.route('/<id>', methods=['DELETE'])
def delete_object(id: int):
    for device in list_device:
        print(list_device)
        if device.id == id:
            list_device.remove(device)
            break


if __name__ == '__main__':
    app.run()
