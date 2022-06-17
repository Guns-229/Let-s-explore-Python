import requests

response = requests.get("http://127.0.0.1:5000")
print("Request request:", response.request.headers)
print("*******")
print("Response cookies:", response.cookies)
for cookie in response.cookies.keys():
    print(cookie)