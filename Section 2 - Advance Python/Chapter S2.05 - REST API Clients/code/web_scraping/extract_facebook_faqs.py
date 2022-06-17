"""."""

import requests

from bs4 import BeautifulSoup


def get_download(url):
    """."""
    done_urls = []
    left_urls = [url]
    faqs = []
    while left_urls:
        url = left_urls[0]
        print("Processing: ", url,
              len(done_urls), len(left_urls))
        # To get English version of FAQ's
        cookies = dict(locale='en_US')
        headers = {'user-agent': 'my-app/0.0.1',
                   ' Accept-Language': 'en-US,en;q=0.5'}
        response = requests.get(url, headers, cookies=cookies)
        urls, fq = get_urls_from_page(response.text)
        if fq:
            faqs.extend(fq)
        done_urls.append(url)
        urls = set(urls)
        left_urls = list(urls.difference(done_urls))
    return faqs


def get_faqs(dt):
    """."""
    fq_list = []
    for a in dt.select('div[role="presentation"]'):
        try:
            fq = a.select('a[role="button"]')[0].text
            fa = a.parent.select('div[role="presentation"] + div')
            fa = fa[0].select("div:nth-of-type(1)")[0]
            fq_list.append([fq, fa])
        except Exception as error:
            print("Error: ", error)
    return fq_list


def get_urls_from_page(html_doc):
    """."""
    soup = BeautifulSoup(html_doc, 'html.parser')
    faqs1 = get_faqs(soup)
    urls = [BASE_URL + a['href']
            for a in soup.select('a[role="menuitem"]') if a.text]
    return urls, faqs1


BASE_URL = "https://www.facebook.com"
if __name__ == "__main__":
    URL = BASE_URL + "/help/?helpref=hc_global_nav"
    faqs = get_download(URL)
    with open("faqs.yml", "w") as f:
        d = "- {faq}\n\t- {ans}\n"
        for faq, ans in faqs:
            f.write(d.format(faq=faq, ans=ans))
