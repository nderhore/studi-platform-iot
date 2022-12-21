from bdd.database import db

from utils.PasswordUtils import encode_password


class User(db.Model):
    _username = db.Column('username', db.String, primary_key=True, )
    _password = db.Column('password', db.String(100))

    def __init__(self, username: str, password: str):
        self._username = username
        self._password = encode_password(password)\
            .decode(encoding='utf-8')

    @property
    def username(self):
        return self._username

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self.password = password

    def to_json(self):
        return self.__str__()

    def __iter__(self):
        yield from {
            "username": self._username,
        }.items()

    @staticmethod
    def from_json(json_dct):
        return User(json_dct.get('username'), json_dct.get('password'))
