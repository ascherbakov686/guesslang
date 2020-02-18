#!/usr/bin/env python3

from bs4 import BeautifulSoup
import glob

for f in glob.glob("../datasets/list_of_sites/drupal/*.html"):
 print(f)
 soup = BeautifulSoup(open(f), 'html.parser')
 par = soup.find_all('a', href=True)
 for a in par:
   print(a['href'])
