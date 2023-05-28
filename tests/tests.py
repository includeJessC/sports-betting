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
    assert response.json() == {"id": "lol", "user_meta": {"name": "123", "surname": "123", "password": "123"}}


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


def test_competitions_get():
    response = requests.get("http://192.168.65.4:8080/competitions?id=lol")
    assert response.status_code == 200
    del response.json()['competitions'][0]['matches'][0]['start_time']
    assert response.json() == {
        "competitions": [{"name": "1", "id": "1", "is_active": True, "created_by": "lol", "matches": [
            {"first_team_name": "1", "second_team_name": "2", "id": "1", "name": "1", "is_active": False}]}]}


def test_competition_info_get():
    response = requests.get("http://192.168.65.4:8080/competitions_info?id=lol&competition_id=1")
    assert response.status_code == 200
    del response.json()['matches'][0]['start_time']
    assert response.json() == {"name": "1", "id": "1", "is_active": True, "created_by": "lol", "matches": [
        {"first_team_name": "1", "second_team_name": "2", "id": "1", "name": "1", "is_active": False}]}


def test_competition_info_post():
    response = requests.post("http://192.168.65.4:8080/competitions_info?id=kek&competition_id=1")
    assert response.status_code == 200
    del response.json()['matches'][0]['start_time']
    assert response.json() == {"name": "1", "id": "1", "is_active": True, "created_by": "lol", "matches": [
        {"first_team_name": "1", "second_team_name": "2", "id": "1", "name": "1", "is_active": False}]}


def test_match_info_get():
    response = requests.get("http://192.168.65.4:8080/match_info?id=lol&competition_id=1&match_id=1")
    assert response.status_code == 200
    assert response.json() == {"first_team_name": "1", "second_team_name": "2", "id": "1", "name": "1",
                               "is_active": False}


def test_create_competition_and_match():
    response = requests.post("http://192.168.65.4:8080/create/competition?id=lol", json={"name": "2"})
    assert response.status_code == 200
    del response.json()['matches'][0]['start_time']
    c_id = response.json()['id']
    del response.json()['id']
    assert response.json() == {"name": "2", "is_active": True, "created_by": "lol", "matches": []}
    response = requests.post(f"http://192.168.65.4:8080/create/match?id=lol&competition_id={c_id}",
                             json={"first_team_name": "1", "second_team_name": "2", "special_bets": ["1", "2"]})
    assert response.status_code == 200
    response = requests.get(f"http://192.168.65.4:8080/competitions_info?id=lol&competition_id={c_id}")
    assert response.status_code == 200
    assert len(response.json()['matches']) != 0


def test_competitions_get_bad_path():
    response = requests.get("http://192.168.65.4:8080/competitions?id=lol1")
    assert response.status_code == 404


def test_competition_info_get_bad_path():
    response = requests.get("http://192.168.65.4:8080/competitions_info?id=lol&competition_id=12")
    assert response.status_code == 404


def test_competition_info_post_bad_path():
    response = requests.post("http://192.168.65.4:8080/competitions_info?id=kek&competition_id=12")
    assert response.status_code == 404


def test_match_info_get_bad_path():
    response = requests.get("http://192.168.65.4:8080/match_info?id=lol&competition_id=1&match_id=12")
    assert response.status_code == 404
