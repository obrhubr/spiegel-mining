import time
import logging
logging.basicConfig(level=logging.DEBUG, filename='wrangler.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
import requests
import re
from bs4 import BeautifulSoup
import json
import os

import wrangler.lib.extractor as ex
import wrangler.lib.datasetifier as dsf

def already_wrangled(data, n):
    for d in data:
        if d["name"] == n:
            return True
    return False

def main():
    data = []

    with open("data/wranglerdata.json", encoding="utf-8") as json_file:
        jsondata = json.load(json_file)

    files = [f for f in os.listdir("data/articles/") if os.path.isfile(os.path.join("data/articles/", f))]
    wranglerdata = {}
    wranglerdata["data"] = []
    for n in files:
        if n == "articles.json":
            continue

        if already_wrangled(jsondata["data"], n):
            continue

        wranglerdata["data"].append({"name": n})
        
        logging.info("Extracting features: " + n)
        f = open("data/articles/" + n, "r", encoding='utf-8')
        html = f.read()

        returndat = ex.extract_html(html)
        
        if returndat != []:
            data.append(returndat)

    json_data = wranglerdata["data"]+jsondata["data"]
    combined_data = {"data": json_data}

    with open("data/wranglerdata.json", 'w', encoding="utf-8") as outfile:
            json.dump(combined_data, outfile)
            outfile.close()

    logging.info("Writing features  to csv: ")
    dsf.write_csv('alldata.csv', ["time", "length", "rubrik", "author", "keywords"], data)