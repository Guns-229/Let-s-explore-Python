import requests

r = requests.get("http://localhost:5000/articles/10")
print(r.status_code)
print(r.headers)
print(r.text)
print(r.cookies)

r = requests.get("http://localhost:5000/articles/5")
print(r.text)
