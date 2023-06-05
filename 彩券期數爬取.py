import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.taiwanlottery.com.tw/index_new.aspx')
soup = BeautifulSoup(r.text, 'html.parser')

##########

datas = soup.find('div', class_='contents_box02')
p = datas.find('span', 'font_black15').text
number = datas.find_all('div', class_='ball_tx ball_green')
number_special = datas.find('div', class_ = 'ball_red')

print(f"威力彩期數: {p}")
print("開出順序: ", end= "")

for i in range(6):
    print(number[i].text, end='')

print("")
print("大小順序: ", end='' )
 
for i in range(6,12):
    print(number[i].text, end='')

print('')

print(f"特別號: {number_special.text}")