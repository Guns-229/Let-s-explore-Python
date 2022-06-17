import unittest
import requests

proxies = {
              "http"  : "http://127.0.0.1:8080",
              "https" : "https://127.0.0.1:8080",
              "ftp"   : "ftp://127.0.0.1:8080"
            }

def login(s, username, passwd):
  login_url = "http://127.0.0.1:5000/login"
  data = {"username": username, "password": passwd}
  resp = s.post(login_url, data=data, proxies=proxies)
  return "Successfully logged in." in resp.text


class Test_Login(unittest.TestCase):
  def setUp(self):
    self._sess = requests.Session()
    login(self._sess,  "mayank.johri", "mayank.johri")


  def tearDown(self):
    self._sess.close()


  def test_wrong_username(self):
    wrong_username = "mayank.1johri"
    passwd = "wrong"
    urls = {}
    login_url = "http://127.0.0.1:5000/login"
    data = {"username": wrong_username, "password": passwd}
    s = requests.Session()
    resp = s.post(login_url, data=data,  proxies=proxies)
    self.assertNotIn("Successfully logged in.", resp.text)
    s.close()


  def test_wrong_password(self):
    username = "mayank.johri"

    passwd = "wrong"
    urls = {}
    login_url = "http://127.0.0.1:5000/login"
    data = {"username": username, "password": passwd}
    s = requests.Session()
    resp = s.post(login_url, data=data,  proxies={'http_proxy': proxy})
    self.assertNotIn("Successfully logged in.", resp.text)
    s.close()

  def test_sample_login(self):
    username = "mayank.johri"
    currect_passwd = "mayank.johri"
    wrong_passwd = "wrong"
    urls = {}
    login_url = "http://127.0.0.1:5000/login"
    data = {"username": username, "password": currect_passwd}
    s = requests.Session()
    resp = s.post(login_url, data=data)
    self.assertIn("Successfully logged in.", resp.text)
    s.close()

  def test_select_topic(self):
    url =  "http://127.0.0.1:5000/start_quiz?topic=1"
    resp = self._sess.get(url)
    print(resp.text)
    self.assertIn("Welcome to Pareekshan", resp.text)
  # def test_start_quiz(self):
