import json, time, random, itertools
from flask import (
    Flask, Blueprint, flash, g, redirect, render_template, request, url_for, \
    Response, stream_with_context, jsonify
)
from werkzeug.exceptions import abort

from flaskr import stream_template
from flaskr.auth import login_required
from flaskr.db import get_db
from pathlib import Path
import numpy as np

# app = Flask(__name__)

bp = Blueprint('blog', __name__)
datafolder = "/Users/apple/Dropbox/My Programming/Python/Notes/Web Apps/flask-master/examples/tutorial/instance"


@bp.route('/')
def index():
    """Show all the posts, most recent first."""
    db = get_db()
    posts = db.execute(
        'SELECT p.id, title, body, created, author_id, username'
        ' FROM post p JOIN user u ON p.author_id = u.id'
        ' ORDER BY created DESC'
    ).fetchall()
    return render_template('blog/index.html', posts=posts)


def get_post(id, check_author=True):
    """Get a post and its author by id.

    Checks that the id exists and optionally that the current user is
    the author.

    :param id: id of post to get
    :param check_author: require the current user to be the author
    :return: the post with author information
    :raise 404: if a post with the given id doesn't exist
    :raise 403: if the current user isn't the author
    """
    post = get_db().execute(
        'SELECT p.id, title, body, created, author_id, username'
        ' FROM post p JOIN user u ON p.author_id = u.id'
        ' WHERE p.id = ?',
        (id,)
    ).fetchone()

    if post is None:
        abort(404, "Post id {0} doesn't exist.".format(id))

    if check_author and post['author_id'] != g.user['id']:
        abort(403)

    return post


@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    """Create a new post for the current user."""
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'INSERT INTO post (title, body, author_id)'
                ' VALUES (?, ?, ?)',
                (title, body, g.user['id'])
            )
            db.commit()
            return redirect(url_for('blog.index'))

    return render_template('blog/create.html')


@bp.route('/<int:id>/update', methods=('GET', 'POST'))
@login_required
def update(id):
    """Update a post if the current user is the author."""
    post = get_post(id)

    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'UPDATE post SET title = ?, body = ? WHERE id = ?',
                (title, body, id)
            )
            db.commit()
            return redirect(url_for('blog.index'))

    return render_template('blog/update.html', post=post)


@bp.route('/<int:id>/delete', methods=('POST',))
@login_required
def delete(id):
    """Delete a post.

    Ensures that the post exists and that the logged in user is the
    author of the post.
    """
    get_post(id)
    db = get_db()
    db.execute('DELETE FROM post WHERE id = ?', (id,))
    db.commit()
    return redirect(url_for('blog.index'))

# Setting shared variables
x = np.arange(0, 12, 0.1)
lx = len(x)
yr = np.random.rand(lx) - np.random.rand(lx)
yr2 = np.random.rand(lx) - np.random.rand(lx)
ys = np.sin(3*x)
yc = np.cos(3 * x)

@bp.route('/experimentss', methods=['POST', 'GET']) #how it appears in the address bar
def experimen():
    tojsondata = [0, 10, 5, 2, 20, 30, 64]
    openpath = Path(datafolder) / "data.star"
    if not Path.exists(openpath):
        txt_loaded = {}
    else:
        with open(openpath) as txt_file: # reading data
            txt_loaded = json.load(txt_file)

    if request.method == 'POST':
        
        if request.form.get('measure'):
            data = {}
            data['x'] = [x for x in x]
            data['y1'] = [y for y in abs(yr) - np.random.rand(lx)]
            data['y2'] = [y for y in abs(yr2) - np.random.rand(lx)]
            with open(openpath, 'w') as _file: # writing data
                json.dump(data, _file)

    # RENDER to literal HTML file:
    return render_template('blog/experiments.html', dat=txt_loaded, tojsondata=tojsondata)

# Streaming

