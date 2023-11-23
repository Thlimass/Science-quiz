from flask import request

from ..app import app
from ..services.question_services import create


@app.route("/question/<category_name>", methods=['POST'])
def list_create_questions(category_name):
    if request.method == 'POST':
        return create(category_name)
    else:
        return 'Method is Not Allowed'
