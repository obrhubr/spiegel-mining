# fetch the news site, load article, compare it, pass it on
import requests
import logging
import re
from bs4 import BeautifulSoup
import json

def check_news(links):
    with open("data/new/site.json", encoding="utf-8") as json_file:
        data = json.load(json_file)
    if links == data:
        logging.info("The files are identical: ")
        return True
    return False

def get_links(html):
    soup = BeautifulSoup(html)
    soup = soup.find_all('article')

    links = {}
    links["data"] = []
    linkar = []

    for s in soup:
        if len(s.find_all('svg')) == 0:
            linkar.append(s.find_all('a'))

    for l in linkar:
        data = {}
        data["url"] = re.match(r"<a\s+(?:[^>]*?\s+)?href=([\"'])(.*?)\1", str(l[0]))[2]
        data["title"] = re.match(r"<a\s+(?:[^>]*?\s+)?title=([\"'])(.*?)\1", str(l[0]))[2]
        links["data"].append(data)

    return links

def run():
    r = requests.get("https://www.spiegel.de/schlagzeilen/")
    html = r.text
    links = get_links(html)

    if check_news(links) == True:
        return False
    else:
        with open("./data/new/site.json", 'w', encoding="utf-8") as outfile:
            json.dump(links, outfile)
            outfile.close()

        return True