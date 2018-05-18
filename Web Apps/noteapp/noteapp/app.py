from flask import Flask
from noteapp.views.index import bp as index_bp
# from views.index import bp as index_bp

app = Flask(__name__)

# @app.route('/')
# def home():
#     return "Hello WORLD"

app.register_blueprint(index_bp)
