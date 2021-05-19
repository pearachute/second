from selenium import webdriver
import pandas as pd
from bs4 import BeautifulSoup
import numpy as np
import matplotlib.pyplot as plt

URL = 'https://kr.noxinfluencer.com/youtube-channel-rank/top-100-all-all-youtuber-sorted-by-subs-weekly'
driver = webdriver.Chrome(executable_path='C:/Users/82109/PycharmProjects/minie_sng/chromedriver.exe')
driver.get(url=URL)


data= driver.page_source

soup=BeautifulSoup(data,'lxml')

df=pd.read_html(soup.prettify())[0]

# print(df)

driver.quit()