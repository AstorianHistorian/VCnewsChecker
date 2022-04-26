from bs4 import BeautifulSoup as bs
import requests
import time
 
def Get_news():
    n =''
    while True:
        res = requests.get(f"https://vc.ru/new")
        news = bs(res.text, "html.parser")
        latest = news.find(class_='content-container')
        latest_ttl = latest.find(class_='content-title content-title--short l-island-a').get_text()
        latest_txt = latest.find(class_='content-title content-title--short l-island-a').find_next(class_ ='l-island-a').get_text()
        latest_link = news.find(class_="content-link")["href"]
        latest_ttl = latest_ttl.replace("\n","").replace("  ","").replace("Статьи редакции","")
        latest_txt = latest_txt.replace("\n","").replace("  ","")
        if n !=latest_ttl:
            link = f"https://api.telegram.org/bot5208323305:AAGNycGqX3hN9qu_6_L0Z3Pq3jHOkn-PbxI/sendMessage?chat_id=-1001656484044&text={latest_ttl}\n{latest_txt}\n{latest_link}"
            requests.get(link)
            n = latest_ttl
        time.sleep(300)  

Get_news()
