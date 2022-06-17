import json
import requests


def login(username, password):
    url = "http://127.0.0.1:5000/login"
    data ={"username": "admin", "password": "admin"}
    res = requests.post(url, data)
    print(res, res.headers, res.text)
    return res.cookies


def select_topic(topic_id, cookies):
    url = "http://127.0.0.1:5000/start_quiz?topic={}".format(topic_id)
    res = requests.get(url, cookies=cookies)
    print(res, res.headers, res.text)

def take_test():
    pass

cookies = login("admin", "admin")
select_topic(2, cookies)
