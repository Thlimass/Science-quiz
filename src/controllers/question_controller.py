from flask import request, jsonify

from ..app import app
from ..services.question_services import create, delete_question_by_id


@app.route("/question/<category_name>", methods=['POST'])
def list_create_questions(category_name):
    if request.method == 'POST':
        return create(category_name)
    else:
        return 'Method is Not Allowed'


@app.route("/question/<question_id>", methods=['DELETE'])
def delete_question(question_id):
    deleted = delete_question_by_id(question_id)

    if deleted:
        return jsonify({'message': 'Question deleted successfully'}), 200
    else:
        return jsonify({'message': 'Question not found'}), 404
