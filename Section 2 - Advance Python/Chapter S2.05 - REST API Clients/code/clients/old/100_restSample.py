import requests

try:
    r = requests.get("http://localhost:5000/tamil")
    print(r)
    print(r.status_code)
    print(r.text)
    print(r.json())
except Exception as e:
    print(e)
