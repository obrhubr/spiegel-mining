import time
import logging
logging.basicConfig(level=logging.DEBUG)
import requests
import re
from bs4 import BeautifulSoup
import json
import os

# extract : time, len, rubrik, author, title, title len, 

def ex_time(soup):
    date = soup.find_all('time')
    if date == []:
        return ''
    return date[0].contents[0]

def ex_len(soup):
    return len(soup.text.replace('\n', '').split())

def ex_rubrik(soup):
    ul = soup.find_all('ul', class_="swiper-wrapper relative flex items-center bottom-8")[0]
    li = ul.find_all('li')[1]
    r = li.find_all('span', class_="border-b whitespace-no-wrap border-inherit")
    rubrik = r[0].contents[0]
    if r == []:
        return ''
    return rubrik.replace('\n', '')

def ex_author(soup):
    header = soup.find_all('header')[0]
    author = header.find_all('a', class_="text-black font-bold border-b border-shade-light hover:border-black")
    if author == []:
        div = soup.find_all('div', class_="lg:w-8/12 md:w-10/12 lg:mx-auto md:mx-auto lg:px-24 md:px-24 sm:px-16")
        author = div[1].find_all('div', class_="font-sansUI lg:text-base md:text-base sm:text-s text-shade-dark mt-8")
        return author[0].contents[0]
    return author[0].contents[0]

def ex_keywords(soup):
    sections = soup.find_all('section', class_="lg:p-24 md:px-24 md:pt-24 sm:px-16 sm:pt-24 rounded shadow bg-white")[0]
    read_more = sections.find_all('div', class_="lazytrigger flex flex-row flex-shrink-0 overflow-hidden lg:mb-40 md:mb-40 sm:mb-32 relative font-sans")
    tags = read_more[0].find_all('div', class_="swiper-wrapper flex")
    keywords = tags[0].find_all('a')
    if keywords == []:
        return []
    data = []
    for i in keywords:
        data.append(i.contents[1].contents[0])
    return data

def extract_html(html):
    data = []
    soup = BeautifulSoup(html)

    # Get date in str format
    try:
        data.append(ex_time(soup))
    except:
        data.append('')
        logging.error('Fatal error: could not extract time: ')
    #Append article text
    try:
        data.append(ex_len(soup))
    except:
        data.append('')
        logging.error('Fatal error: could not extract length: ')
    # get rubrik
    try:
        data.append(ex_rubrik(soup))
    except:
        data.append('')
        logging.error('Fatal error: could not extract rubrik: ')
    # get author
    try:
        data.append(ex_author(soup))
    except:
        data.append('')
        logging.error('Fatal error: could not extract author: ')
    # get keywords
    try:
        data.append(ex_keywords(soup))
    except:
        data.append('')
        logging.error('Fatal error: could not extract keywords: ')

    return data