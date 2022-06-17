from lxml.etree import fromstring
import urllib3

http = urllib3.PoolManager()
source =  http.request('GET', "https://weather.com/en-IN/weather/today/l/INXX0096:1:IN")
# print(source.data)

data =  fromstring(source.data)
d = data.cssselect(".today_nowcard-sidecar > table > tbody > tr")
print(d)
