from flask import jsonify, request
import uuid
from .. import db
from ..entities.question_entity import Question


def create():
    request_form = request.json
    print(request_form)
    question_id = str(uuid.uuid4())
    question = Question(
        id=question_id,
        category_id="7487fa5a-4796-4c71-a0f1-7d18031fa3e9",
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