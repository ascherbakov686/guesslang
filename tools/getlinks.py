#!/usr/bin/env python3

from bs4 import BeautifulSoup
from requests_html import HTMLSession
import sys

if not sys.warnoptions:
    import warnings
    warnings.simplefilter("ignore")

dork = 'inurl%3A"%2Fuser%2Fregister"+"Powered+by+Drupal"'
li = 1000

def googlesearch(searchfor):
    for lis in range(li):
        if (lis%10):
            link = 'https://www.google.com/search?q=%s&ie=utf-8&oe=utf-8&start=%d' % (searchfor, lis)
            session = HTMLSession()
            r = session.get(link,verify=False)
            soup = BeautifulSoup(r.html.html, 'html.parser')
            par = soup.find_all('a', href=True)
            for a in par:
                print(a)

googlesearch(dork)
