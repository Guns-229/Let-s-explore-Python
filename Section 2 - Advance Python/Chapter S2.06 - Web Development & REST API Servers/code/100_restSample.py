import requests

resp = requests.get('http://localhost:5000/echo')

if resp.status_code != 200:
    # This means something went wrong.
	print("Error Error Error : ", resp.status_code)
else:
    print(dir(resp))
    print(resp.text)
