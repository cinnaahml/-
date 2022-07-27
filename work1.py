from distutils.filelist import findall
from importlib.resources import path
from lib2to3.pgen2 import driver
from click import option
import requests
import json
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

'''
option=webdriver.ChromeOptions()
option.add_argument("headless")
driver=webdriver.Chrome()

'''

r=requests.get("https://technews.tw/")

soup=BeautifulSoup(r.text,"html.parser")
a=soup.findAll("li",{"class":"block2014"})
print(len(a))
my_data=[]
for obj in a:
    category=obj.find("div",{"class":"cat01"})
    sum_title=obj.find("div",{"class":"sum_title"}).find("h3")
    sum_title_url=obj.find("div",{"class":"img"}).find("a")
   
    e=[]       
    t3=obj.find("div",{"class":"itemelse"}).find_all("li",{"class":"spotlist"})
    for rr in t3:
        t4=rr.find("a")
        e.append({"title":t4.text,"url":t4["href"]})    

    my_data.append({"category":category.text,"sum_title":sum_title.text,"sum_title_url": sum_title_url["href"],"spotlist":e})
print(my_data)

content = json.dumps(my_data,ensure_ascii=False)
# 列表轉換為json 字串 ，不使用ascii編碼，
f = open('work1_1.json','w')
f.write(content)
f.close()


