# Fetch https://www.spiegel.de/schlagzeilen/ this page. Cache it. Check every minute if the cached article doesn't match the new one, etc...
import miner.lib.fetch_new as fn
import miner.lib.fetch_article as fa
import miner.lib.write_article as wa

import logging
logging.basicConfig(level=logging.DEBUG, filename='miner.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')

def routine():
    logging.info("Reading 'schlagzeilen' page to find new articles: ")
    newsite = fn.run()
    logging.info("Finished updating the new/site.json file: ")
    if newsite == True:
        logging.info("Downloading new articles: ")
        fa.run()

def main():
    logging.info("Starting to get data: ")
    routine()