from flask import Blueprint, render_template, request, redirect
import random, json
from setuptools.sandbox import _file
from noteapp.views.sources import average

bp = Blueprint(__name__, __name__, template_folder='templates')

def random_string(length=16):
    final_string = ''
    chars = "abcdefghijklmnopqrstuvwxyz0123456789"
    for i in range (0, length):
        final_string += chars[random.randint(0, len(chars)-1)]
    
    return final_string

# print(random_string(16))

@bp.route('/createdata', methods=['POST', 'GET']) #this will appear as the web address
def show():
    if request.method == 'POST':
        if request.form.get('createdata'):
            text = request.form.get('mass')
            text01 = request.form.get('acceleration')
            text02 = average([1,2,3,4,5,6,7,8])
            datad = dict()
            datad['mass'] = text
            datad['acceleration'] = text01
            datad['force'] = float(text) * float(text01)
            datad['average'] = text02
            datad = json.dumps(datad)
            datapath = '/Users/apple/Dropbox/My Programming/Python/Notes/Web Apps/noteapp/noteapp/database/{}.pyqum'.format(
                random_string())
            with open(datapath, 'wb') as _file:
                _file.write(bytes(datad, 'utf8'))
            _file.close()
            return redirect('/')

    return render_template('createdata.html') #this is where it really goes
