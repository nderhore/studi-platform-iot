import json

from app import db


class Device(db.Model):
    _id_device = db.Column('id_device', db.Integer, primary_key=True)
    _nom = db.Column('nom', db.String(100))
    _marque = db.Column('marque', db.String(50))
    _type = db.Column('type', db.String(200))
    _category_id = db.Column('category_id', db.Integer, db.ForeignKey('category.id_category'),
                             nullable=False)

    # Un constructeur
    def __init__(self, id_device: int, nom: str, marque: str, type: str, category_id: int):
        self._id_device = id_device
        self._nom = nom
        self._marque = marque
        self._type = type
        self._category_id = category_id

    # accesseur et les mutateurs
    @property
    def id_device(self):
        return self._id_device

    @property
    def nom(self):
        return self._nom

    @nom.setter
    def nom(self, nom: str):
        self._nom = nom

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, type: str):
        self._type = type

    @property
    def marque(self):
        return self._marque

    @marque.setter
    def marque(self, marque: str):
        self._marque = marque

    def to_json(self):
        return self.__str__()

    def __iter__(self):
        yield from {
            "id_device": self.id_device,
            "nom": self.nom,
            "marque": self.marque,
            "type": self.type,
        }.items()

    def __str__(self):
        return json.dumps(dict(self), ensure_ascii=False)

    def __repr__(self):
        return self.__str__()

    @staticmethod
    def from_json(json_dct):
        print(json_dct['id_device'])
        device_id: int = int(json_dct['id_device'])
        return Device(device_id,
                      json_dct['nom'], json_dct['marque'],
                      json_dct['type'])
