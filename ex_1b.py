#!/usr/bin/env python
# coding: utf-8

# In[ ]:



from urllib import request
from bs4 import BeautifulSoup as BS
import re

# Look at the page and the code
url = 'https://en.wikipedia.org/wiki/List_of_rock_music_performers' 
html = request.urlopen(url)
bs = BS(html.read(), 'html.parser')

tags = bs.find_all('ul')[18].find_all('li')

links = ['http://en.wikipedia.org' + tag.a['href'] for tag in tags]

for link in links:
    print(link)

