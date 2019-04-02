from __future__ import absolute_import

from flask import render_template

from demo import app


@app.route('/hello')
def hello():
    user = {'username': 'Sara Qian'}
    return render_template('hello.html', title=app.config['TITLE'], user=user)





