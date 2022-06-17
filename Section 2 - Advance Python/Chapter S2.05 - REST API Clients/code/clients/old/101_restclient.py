import requests

baseurl = "http://localhost:5000"
resp = requests.get(baseurl + '/echo')
if resp.status_code != 200:
    # This means something went wrong.
    raise ApiError('GET / {}'.format(resp.status_code))
else:
    print(resp.text)

resp = requests.post(baseurl + "/echo")
if resp.status_code != 200:
    # This means something went wrong.
    raise ApiError('POST / {}'.format(resp.status_code))
else:
    print(resp.text)

resp = requests.put(baseurl + "/echo")
if resp.status_code != 200:
    # This means something went wrong.
    raise ApiError('PUT / {}'.format(resp.status_code))
else:
    print(resp.text)

resp = requests.delete(baseurl + "/echo")
if resp.status_code != 200:
    # This means something went wrong.
    raise ApiError('DELETE / {}'.format(resp.status_code))
else:
    print(resp.text)

# for todo_item in resp.json():
#     print('{} {}'.format(todo_item['id'], 
#                          todo_item['summary']))
