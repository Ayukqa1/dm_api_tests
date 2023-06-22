import requests


def put_v1_account_token():
    """
    Activate registered user
    :return:
    """
    token = "12345"
    url = f"http://localhost:5051/v1/account/{token}"

    headers = {
        'X-Dm-Auth-Token': 'aliquip cupidatat',
        'X-Dm-Bb-Render-Mode': 'aliquip cupidatat',
        'Accept': 'text/plain'
    }

    response = requests.request(
        method="PUT",
        url=url,
        headers=headers
    )

    print(response.text)
