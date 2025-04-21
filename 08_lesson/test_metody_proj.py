import requests

base_url = "https://yougile.com"

my_headers = {
    'Authorization': f'Bearer {my_token}'}

def test_create_proj():
    project_body = {
        'title': 'Проект №1'
    }
    resp = requests.post(base_url + '/api-v2/projects', json=project_body, headers = my_headers)
    assert resp.json()["id"] is not None
    assert resp.status_code == 201

def test_create_proj_negative():
    project_body = {
        'title': ''
    }
    resp = requests.post(base_url + '/api-v2/projects', json=project_body, headers = my_headers)
    assert resp.json()["message"][0] == 'title should not be empty'
    assert resp.status_code == 400

def test_update_proj():
    project_body = {
        'title': 'Проект №5'
    }
    resp = requests.post(base_url + '/api-v2/projects', json=project_body, headers=my_headers)
    project_id =  resp.json()["id"]
    project_body_update = {
        'title': 'Проект №5new'
    }
    resp_update = requests.put(base_url + f'/api-v2/projects/{project_id}', json=project_body_update, headers=my_headers)
    assert resp_update.json()["id"] is not None
    assert resp_update.status_code == 200

def test_update_proj_negative():
    project_body = {
        'title': 'Проект №5'
    }
    resp = requests.post(base_url + '/api-v2/projects', json=project_body, headers =my_headers)
    project_id =  resp.json()["id"]
    project_body_update = {
        'title': 'Проект №5new'
    }
    resp_update = requests.put(base_url + f'/api-v2/projects/{project_id}', json=project_body_update)
    assert resp_update.json()["message"][0] == 'U'
    assert resp_update.status_code == 401

def test_receive_proj():
    project_body = {
        'title': 'Новый проект'
    }
    resp = requests.post(base_url + '/api-v2/projects', json=project_body, headers=my_headers)
    project_id =  resp.json()["id"]

    resp_receive = requests.get(base_url + f'/api-v2/projects/{project_id}', json=project_body, headers=my_headers)
    assert resp_receive.json()["title"] == 'Новый проект'
    assert resp_receive.status_code == 200

def test_receive_proj_negative():
    project_body = {
        'title': ''
    }
    resp = requests.post(base_url + '/api-v2/projects', json=project_body, headers=my_headers)
    project_id =  resp.json()["id"]

    resp_receive = requests.get(base_url + f'/api-v2/projects/{project_id}', json=project_body)
    assert resp_receive.json()["message"][0] == 'Проект не найден'
    assert resp_receive.status_code == 404