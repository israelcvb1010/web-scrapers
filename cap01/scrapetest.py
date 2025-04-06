from urllib.request import urlopen, HTTPError, URLError
from bs4 import BeautifulSoup


def get_title(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        print(e)
        return None
    try:
        bsObj = BeautifulSoup(html.read(), features='html.parser')
        title = bsObj.body.h1
    except AttributeError as e:
        print(e)
        return None
    return title


url = "https://brightdata.com.br/faqs/beautifulsoup/how-to-install/"
title = get_title(url)

if title == None:
    print("Title could not be found.")
else:
    print(title)

