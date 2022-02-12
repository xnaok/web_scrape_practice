# Library
import requests
from bs4 import BeautifulSoup
from time import sleep

# Scraping
class Scr():
    def __init__(self, urls):
        self.urls=urls

    def geturl(self):
        all_text=[]
        for url in self.urls:
            r=requests.get(url)
            c=r.content
            soup=BeautifulSoup(c,"html.parser")
            article1_content=soup.find_all("p")
            temp=[]
            for con in article1_content:
                out=con.text
                temp.append(out)
            text=''.join(temp)
            all_text.append(text)
            sleep(1)
        return all_text

sc=Scr(["https://toukei-lab.com/conjoint","https://toukei-lab.com/correspondence"])
print(sc.geturl())

# 参考サイト：https://toukei-lab.com/python-can