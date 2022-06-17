import requests

try:
    response = requests.get("http://127.0.0.1:5000/cities")
    print(dir(response))
    print(responser.status_code)
    print(responser.headers)
    print(responser.json)
    print(responser.text)
except Exception as e:
    print(e)
