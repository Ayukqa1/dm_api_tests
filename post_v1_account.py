import requests


def post_v1_account():
    """
    Register new user
    :return:
    """
    url = "http://localhost:5051/v1/account"

    payload = {
        "login": "login_8",
        "email": "login8@mail.ru",
        "password": "login_88"
    }
    headers = {
        'X-Dm-Auth-Token': 'aliquip cupidatat',
        'X-Dm-Bb-Render-Mode': 'aliquip cupidatat',
        'Content-Type': 'application/json',
        'Accept': 'text/plain'
    }

    response = requests.request(
        method="POST",
        url=url,
        headers=headers,
        json=payload
    )