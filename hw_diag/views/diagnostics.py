import json

from flask import Blueprint
from flask import render_template
from flask import request
from flask import jsonify


DIAGNOSTICS = Blueprint('DIAGNOSTICS', __name__)


@DIAGNOSTICS.route('/')
def get_diagnostics():
    diagnostics = {}
    try:
        with open('diagnostic_data.json', 'r') as f:
            diagnostics = json.load(f)
    except FileNotFoundError:
        msg = 'Diagnostics have not yet run, please try again in a few minutes'
        diagnostics = {'error': msg}

    if request.args.get('json'):
        return jsonify(diagnostics)

    return render_template('diagnostics_page.html', diagnostics=diagnostics)
