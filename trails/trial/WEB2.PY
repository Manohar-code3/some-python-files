import requests
from bs4 import BeautifulSoup
r=requests.get("https://www.flexjobs.com/search?search=part+time&location=india")
# print(r.status_code)
soup=BeautifulSoup(r.content,'html.parser')
# print(soup)
def tran(soup):
    divs=soup.find_all('li', class_ = 'm-0 row job')
    for i in divs:
        tittle=i.find('div', class_='row align-items-center mb-2').text
        return tittle
print(tran(soup))