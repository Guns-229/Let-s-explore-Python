import requests

r = requests.get("http://localhost:5000/test/articles")
print(r.status_code)
print(r.headers)
print(r.text)
print(r.cookies)
