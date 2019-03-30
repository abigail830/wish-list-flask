from __future__ import absolute_import

from demo import app


@app.route('/health')
def health():
    return "UP"




