import requests


def get_v1_account():
    """
    Get current user
    :return:
    """
    url = "http://localhost:5051/v1/account"

    headers = {
        'X-Dm-Auth-Token': 'aliquip cupidatat',
        'X-Dm-Bb-Render-Mode': 'aliquip cupidatat',
        'Accept': 'text/plain'
    }

    response = requests.request(
        method="GET",
        url=url,
        headers=headers
    )

    print(response.text)
