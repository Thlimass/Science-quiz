from flask import request

from ..app import app
from ..services.category_services import create, list_all_categories, find_category_type


@app.route("/category", methods=['GET', 'POST'])
def list_create_categories():
    if request.method == 'GET':
        return list_all_categories()
    if request.method == 'POST':
        return create()
    else:
        return 'Method is Not Allowed'


@app.route("/category/<category_name>", methods=['GET'])
def category_by_name(category_name):
    if request.method == 'GET':
        return find_category_type(category_name)
    else:
        return 'Method is Not Allowed'
