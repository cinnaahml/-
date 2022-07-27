from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
import pickle
import pymongo
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
#myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = client["work3"]
mycol = mydb["work3_3"]

options = webdriver.ChromeOptions()
options.add_argument("headless")

driver = webdriver.Chrome(options = options)

f=open('exam3_11.txt','a')
fa=open('exam3_12.pickle','wb')

for i in range(1,4):
    a = "https://gogakuru.com/english/phrase/genre/180_%E5%88%9D%E7%B4%9A%E3%83%AC%E3%83%99%E3%83%AB.html?pageID=" + str(i) + '&flow=enSearchGenre&condGenre=180&layoutPhrase=1&orderPhrase=1&condMovie=0&perPage=50'
    print(a)
    driver.get(a)
    time.sleep(5)
    r = driver.find_elements(By.CLASS_NAME,'en')
    #print(len(r))   
    for aa in r:
        f.write(aa.text+'\n')
        pickle.dump(aa.text, fa)
    
    records=[]
    for i , x in enumerate(r):
        d={}
        i+=1
       
        d['item']= i
        d['mesg']=x.text
        records.append(d)        
    print(records)
    mycol.insert_many(records)

f.close()
fa.close()
driver.quit()





    