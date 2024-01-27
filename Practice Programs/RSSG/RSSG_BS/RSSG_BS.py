import urllib.request
from bs4 import BeautifulSoup

get = urllib.request.urlopen("https://www.lightnovelpub.com/novel/reincarnation-of-the-strongest-sword-god-lnv-10051457/chapter-58")
html = get.read()

soup = BeautifulSoup(html)

print(soup)
