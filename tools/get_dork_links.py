#!/usr/bin/env python3

from bs4 import BeautifulSoup
import requests

dork = 'inurl%3A"%2Fuser%2Fregister"+"Powered+by+Drupal"'
li = 30 #number page 10,20,30,...etc

def googlesearch(searchfor):
    for lis in range(li):
        if (lis%10):
            link = 'https://www.google.com/search?q=%s&ie=utf-8&oe=utf-8&start=%d' % (searchfor, lis)
            ua = {'User-Agent': 'curl/7.58.0'}
            payload = {'q': searchfor}
            response = requests.get(link, headers=ua, params=payload)
            soup = BeautifulSoup(response.text, 'html.parser')
            par = soup.find_all('h3', class_="r")
            for a in par:
                print(a.find('a').get('href'))

googlesearch(dork)
