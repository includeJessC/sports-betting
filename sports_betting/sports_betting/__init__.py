# -*- coding: utf-8 -*-
from __future__ import absolute_import

from flask import Flask
from flask_apscheduler import APScheduler

from v1 import bp
from v1.db_manager import DataBaseManagemantSystem


def create_app():
    app = Flask(__name__, static_folder='static')
    app.register_blueprint(
        bp)
    return app

if __name__ == '__main__':
    sheduler = APScheduler()
    app = create_app()
    sheduler.init_app(app)
    sheduler.start()
    app.run(debug=True)