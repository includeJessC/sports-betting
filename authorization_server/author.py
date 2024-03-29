import datetime
import os

import jwt
import psycopg2
import requests
from flask import Flask, request, Response, redirect

passkey = os.environ.get("PASS_KEY")
username = os.environ.get("DB_USER")
db_name = os.environ.get("DB_NAME")
us_password = os.environ.get("DB_PASSWORD")
db_host = os.environ.get("DB_HOST")

app = Flask(__name__)
SITE_NAME = 'http://51.250.21.113:8080'


class DataBaseManagemantSystemAuthor:
    def __init__(self):
        self.con = psycopg2.connect(
            database=db_name,
            user=username,
            host=db_host,
            password=us_password,
        )
        self.cur = self.con.cursor()

    def __del__(self):
        self.con.close()

    def check_token(self, username, token):
        cur = self.con.cursor()
        request = f"SELECT * FROM sport_betting.login_token WHERE id = '{str(jwt.encode({'id': username}, passkey, algorithm='HS256'))}' AND token='{token}'"
        cur.execute(request)
        resp = cur.fetchone()
        return resp is not None and datetime.datetime.now() - resp[2] < datetime.timedelta(days=1)


@app.route('/', defaults={'path': ''}, methods=['GET', 'POST'])
@app.route('/<path:path>', methods=['GET', 'POST'])
def proxy(path):
    db = DataBaseManagemantSystemAuthor()
    global SITE_NAME
    print("HOP")
    try:
        body = request.get_json()
    except Exception:
        body = None
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
    print("ALL")
    print(request.method)
    if (token is None or username is None or not db.check_token(username, token)) and path.find(
            'register') == -1 and path.find('login') == -1:
        print("redirect")
        return redirect('http://51.250.21.113:3000/login')
    if request.method == 'GET':
        print(f'{SITE_NAME}/{path}?{request.query_string.decode()}')
        if len(request.query_string.decode()) != 0:
            resp = requests.request(url=f'{SITE_NAME}/{path}?{request.query_string.decode()}', method=request.method, json=body)
        else:
            resp = requests.request(url=f'{SITE_NAME}/{path}', method=request.method, json=body)
        excluded_headers = ['content-encoding', 'content-length', 'transfer-encoding', 'connection']
        headers = [(name, value) for (name, value) in resp.raw.headers.items() if name.lower() not in excluded_headers]
        response = Response(resp.content, resp.status_code, headers)
        return response
    elif request.method == 'POST':
        print(f'{SITE_NAME}/{path}?{request.query_string.decode()}')
        print("THIS IS POST")
        if len(request.query_string.decode()) != 0:
            resp = requests.request(url=f'{SITE_NAME}/{path}?{request.query_string.decode()}', method=request.method, json=body)
        else:
            resp = requests.request(url=f'{SITE_NAME}/{path}', method=request.method, json=body)
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
    print("NOTH")


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=80)
