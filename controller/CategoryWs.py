import json

from flask import Blueprint

from models.Category import Category

category_ws = Blueprint('category', __name__, template_folder='templates')
list_category: list = []


@category_ws.get('/category/')
def get_all_devices():  # put application's code here
    return json.dumps(list_category, default=Category.to_json)