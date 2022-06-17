import json
import requests
from requests import Session


def login(username, password, session):
    url = "http://127.0.0.1:5000/login"
    data ={"username": "admin", "password": "admin"}
    res = session.post(url, data)
    print(res, res.headers, res.text)
    return res.headers


def select_topic(topic_id, session):
    url = "http://127.0.0.1:5000/start_quiz?topic={}".format(topic_id)
    res = session.get(url, headers=headers)
    print(res, res.headers, res.text)

session = Session()
headers = login("admin", "admin", session)
select_topic(2, session)
