import requests
from bs4 import BeautifulSoup
import json

r = requests.get("https://store.line.me/stickershop/product/16946272/zh-Hant")
soup = BeautifulSoup(r.text, 'html.parser')

tags = soup.find_all('li', class_="mdCMN09Li")

print(soup.title.text)
print(len(tags))
for tag in tags:
    data = tag.get("data-preview")
    data = json.loads(data)
    imgfile = requests.get(data['staticUrl'])
    with open(data['id']+'.png', 'wb') as f:
        f.write(imgfile.content)
        print(data['id'])
    