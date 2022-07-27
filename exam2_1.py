from quopri import encode
from newsapi import NewsApiClient
import json

newsapi = NewsApiClient(api_key='7f1ae32693bb47489be385165d99364e')
 
all_articles = newsapi.get_everything(q='+新冠肺炎, -外遇',                                    
                                      domains='ettoday.net , storm.mg , chinatimes.com , udn.com ',
                                      language='zh',
                                      sort_by='relevancy')
content=json.dumps(all_articles,ensure_ascii=False)
f=open('exam2_1.json','w',encoding="UTF-8")
f.write(content)
f.close()