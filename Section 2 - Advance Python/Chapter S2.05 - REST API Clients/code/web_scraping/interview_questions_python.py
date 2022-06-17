"""."""

import requests

from bs4 import BeautifulSoup

PROXY = {
    "http": "http://PROXY:8080",
    "https": "http://PROXY:8080"
}


def get_download(url):
    """."""
    done_urls = []
    left_urls = [url]
    faqs = {}
    url = left_urls[0]
    print("Processing: ", url,
          len(done_urls), len(left_urls))
    response = requests.get(url)  # proxies=PROXY headers, cookies=cookies
    faqs = get_questions_from_page(response.text)
    return faqs


def get_questions_from_page(page):
    """."""
    soup = BeautifulSoup(page, 'html.parser')
    faqs = {}
    for a in soup.select('div[class="accordion-parent"]'):
        faqs[a.select('[class="accord-heading]"')[0].text] = a.select(
            '[class="accord-panel]"')[0].text
    return faqs


BASE_URL = "https://intellipaat.com"
if __name__ == "__main__":
    URL = BASE_URL + "/interview-question/python-interview-questions/"
    faqs = get_download(URL)
    print(faqs)
