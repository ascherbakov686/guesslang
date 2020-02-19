#!/usr/bin/env python3

from bs4 import BeautifulSoup
import glob
#from urllib.request import urlopen
from requests_html import HTMLSession
from urllib.parse import urlsplit
from re import compile

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

for f in glob.glob("../datasets/list_of_sites/drupal/*.html"):
 soup = BeautifulSoup(open(f), 'html.parser')
 par = soup.find_all('a', href=True)
 rex = compile('.*google.*')

 for a in par:
   if not rex.match(str(a)):
     base_url = "{0.scheme}://{0.netloc}/".format(urlsplit(a['href']))
     if base_url != ':///':
      session = HTMLSession()
      r = session.get(base_url,verify=False)
      with open('../datasets/learn/%s.html.drupal' % urlsplit(a['href']).netloc, 'w', encoding='utf-8') as f_out:
         f_out.write(r.html.html)
         f_out.close()
