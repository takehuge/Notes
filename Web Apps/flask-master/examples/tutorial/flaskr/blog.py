import json, time, random, itertools
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

app = Flask(__name__)

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


@bp.route('/experimentss', methods=['POST', 'GET']) #how it appears in the address bar
def experimen():
    tojsondata = [0, 10, 5, 2, 20, 30, 64]
    openpath = Path(datafolder) / "data.star"
    if not openpath.exists():
        txt_loaded = {}
    else:
        with open(openpath) as txt_file: # reading data
            txt_loaded = json.load(txt_file)

    if request.method == 'POST':
        
        if request.form.get('measure'):
            data = {}
            x = np.arange(0,12,0.5)
            data['x'] = [x for x in x]
            y = np.random.rand(len(data['x']))
            data['y1'] = [y for y in y]
            y = np.random.rand(len(data['x']))
            data['y2'] = [y for y in y]
            with open(openpath, 'w') as _file: # writing data
                json.dump(data, _file)

    return render_template('blog/experiments.html', dat=txt_loaded, tojsondata=tojsondata)

# Streaming

@bp.route('/analysis', methods=['POST', 'GET'])
def analysis(): # one of the method called by base/layout
    data = {}
    x = np.arange(0, 12, 0.5)
    data['x'] = [x for x in x]
    y = np.random.rand(len(data['x']))
    data['y'] = [y for y in y]

    # if request.method == 'POST':
        
    #     if request.form.get('analysis'):
    #         for i in range(5):
    #             y[1:len(y)] = y[0:len(y)-1]
    #             y[0] = random.uniform(0, 1)
    #             data['y'] = [y for y in y]
    #             time.sleep(0.7)

    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    def gen():                                                                                                                                                                                
        for item in data:                                                                                                                                                                          
            yield str(item)                                                                                                                                                                        
            time.sleep(0.37) 

    rows = gen()
    
    # return redirect('/analysis')
    # return Response(gen())
    return Response(stream_with_context(stream_template('blog/analysis.html', data=rows)))
    # return render_template('blog/analysis.html', data=data) #link to literal html file
