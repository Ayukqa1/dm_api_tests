import requests


def post_v1_account_password():
    """
    Reset registered user password
    :return:
    """
    url = "http://localhost:5051/v1/account/password"

    payload = {
        "login": "adipisicing incididunt",
        "email": "occaecat incididunt dolor dolore ipsum"
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

    print(response.text)
