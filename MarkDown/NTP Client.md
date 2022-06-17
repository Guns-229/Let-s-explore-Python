
# NTP Client


```python
#!/usr/bin/env python
from socket import AF_INET, SOCK_DGRAM
import sys
import socket
import struct, time

def getNTPTime(host = "pool.ntp.org"):
        port = 123
        buf = 1024
        address = (host, port)
        print(address)
        msg = '\x1b' + 47 * '\0'

        # reference time (in seconds since 1900-01-01 00:00:00)
        TIME1970 = 2208988800 # 1970-01-01 00:00:00

        # connect to server
        client = socket.socket( AF_INET, SOCK_DGRAM)
        client.sendto(msg, address)
        msg, address = client.recvfrom( buf )

        t = struct.unpack( "!12I", msg )[10]
        t -= TIME1970
        return time.ctime(t).replace("  "," ")

if __name__ == "__main__":
        print (getNTPTime())
```

    ('pool.ntp.org', 123)
    


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-4-c5b0a5c09c26> in <module>()
         25 
         26 if __name__ == "__main__":
    ---> 27         print (getNTPTime())
    

    <ipython-input-4-c5b0a5c09c26> in getNTPTime(host)
         17         # connect to server
         18         client = socket.socket( AF_INET, SOCK_DGRAM)
    ---> 19         client.sendto(msg, address)
         20         msg, address = client.recvfrom( buf )
         21 
    

    TypeError: a bytes-like object is required, not 'str'



```python

```
