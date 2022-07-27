import requests
import json
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from quopri import encode
from newsapi import NewsApiClient


r=requests.get("https://newsapi.org/v2/everything?q='+新冠肺炎, -外遇'&domains=ettoday.net,storm.mg,chinatimes.com,udn.com&language=zh&sort_by=relevancy&apiKey=7f1ae32693bb47489be385165d99364e").json()


a = r['articles']
#print(a.join(str))
f=open('exam2_2.json','w',encoding="UTF-8")
for b in a:
    print(b)
    content=json.dumps(b,ensure_ascii=False)
    f.write(content)
f.close()


