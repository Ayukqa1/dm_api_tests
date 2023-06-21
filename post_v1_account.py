import requests
import json

url = "http://localhost:5051/v1/account"

payload = json.dumps({
  "login": "login_8",
  "email": "login8@mail.ru",
  "password": "login_88"
})
headers = {
  'X-Dm-Auth-Token': 'aliquip cupidatat',
  'X-Dm-Bb-Render-Mode': 'aliquip cupidatat',
  'Content-Type': 'application/json',
  'Accept': 'text/plain'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
