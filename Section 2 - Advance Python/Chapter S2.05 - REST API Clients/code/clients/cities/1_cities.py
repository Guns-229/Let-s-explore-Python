import requests

try:
    response = requests.get("http://127.0.0.1:5000/cities")
    print(dir(response))
    print("*" * 20)
    print(response.status_code)
    print("*" * 20)
    print(response.headers)
    print("*" * 20)
    print(response.json())
    print("*" * 20)
    print(response.text)
    print("*" * 20)
    print(response.cookies)
except Exception as e:
    print(e)
