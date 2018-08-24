import json
import time
import random
import itertools
import requests
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


@bp.route('/vocab')
def show():

    return render_template("vocab/vocaba.html")


@bp.route('/vocab/stepform')
def stepform():
    x = 0
    y = 0
    def plus():
        print("PLUS INITIATED!")
    def minus():
        print("MINUS INITIATED!")
    return render_template("vocab/stepform.html", x=x, y=y, plus=plus, minus=minus)



