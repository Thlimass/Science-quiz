from flask import request, jsonify

from ..app import app
from ..services.category_services import \
    create, \
    list_all_categories,\
    find_category_type, \
    delete_category_by_id


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


@app.route("/category/<category_id>", methods=['DELETE'])
def delete_category(category_id):
    deleted = delete_category_by_id(category_id)

    if deleted:
        return jsonify({'message': 'Category deleted successfully'}), 200
    else:
        return jsonify({'message': 'Category not found'}), 404
