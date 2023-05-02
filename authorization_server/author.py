import datetime
import os

import cryptocode
import psycopg2
import requests
from flask import Flask, request, Response, redirect

passkey = os.environ.get("PASS_KEY")

app = Flask(__name__)
SITE_NAME = 'http://127.0.0.1:8080'


class DataBaseManagemantSystemAuthor:
    def __init__(self):
        self.con = psycopg2.connect(
            database="postgres",
            user="aabogacheva",
            password="Stack_073A",
        )
        self.cur = self.con.cursor()

    def __del__(self):
        self.con.close()

    def check_token(self, username, token):
        cur = self.con.cursor()
        request = f"SELECT * FROM sport_betting.login_token WHERE id = '{str(cryptocode.encrypt(username, passkey))}' AND token='{token}'"
        cur.execute(request)
        resp = cur.fetchone()
        return resp is not None and datetime.datetime.now() - resp[2] < datetime.timedelta(days=1)


@app.route('/<path:path>', methods=['GET', 'POST', 'DELETE'])
def proxy(path):
    db = DataBaseManagemantSystemAuthor()
    global SITE_NAME
    body = request.get_json()
    token = None
    username = None
    for (name, value) in request.headers:
        print(name)
        print(value)
        if name == 'X-Token':
            token = value
        if name == 'X-Username':
            username = value
    print(request.headers)
    print(f"TOKEN IS {token}")
    print(request.query_string.decode())
    if (token is None or username is None or not db.check_token(username, token)) and path.find('/register') is None:
        return redirect(f'{SITE_NAME}/user_login')
    if request.method == 'GET':
        print(f'{SITE_NAME}/{path}?{request.query_string.decode()}')
        resp = requests.get(f'{SITE_NAME}/{path}?{request.query_string.decode()}', json=body)
        excluded_headers = ['content-encoding', 'content-length', 'transfer-encoding', 'connection']
        headers = [(name, value) for (name, value) in resp.raw.headers.items() if name.lower() not in excluded_headers]
        response = Response(resp.content, resp.status_code, headers)
        return response
    elif request.method == 'POST':
        print(f'{SITE_NAME}/{path}?{request.query_string.decode()}')
        resp = requests.post(f'{SITE_NAME}/{path}?{request.query_string.decode()}', json=body)
        excluded_headers = ['content-encoding', 'content-length', 'transfer-encoding', 'connection']
        headers = [(name, value) for (name, value) in resp.raw.headers.items() if name.lower() not in excluded_headers]
        response = Response(resp.content, resp.status_code, headers)
        return response
    elif request.method == 'DELETE':
        resp = requests.delete(f'{SITE_NAME}/{path}?{request.query_string.decode()}', json=body)
        excluded_headers = ['content-encoding', 'content-length', 'transfer-encoding', 'connection']
        headers = [(name, value) for (name, value) in resp.raw.headers.items() if name.lower() not in excluded_headers]
        response = Response(resp.content, resp.status_code, headers)
        return response


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=80)
