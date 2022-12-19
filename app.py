from flask import Flask
from flask_jwt_extended import JWTManager

from bdd.database import db
from controller.CategoryWs import category_ws

from controller.DeviceWs import device_ws
from config.config import config
from controller.LoginWs import login_ws

app = Flask(__name__)
app.config.from_object(config)

app.register_blueprint(device_ws)
app.register_blueprint(category_ws)
app.register_blueprint(login_ws)

#Configuration Token JWT
app.config['JWT_SECRET_KEY'] = 'Studi'
app.config['JWT_COOKIE_CSRF_PROTECT'] = True
app.config['JWT_ACCESS_COOKIES_PATH'] = '/api'
app.config['JWT_REFRESH_COOKIES_PATH'] = '/api/tokenRefresh'
app.config['JWT_TOKEN_LOCATION'] = ['cookies']

db.init_app(app)
jwt = JWTManager(app)
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run()
