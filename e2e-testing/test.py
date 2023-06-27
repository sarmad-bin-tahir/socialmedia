import requests
import json

API_URL = "http://localhost:8000"


def perform_login():
    url = f"{API_URL}/api/login/"
    data = {
        "email": "sarmad.tahir+01@gmail.com",
        "password": "Bella112233"
    }
    response = requests.post(url, data=data, )

    return response


def create_post():
    url = f"{API_URL}/api/posts/"
    payload = {
        "text": "My name is sarmad bin tahir",
    }
    response = perform_login()
    data = json.loads(response.text)
    headers = {
        "Authorization": f"jwt {data.get('token')}"
    }
    return requests.post(url, data=payload, headers=headers)


def test_register():
    url = f"{API_URL}/api/register/"
    data = {
        "email": "sarmad.tahir+01@gmail.com",
        "password1": "Bella112233",
        "password2": "Bella112233"
    }
    response = requests.post(url, data=data)
    assert response.status_code == 200


def test_valid_login():
    response = perform_login()
    assert response.status_code == 200


def test_invalid_login():
    url = f"{API_URL}/api/login/"
    data = {
        "email": "sarmad.tahir+01@gmail.com",
        "password": "Bella11223344"
    }
    response = requests.post(url, data=data)
    assert response.status_code == 400


def test_create_post():
    response = create_post()
    assert response.status_code == 201


def test_read_post():
    response = create_post()
    post_data = json.loads(response.text)
    POST_ID = post_data.get('id')
    url = f"{API_URL}/api/posts/{POST_ID}/"
    response = perform_login()
    data = json.loads(response.text)
    headers = {
        "Authorization": f"jwt {data.get('token')}"
    }
    response = requests.get(url, headers=headers)
    assert response.status_code == 200


def test_update_post():
    response = create_post()
    post_data = json.loads(response.text)
    POST_ID = post_data.get('id')
    url = f"{API_URL}/api/posts/{POST_ID}/"
    payload = {
        "text": "My name is sarmad bin tahir updated",
    }
    response = perform_login()
    data = json.loads(response.text)
    headers = {
        "Authorization": f"jwt {data.get('token')}"
    }
    response = requests.put(url, data=payload, headers=headers)
    assert response.status_code == 200


def test_delete_post():
    response = create_post()
    post_data = json.loads(response.text)
    POST_ID = post_data.get('id')
    url = f"{API_URL}/api/posts/{POST_ID}/"
    response = perform_login()
    data = json.loads(response.text)
    headers = {
        "Authorization": f"jwt {data.get('token')}"
    }
    response = requests.delete(url, headers=headers)
    assert response.status_code == 204


def test_get_user_details():
    url = f"{API_URL}/api/get-user-details"
    response = perform_login()
    data = json.loads(response.text)
    headers = {
        "Authorization": f"jwt {data.get('token')}"
    }
    response = requests.get(url, headers=headers)
    assert response.status_code == 200


def test_like_unlike_post():
    response = create_post()
    post_data = json.loads(response.text)
    POST_ID = post_data.get('id')
    url = f"{API_URL}/api/like-unlike/"
    response = perform_login()
    data = json.loads(response.text)
    headers = {
        "Authorization": f"jwt {data.get('token')}"
    }
    payload = {
        "post_id": POST_ID,
        "reaction": True
    }
    response = requests.put(url, data=payload, headers=headers)
    assert response.status_code == 200
