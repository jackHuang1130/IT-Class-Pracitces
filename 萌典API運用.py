import requests
import json

var1 = input("請輸入國字 => ")

r = requests.get(f"https://www.moedict.tw/raw/{var1}")
data = json.loads(r.text)

bopomofo = []

for i in range(len(data['heteronyms'])):
    bopomofo.append(data['heteronyms'][i]['bopomofo'])
    
bopomofo_str = str(bopomofo)[1:-1]

print(f"部首：{data['radical']}")
print(f"筆劃：{data['stroke_count']}")
print(f"注音：{bopomofo_str}")