# -*- coding: utf-8 -*-
"""webscrapingg.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1CK1oJbc3BBSJX-11GIcAp4i0uVavybk-
"""

from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://www.worldometers.info/coronavirus/'
req = requests.get(url)
print(req)

soup = BeautifulSoup(req.content, 'html.parser')

tablea = soup.find(name='table')

df = pd.read_html(str(tablea))[0].set_index('daily')

df.to_csv('covid_stats.csv)