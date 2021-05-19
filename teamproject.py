from selenium import webdriver
import pandas as pd
from bs4 import BeautifulSoup
import numpy as np
import matplotlib.pyplot as plt

URL = 'https://kr.noxinfluencer.com/youtube-channel-rank/top-100-all-all-youtuber-sorted-by-subs-weekly'
driver = webdriver.Chrome(executable_path='C:/Users/82109/Desktop/second/chromedriver.exe')
driver.get(url=URL)


data= driver.page_source

soup=BeautifulSoup(data,'lxml')

df=pd.read_html(soup.prettify())[0]

# print(df)

driver.quit()

channel_name = list(np.array(df.iloc[:, 1].tolist()))

# print(channel_name)

subscribe_num = list(np.array(df.iloc[:, 3].tolist()))

subscribe_num = [i.split()[0] for i in subscribe_num]

subscribe_num = [i.rstrip('억만') for i in subscribe_num]

count = 0

for i in subscribe_num:
    if '.' in i:
        subscribe_num[count] = i.replace('.', '')
        count += 1

count = 0

subscribe_num = [int(i) for i in subscribe_num]

for i in subscribe_num:
    count += 1
    if count == 3:
        subscribe_num[count - 1] *= 10
    elif count >= 5:
        subscribe_num[count - 1] /= 100

print(subscribe_num)
x=np.arange(len(channel_name))
plt.bar(x,subscribe_num)
plt.xticks(x,channel_name,rotation='vertical')
plt.show()