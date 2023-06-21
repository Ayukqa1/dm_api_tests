import requests


def post_v1_account_login():
    """
    Authenticate via credentials
    :return:
    """
    url: = "http://localhost:5051/v1/account/login"

    payload = {
        "login": "esse",
        "password": "et minim pariatur",
        "rememberMe": True
    }
    headers = {
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
