import requests

response = requests.post("http://127.0.0.1:5000/quarks",
						 json={"name":"top", "charge":"+2/3"})
print(response.json())
