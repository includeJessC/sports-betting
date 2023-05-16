import requests
import pytest

def test_user_register_happy_path():
    response = requests.get("http://192.168.65.4:8080/", data={"id": "newuser", "user_meta": {"name": "A", "surname": "B", "password": "34"}})
    assert response.status_code == 200
