# -*- coding: utf-8 -*-
from __future__ import absolute_import

from flask import Flask
from flask_apscheduler import APScheduler

import v1


def create_app():
    app = Flask(__name__, static_folder='static')
    app.register_blueprint(
        v1.bp,
        url_prefix='/v1')
    return app

if __name__ == '__main__':
    sheduler = APScheduler()
    app = create_app()
    sheduler.init_app(app)
    sheduler.start()
    app.run(debug=True)