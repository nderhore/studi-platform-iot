class Device:

    # Un constructeur
    def __init__(self, id: int, nom: str, marque: str, type: str):
        self._id = id
        self._nom = nom
        self._marque = marque
        self._type = type

    # accesseur et les mutateurs
    @property
    def id(self):
        return self._id

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



