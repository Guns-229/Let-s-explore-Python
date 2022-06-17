# file: 102_resp_iter_content.py
# Run Chapter S2.06 - Web Development & REST API Servers/code/flask/swagatham_2.py
# for server

import requests
import unicode
try:
    r = requests.get("http://localhost:5000/tamil")
    print(r)
    print(r.status_code)
    print(r.text)
    print(r.json())
    content = ""
    for d in r.iter_content(decode_unicode=True):
        content += "".join(map(chr, d))
    # print(unicode(content, "utf-8"))
except Exception as e:
    print(e)
