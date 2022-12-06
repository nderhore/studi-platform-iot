import json

from app import db


class Category(db.Model):
    _id_category = db.Column('id_category', db.Integer, primary_key=True,
                             autoincrement=True)
    _libelle = db.Column('libelle', db.String)
    _devices = db.relationship('Device')

    def __init__(self, id_category: int, libelle: str, devices: str):
        self._id_category = id_category
        self._libelle = libelle
        self._devices = devices

    @property
    def libelle(self):
        return self._libelle

    @libelle.setter
    def libelle(self, libelle: str):
        self._libelle = libelle

    @property
    def id_category(self):
        return self._id_category


    def to_json(self):
        return self.__str__()

    def __iter__(self):
        yield from {
            "id_category": self.id_device,
            "libelle": self.nom,
            "devices": self.marque,
        }.items()

    def __str__(self):
        return json.dumps(dict(self), ensure_ascii=False)

    def __repr__(self):
        return self.__str__()

    @staticmethod
    def from_json(json_dct):
        print(json_dct['id_device'])
        id_category: int = int(json_dct['id_category'])
        return Category(id_category,
                        json_dct['libelle'], json_dct['devices'])
