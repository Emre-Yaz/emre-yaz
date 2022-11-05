# This program tests if a given page is found or not on the server.
# Totally created by Emre-Yaz.

import requests
from bs4 import BeautifulSoup as bs



url = input('Enter the page url: ')
try:
    r = requests.get(url)
except requests.exceptions.ConnectionError as e:
    print('Not on the server.')
else:
    print('Page is found.')

#soup = bs(r.content,'html.parser')
#isfound = str(soup.find('h1'))



#if "This site can not be reached" in isfound:
#    print('Not on the server.')
#else:
#    print('Page is found.')
