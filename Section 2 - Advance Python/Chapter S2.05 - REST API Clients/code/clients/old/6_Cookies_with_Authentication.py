import requests 

session = requests.session()
user ="mayank"
password = "test"
p = session.post("http://127.0.0.1:5000/api/users", {'user':user,'password':password})
print ('headers', p.headers)
print ('cookies', requests.utils.dict_from_cookiejar(session.cookies))
print ('html',  p.text)