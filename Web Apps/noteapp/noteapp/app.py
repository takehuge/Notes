from flask import Flask
from noteapp.views.index import bp as index_bp
from noteapp.views.createdata import bp as createdata_bp

app = Flask(__name__)

# @app.route('/')
# def home():
#     return "Hello WORLD"

app.register_blueprint(index_bp)
app.register_blueprint(createdata_bp)
