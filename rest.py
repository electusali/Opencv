import requests 
from bs4 import BeautifulSoup


url =  "https://www.doviz.com/"

response =  requests.get(url) 

html_icerigi = response.content 

soup =  BeautifulSoup(html_icerigi,"html.parser") 


 
for i in soup.find_all("div",{"class":"market-data"}):
    for a in i.find_all('span',{'class':'name'}):
            print(a.text)
           
    for a in i.find_all('div',{'class':'item'}):  
        for c in a.find_all('span',{'data-socket-attr':'s'}):
                print(f'{a.text} fiyati {c.text.strip()}')
                #print(c.text.strip())    