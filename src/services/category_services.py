from flask import request, jsonify
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


def list_all():
    categories = Category.query.all()
    response = []
    for category in categories: response.append(category.toDict())
    return jsonify(response)
