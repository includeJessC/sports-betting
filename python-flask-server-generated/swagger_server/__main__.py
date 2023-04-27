#!/usr/bin/env python3

import connexion

from swagger_server import encoder
from flask_apscheduler import APScheduler

app = connexion.App(__name__, specification_dir='./swagger/')
app.app.json_encoder = encoder.JSONEncoder
app.add_api('swagger.yaml', arguments={'title': 'Sports betting'}, pythonic_params=True)
scheduler = APScheduler()
scheduler.init_app(app)
scheduler.start()

def main():
    app.run(port=8080, debug=True)


if __name__ == '__main__':
    main()
