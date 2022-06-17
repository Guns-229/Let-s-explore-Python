
# Rest Clients 

## Requests
-------

Requests is the only Non-GMO HTTP library for Python, safe for human consumption.

> **Warning**: Recreational use of other HTTP libraries may result in dangerous side-effects, including: security vulnerabilities, verbose code, reinventing the wheel, constantly reading documentation, depression, headaches, or even death.

### Supported Features
Requests is ready for today's web.

* International Domains and URLs
* Keep-Alive & Connection Pooling
* Sessions with Cookie Persistence
* Browser-style SSL Verification
* Basic/Digest Authentication
* Elegant Key/Value Cookies
* Automatic Decompression
* Automatic Content Decoding
* Unicode Response Bodies
* Multipart File Uploads
* HTTP(S) Proxy Support
* Connection Timeouts
* Streaming Downloads
* .netrc Support
* Chunked Requests
* Thread-safety

### Sample of Requests


```python
import requests
r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
print(r.status_code)
print(r.headers['content-type'])
# print(r.encoding)
print(r.text)
print(r.json())
```


    ---------------------------------------------------------------------------

    SSLEOFError                               Traceback (most recent call last)

    C:\apps\WinPython-64bit-3.6.1.0Qt5\python-3.6.1.amd64\lib\site-packages\requests\packages\urllib3\connectionpool.py in urlopen(self, method, url, body, headers, retries, redirect, assert_same_host, timeout, pool_timeout, release_conn, chunked, body_pos, **response_kw)
        593             if is_new_proxy_conn:
    --> 594                 self._prepare_proxy(conn)
        595 


    C:\apps\WinPython-64bit-3.6.1.0Qt5\python-3.6.1.amd64\lib\site-packages\requests\packages\urllib3\connectionpool.py in _prepare_proxy(self, conn)
        809 
    --> 810         conn.connect()
        811 


    C:\apps\WinPython-64bit-3.6.1.0Qt5\python-3.6.1.amd64\lib\site-packages\requests\packages\urllib3\connection.py in connect(self)
        325             server_hostname=hostname,
    --> 326             ssl_context=context)
        327 


    C:\apps\WinPython-64bit-3.6.1.0Qt5\python-3.6.1.amd64\lib\site-packages\requests\packages\urllib3\util\ssl_.py in ssl_wrap_socket(sock, keyfile, certfile, cert_reqs, ca_certs, server_hostname, ssl_version, ciphers, ssl_context, ca_cert_dir)
        323     if HAS_SNI:  # Platform-specific: OpenSSL with enabled SNI
    --> 324         return context.wrap_socket(sock, server_hostname=server_hostname)
        325 


    C:\apps\WinPython-64bit-3.6.1.0Qt5\python-3.6.1.amd64\lib\ssl.py in wrap_socket(self, sock, server_side, do_handshake_on_connect, suppress_ragged_eofs, server_hostname, session)
        400                          server_hostname=server_hostname,
    --> 401                          _context=self, _session=session)
        402 


    C:\apps\WinPython-64bit-3.6.1.0Qt5\python-3.6.1.amd64\lib\ssl.py in __init__(self, sock, keyfile, certfile, server_side, cert_reqs, ssl_version, ca_certs, do_handshake_on_connect, family, type, proto, fileno, suppress_ragged_eofs, npn_protocols, ciphers, server_hostname, _context, _session)
        807                         raise ValueError("do_handshake_on_connect should not be specified for non-blocking sockets")
    --> 808                     self.do_handshake()
        809 


    C:\apps\WinPython-64bit-3.6.1.0Qt5\python-3.6.1.amd64\lib\ssl.py in do_handshake(self, block)
       1060                 self.settimeout(None)
    -> 1061             self._sslobj.do_handshake()
       1062         finally:


    C:\apps\WinPython-64bit-3.6.1.0Qt5\python-3.6.1.amd64\lib\ssl.py in do_handshake(self)
        682         """Start the SSL/TLS handshake."""
    --> 683         self._sslobj.do_handshake()
        684         if self.context.check_hostname:


    SSLEOFError: EOF occurred in violation of protocol (_ssl.c:749)

    
    During handling of the above exception, another exception occurred:


    SSLError                                  Traceback (most recent call last)

    C:\apps\WinPython-64bit-3.6.1.0Qt5\python-3.6.1.amd64\lib\site-packages\requests\adapters.py in send(self, request, stream, timeout, verify, cert, proxies)
        422                     retries=self.max_retries,
    --> 423                     timeout=timeout
        424                 )


    C:\apps\WinPython-64bit-3.6.1.0Qt5\python-3.6.1.amd64\lib\site-packages\requests\packages\urllib3\connectionpool.py in urlopen(self, method, url, body, headers, retries, redirect, assert_same_host, timeout, pool_timeout, release_conn, chunked, body_pos, **response_kw)
        629             clean_exit = False
    --> 630             raise SSLError(e)
        631 


    SSLError: EOF occurred in violation of protocol (_ssl.c:749)

    
    During handling of the above exception, another exception occurred:


    SSLError                                  Traceback (most recent call last)

    <ipython-input-10-c0090b60f282> in <module>()
          1 import requests
    ----> 2 r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
          3 print(r.status_code)
          4 print(r.headers['content-type'])
          5 # print(r.encoding)


    C:\apps\WinPython-64bit-3.6.1.0Qt5\python-3.6.1.amd64\lib\site-packages\requests\api.py in get(url, params, **kwargs)
         68 
         69     kwargs.setdefault('allow_redirects', True)
    ---> 70     return request('get', url, params=params, **kwargs)
         71 
         72 


    C:\apps\WinPython-64bit-3.6.1.0Qt5\python-3.6.1.amd64\lib\site-packages\requests\api.py in request(method, url, **kwargs)
         54     # cases, and look like a memory leak in others.
         55     with sessions.Session() as session:
    ---> 56         return session.request(method=method, url=url, **kwargs)
         57 
         58 


    C:\apps\WinPython-64bit-3.6.1.0Qt5\python-3.6.1.amd64\lib\site-packages\requests\sessions.py in request(self, method, url, params, data, headers, cookies, files, auth, timeout, allow_redirects, proxies, hooks, stream, verify, cert, json)
        486         }
        487         send_kwargs.update(settings)
    --> 488         resp = self.send(prep, **send_kwargs)
        489 
        490         return resp


    C:\apps\WinPython-64bit-3.6.1.0Qt5\python-3.6.1.amd64\lib\site-packages\requests\sessions.py in send(self, request, **kwargs)
        607 
        608         # Send the request
    --> 609         r = adapter.send(request, **kwargs)
        610 
        611         # Total elapsed time of the request (approximately)


    C:\apps\WinPython-64bit-3.6.1.0Qt5\python-3.6.1.amd64\lib\site-packages\requests\adapters.py in send(self, request, stream, timeout, verify, cert, proxies)
        495         except (_SSLError, _HTTPError) as e:
        496             if isinstance(e, _SSLError):
    --> 497                 raise SSLError(e, request=request)
        498             elif isinstance(e, ReadTimeoutError):
        499                 raise ReadTimeout(e, request=request)


    SSLError: EOF occurred in violation of protocol (_ssl.c:749)



```python
import requests

r = requests.get("http://localhost:5000")
print(r)
print(r.status_code)
print(r.text)
print(r.json())
```

    <Response [200]>
    200
    {"text" : "Welcome to the Rest Server"}
    {'text': 'Welcome to the Rest Server'}

