import socket


class Get_Quotes(object):
    def __init__(self, base_api_path):
        self.base_api_path = base_api_path

    def __enter__(self):
        # Bad code, use the following
        # server = base_api_path.split("/")[2].split(":")
        # if len(server) > 1:
        #     server, port = server[0], server[1]
        # else:
        #     server = server[0]
        #     port = 80

        # better code
        server, *port = self.base_api_path.split("/")[2].split(":")
        if not port:
            port = 80
        print(server, port)
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((server, port))

    def get(api_path, data):
        # self.s.send
        pass

    def __exit__(self):
        self.s.close()


base_api_path = "https://jsonplaceholder.typicode.com"

api = "/posts/1"

server, *port = base_api_path.split("/")[2].split(":")
if not port:
    port = 80
print(server, port)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((server, port))
data = f"""GET {api} HTTP/1.0
:authority: jsonplaceholder.typicode.com
:method: GET
:path: /posts/1
:scheme: https
accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
accept-encoding: gzip, deflate, br
accept-language: en-US,en;q=0.9,hi;q=0.8
cache-control: max-age=0
cookie: __cfduid=da7c0631b0fcc65f15f9a13674da18d8f1529117488; _ga=GA1.2.915788684.1529117388; _gid=GA1.2.41669328.1529117388
dnt: 1
if-none-match: W/"124-yiKdLzqO5gfBrJFrcdJ8Yq0LGnU"
upgrade-insecure-requests: 1
user-agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.361   91301e58-8031-4b36-bf30-7f8dd21cfc56\r\n\r\n"""
# data = f"GET {api} HTTP/1.0\r\nContent-Type: text/html;\r\nUser-Agent: curl/7.16.3 libcurl/7.16.3 OpenSSL/0.9.7l zlib/1.2.3\r\nAccept-Language: en\r\n\r\n"
print(data)
s.send(data.encode())
MSGLEN = 2048
chunks = []
bytes_recd = 0
while bytes_recd <= MSGLEN:
    chunk = s.recv(min(MSGLEN - bytes_recd, 2048))
    if chunk == b'':
        raise RuntimeError("socket connection broken")
    chunks.append(chunk)
    bytes_recd = bytes_recd + len(chunk)
print(chunks)
s.close()
print("done")
