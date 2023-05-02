#!/usr/bin/env python3

import connexion

from swagger_server import encoder
from apscheduler.schedulers.background import BackgroundScheduler

app = connexion.App(__name__, specification_dir='./swagger/')
app.app.json_encoder = encoder.JSONEncoder
app.app.config['JSON_AS_ASCII'] = False
app.add_api('swagger.yaml', arguments={'title': 'Sports betting'}, pythonic_params=True)
scheduler = BackgroundScheduler()
scheduler.start()

def main():
    app.run(port=8080, debug=True)


if __name__ == '__main__':
    main()
