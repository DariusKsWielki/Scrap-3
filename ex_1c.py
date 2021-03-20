#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from urllib import request
from bs4 import BeautifulSoup as BS
import re
import pandas as pd

url = 'https://en.wikipedia.org/wiki/Queen_(band)' 
html = request.urlopen(url)
bs = BS(html.read(), 'html.parser')
name= bs.find('div', class_="fn org").text
genres= bs.find('th',string = 'Genres').next_sibling.text
years_active = bs.find('th',string = 'Years active').next_sibling.text

print("Name: "+ name +" Gneres: "+ genres + " Years active: "+ years_active)

