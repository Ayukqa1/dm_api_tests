import requests
import json


def put_v1_account_password():
    """
    Change registered user password
    :return:
    """
    url = "http://localhost:5051/v1/account/password"

    payload = {
        "login": "dolore Ut esse aute elit",
        "token": "e1e7929b-3cb6-82d2-2295-22e08a0a3fcf",
        "oldPassword": "ullamco dolore",
        "newPassword": "eu"
    }
    headers = {
        'X-Dm-Auth-Token': 'aliquip cupidatat',
        'X-Dm-Bb-Render-Mode': 'aliquip cupidatat',
        'Content-Type': 'application/json',
        'Accept': 'text/plain'
    }

    response = requests.request(
        method="PUT",
        url=url,
        headers=headers,
        json=payload
    )

    print(response.text)
