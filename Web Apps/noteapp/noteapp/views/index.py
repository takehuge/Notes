from flask import Blueprint, render_template
import glob

bp = Blueprint(__name__, __name__, template_folder='templates')

def fetch_data():
    complete_data = []
    datas = glob.glob(
        '/Users/apple/Dropbox/My Programming/Python/Notes/Web Apps/noteapp/noteapp/database/*.pyqum')
    for data in datas:
        with open(data) as dfile:
            complete_data.append(dfile.read())
        dfile.close()
    return complete_data

@bp.route('/')
def show():
    return render_template('index.html', datas=fetch_data())
