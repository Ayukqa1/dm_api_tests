import requests
import json


def put_v1_account_email():
    """
    Change registered user email
    :return:
    """
    url = "http://localhost:5051/v1/account/email"

    payload = {
        "login": "inci",
        "password": "id irure esse",
        "email": "offici"
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
