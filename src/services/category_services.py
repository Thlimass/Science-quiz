from flask import request, jsonify, current_app
import uuid

from .. import db
from ..entities.category_entity import Category


def create():
    request_form = request.json
    category_id = str(uuid.uuid4())
    category = Category(
        id=category_id,
        category_name=request_form['category_name'],
    )
    db.session.add(category)
    db.session.commit()

    response = Category.query.get(category_id).toDict()
    return jsonify(response)


def list_all_categories():
    categories = Category.query.all()
    response = []
    for category in categories: response.append(category.toDict())
    return jsonify(response)


def find_category_type(category_name):
    categories = Category.query.filter_by(category_name=category_name)
    response = []
    for category in categories: response.append(category.toDict())
    return jsonify(response)


def delete_category_by_id(category_id):
    category = Category.query.get(category_id)

    if category:
        db.session.delete(category)
        db.session.commit()
        return True
    else:
        return False
