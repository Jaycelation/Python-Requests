from requests import Request, Session
import requests
r = requests.get('https://qldt.ptit.edu.vn/#/')
print(r.headers)
print(r.cookies)
print(Session())