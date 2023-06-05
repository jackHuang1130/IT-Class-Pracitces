import requests
from bs4 import BeautifulSoup
r = requests.get("http://tw.yahoo.com")
soup = BeautifulSoup(r.text, 'html.parser')

tags2 = soup.find_all("li", class_= "Fz(15px)")    
for tag in tags2:
    linkdata = tag.find('a')
    print(linkdata.text + '  ' + linkdata['href'])    