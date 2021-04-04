import requests
import re
from bs4 import BeautifulSoup
import json

def write_to_file(html, filename):
    filename = "".join([c for c in filename if c.isalpha() or c.isdigit() or c==' ']).rstrip()
    with open("./data/articles/" + filename + ".html", 'w', encoding="utf-8") as outfile:
        outfile.write(html)
        outfile.close()
    return

def hasNot(l, data2):
    for l2 in data2["data"]:
        if l2 == l:
            return False
    return True

def run():
    with open("data/new/site.json", encoding="utf-8") as json_file:
        data = json.load(json_file)
    
    with open("data/articles/articles.json", encoding="utf-8") as json_file:
        data2 = json.load(json_file)

    for l in data["data"]:
        if hasNot(l, data2):
            data2["data"].append(l)

            r = requests.get(l["url"])
            html = r.text
            write_to_file(html, l["title"])

    with open("data/articles/articles.json", 'w', encoding="utf-8") as outfile:
            json.dump(data2, outfile)
        
        