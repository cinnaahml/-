from distutils.filelist import findall
from encodings import utf_8
from fileinput import close
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
f=open("work1_1.json","r")
content = f.read()
print(123)
f=close()
a=json.loads(content)
print(type(a))
print(a[0]["sum_title_url"])
print("sum_"+a[0]["category"][0:2]+"_"+a[0]["sum_title"][0:4]+".txt")
print("sport_"+a[0]["category"][0:2]+"_"+a[0]["spotlist"][0]["title"][0:4]+".txt")

for i in range(0,8):
    name1="sum_"+a[i]["category"][0:2]+"_"+a[i]["sum_title"][0:4]+".txt"
    r=requests.get(a[i]["sum_title_url"])

    soup=BeautifulSoup(r.text,"html.parser")
    aa=soup.find("div",{"class":"indent"}).find_all("p")
    fa = open(name1,'a',encoding="utf-8")
    for obj in aa:
        t1=obj.text
        print(t1)
        fa.write(t1)
    fa.close()

    for m in range(0,3):
        name2="sport_"+a[i]["category"][0:2]+"_"+a[i]["spotlist"][m]["title"][0:4]+".txt"
        r=requests.get(a[i]["spotlist"][m]["url"])

        soup=BeautifulSoup(r.text,"html.parser")
        aa=soup.find("div",{"class":"indent"}).find_all("p")
        fa = open(name2,'a',encoding="utf-8")
        for obj in aa:
            t1=obj.text
            print(t1)
            fa.write(t1)
        fa.close()



