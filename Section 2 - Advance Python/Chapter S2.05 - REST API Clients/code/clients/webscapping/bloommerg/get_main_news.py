import requests
from bs4 import BeautifulSoup as BS

headers = {
    "DNT": "1",
    "TE": "Trailers",
    "Content-type": "application/x-www-form-urlencoded",
    "Host": "www.bloomberg.com",
    "Referer": "https://www.bloomberg.com/asia",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:67.0) Gecko/20100101 Firefox/67.0"
}
s = requests.Session()
html_content = s.get("https://www.bloomberg.com/asia", headers=headers)

html_text = html_content.text
html_soap = BS(html_text, 'html.parser')
print(html_soap)
#cont = html_soap.select("section#hub_story_package_1.story-package-module" \
#                        ".story-package-module__story__headline-link")

cont = html_soap.select("#hub_story_package_1.story-package-module .story-package-module__story__headline-link")

for data in cont:
    print(type(data))
    print(data)
