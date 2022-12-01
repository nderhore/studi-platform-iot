from flask import Flask
from bdd.database import db

from controller.DeviceWs import device_ws
from config.config import config


app = Flask(__name__)
app.config.from_object(config)

app.register_blueprint(device_ws)
db.init_app(app)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run()
