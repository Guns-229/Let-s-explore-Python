"""."""
import requests

try:
    response = requests.post("http://127.0.0.1:8000/cities/Secunderabad",
                             cookies={"client": "linux"})
    print(response.json())

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
    print("*" * 20)
    print(response.headers["12342"])

except Exception as e:
    print(e)
