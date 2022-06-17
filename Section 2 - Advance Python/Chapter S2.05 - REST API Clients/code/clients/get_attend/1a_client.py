import requests

baseurl = "http://127.0.0.1:5000/"
task =  {'user' : 'rakesh saxena'}

response = requests.post(baseurl + "add_user",
                     json=task,
                     headers={'Content-Type':'application/json',
                              'CSRF-TOKEN' : 'Random String'})
#response = requests.post("add_user", data = {"user" : "mayank"})
print("Request request:", response.request.headers)
print("*******")
print("Response Data: ", response.json())
#print(dir(response))
##print("Response isRedirect:", response.is_redirect)
#print("Response apparent_encoding:", response.apparent_encoding)
print("Response content:", response.content)
print("Response cookies:", response.cookies)
#print("Response elapsed:", response.elapsed)
#print("Response encoding:", response.encoding)
print("Response headers:", response.headers)
print("Response status_code:", response.status_code)
