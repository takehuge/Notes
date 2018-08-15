import json
import time
import random
import itertools
from flask import (
    Flask, Blueprint, flash, g, redirect, render_template, request, url_for, Response,
    stream_with_context
)
from werkzeug.exceptions import abort

from flaskr import stream_template
from flaskr.auth import login_required
from flaskr.db import get_db
from pathlib import Path
import numpy as np

from wtforms import Form, FloatField, validators

class InputForm(Form):
    r = FloatField(validators=[validators.InputRequired()])

bp = Blueprint('vocab', __name__)
datafolder = "/Users/apple/Dropbox/My Programming/Python/Notes/Web Apps/flask-master/examples/tutorial/instance"


@bp.route('/vocaba', methods=['POST', 'GET'])
def vocaba():

    if request.headers.get('accept') == 'text/event-stream':
        def events():
            for i, c in enumerate(itertools.cycle('\|/-')):
                yield "data: %s %d\n\n" % (c, i)
                time.sleep(.1)  # an artificial delay
                
        return Response(events(), content_type='text/event-stream')

    return redirect(url_for('vocab.vocaba'))
