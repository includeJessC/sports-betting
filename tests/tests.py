import requests


def test_user_register_happy_path():
    response = requests.post("http://192.168.65.4:8080/user_register",
                             json={"id": "newuser", "user_meta": {"name": "A", "surname": "B", "password": "34"}})
    print(response.text)
    assert response.status_code == 200


def test_user_register_path_repeat():
    response = requests.post("http://192.168.65.4:8080/user_register",
                             json={"id": "lol", "user_meta": {"name": "A", "surname": "B", "password": "34"}})
    print(response.text)
    assert response.status_code == 400


def test_user_login_happy_path():
    response = requests.post("http://192.168.65.4:8080/user_login", json={"id": "lol", "password": "123"})
    print(response.text)
    assert response.status_code == 200


def test_get_user_info():
    response = requests.get("http://192.168.65.4:8080/user?id=lol")
    print(response.text)
    assert response.status_code == 200


def test_get_user_info_bad_path():
    response = requests.get("http://192.168.65.4:8080/user?id=lol12")
    print(response.text)
    assert response.status_code == 404


def test_user_login_wrong_password():
    response = requests.post("http://192.168.65.4:8080/user_login", json={"id": "lol", "password": "1234"})
    print(response.text)
    assert response.status_code == 400


def test_user_register_approve_happy_path():
    response = requests.post("http://192.168.65.4:8080/user_register_approve",
                             json={"id": "pok", "secret_code": "value"})
    print(response.text)
    assert response.status_code == 200


def test_user_register_approve_bad_path():
    response = requests.post("http://192.168.65.4:8080/user_register_approve",
                             json={"id": "lol", "secret_code": "value"})
    print(response.text)
    assert response.status_code == 400


def test_proxy_non_authrorized():
    response = requests.get("http://192.168.65.4:80/competitions?id=lol")
    print(response.text)
    assert response.status_code != 200


def test_proxy_authrorized():
    response = requests.get("http://192.168.65.4:80/competitions?id=lol",
                            headers={'X-Token': 'qw', 'X-Username': 'lol'})
    print(response.text)
    assert response.status_code == 200
