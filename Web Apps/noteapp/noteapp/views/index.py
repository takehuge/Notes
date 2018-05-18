from flask import Blueprint, render_template
# from jinja2 import TemplateNotFound

bp = Blueprint(__name__, __name__, template_folder='templates')

@bp.route('/')
def show():
    return render_template('layout.html')
