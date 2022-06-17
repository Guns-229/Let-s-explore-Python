import requests


def  sample_login():
  username = "mayank.johri"
  currect_passwd = "mayank.johri"
  wrong_passwd = "wrong"
  urls = {}
  login_url = "http://127.0.0.1:5000/login"
  data = {"username": username, "password": currect_passwd}
  s = requests.Session()
  resp = s.post(login_url, data=data)
  print(resp, dir(resp))
  print(resp.text)

sample_login()