@bp.route('/analysis_process')
def analysis_process():
	try:
		stat = request.args.get('stat', 0, type=str)
		if stat.lower() == 'pause':
			return jsonify(result='PAUSED')
		else:
			return jsonify(result='HERE WE GO, ' + str(stat))
	except Exception as e:
		return str(e)

@bp.route('/analysis', methods=['POST', 'GET'])
def analysis(): # one of the method called by base/layout
    # a = input("before post:")
    state = 'NOBODY'
    datagen, data = {}, {}
    data['x'] = [x for x in x]
    data['y'] = [y for y in yr]
    # if request.method == 'GET':
    #     a = input("after post:")
    if request.form.get('analysis'):
        def gen(): 
            i = 1
            while True:
                data['y'][1:lx] = data['y'][0:lx - 1]
                data['y'][0] = random.uniform(-1, 1)
                yield i, data
                time.sleep(0.03)
                i += 1
            
        datagen = gen()

    if request.form.get('res'):
        def gena():
            i = 1
            while True:
                stat = request.args.get('stat', 0, type=str)
                for j in range(lx):
                    data['y'][j] = np.sin(3 * data['x'][j] + (i * np.pi / 100)) * int(stat)
                yield i, data
                time.sleep(0.03)
                i += 1

        datagen = gena()

    # return Response(gen()) #Blank page with just data print
    # return Response(stream_with_context(gen())) #SAME AS ABOVE
    # return Response(stream_template('blog/analysis.html', data=rows)) #BLANK!!! WHY???
    return Response(stream_with_context(stream_template('blog/analysis.html', data=datagen, people=state)))
    # return render_template('blog/analysis.html', data=data) #NORMAL Display, No streaming!

@bp.route('/calibration', methods=['POST', 'GET'])
def calibration():  # one of the method called by base/layout
    datad, data, chartop, chartopt = {}, {}, "", ""
    data['x'] = [x for x in x]
    data['yS'] = [y for y in ys]
    data['yR'] = [y for y in yr]
    data['yC'] = [y for y in yc]
    data['xud'], data['yup'], data['ydn'] = [], [], []
    # chartopt = request.form.get("chartopt")
    if 'run' in request.form:
        chartopt = request.form.get("chartopt") # selection picked for chart#1
        chartop = request.form.get("chartop") # selection picked for chart#2
        def gen():
            for i in range(lx):
                data['xud'].append(data['x'][i])
                    
                if str(chartopt) == "sinusoid":
                    data['yup'].append(data['yS'][i])
                if str(chartopt) == "random":
                    data['yup'].append(data['yR'][i])
                if str(chartopt) == "cosine":
                    data['yup'].append(data['yC'][i])       
                
                if str(chartop) == "0":
                    data['ydn'].append(data['yS'][i])
                if str(chartop) == "1":
                    data['ydn'].append(data['yR'][i])
                if str(chartop) == "2":
                    data['ydn'].append(data['yC'][i])

                yield [data['xud'], data['yup'], data['ydn']]
                time.sleep(0.03)
        datad = gen()

    return Response(stream_with_context(stream_template('blog/calibration.html', datad=datad, chartopt=str(chartopt), chartop=str(chartop))))
    # return render_template('blog/analysis.html', data=data) #NORMAL Display, No streaming!

@bp.route('/scatter', methods=['POST', 'GET'])
def scatter():
    datad = []
    def gen():
        # datad = [] # only if += is used
        for i in range(371):
            a = np.sin(i * np.pi / 25 + 0.25 * np.pi) + 0.07 * random.uniform(-1, 1)
            b = np.cos(i * np.pi / 25 + 0.25 * np.pi) + 0.13 * random.uniform(-1, 1)
            book = dict(x=a, y=b)
            datad.append(book)
            # datad += [book] # equivalent to append but need to declare it inside def
            yield i, datad
            time.sleep(0.0001)
    data = gen()
      
    return Response(stream_with_context(stream_template('blog/scatter.html', data=data)))
