from flask import request

from ..app import app
from ..services.question_services import create


@app.route("/question", methods=['POST'])
def list_create_questions():
    if request.method == 'POST':
        return create()
    else:
        return 'Method is Not Allowed'
