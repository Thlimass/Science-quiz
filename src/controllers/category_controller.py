from flask import request

from ..app import app
from ..services.category_services import create, list_all


@app.route("/category", methods=['GET', 'POST'])
def list_create_categories():
    if request.method == 'GET': return list_all()
    if request.method == 'POST': return create()
    else:
        return 'Method is Not Allowed'
