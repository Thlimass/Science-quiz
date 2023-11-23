from flask import jsonify, request
import uuid
from .. import db
from ..entities.category_entity import Category
from ..entities.question_entity import Question


def create(category_name):
    request_form = request.json
    question_id = str(uuid.uuid4())
    category = Category.query.filter_by(category_name=category_name).first()

    if category:
        question = Question(
            id=question_id,
            category_id=category.id,
            question_text=request_form['question_text'],
            correct_answer=request_form['correct_answer'],
            incorrect_answer=request_form['incorrect_answer']
        )

    db.session.add(question)
    db.session.commit()

    response = Question.query.get(question_id).toDict()
    return jsonify(response)


def list_by_id():
    question = Question.query.get
    return jsonify(question)