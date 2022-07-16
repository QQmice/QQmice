import requests
from bs4 import BeautifulSoup

# url = 'https://www.ptt.cc/bbs/MobileComm/index.html'
# r = requests.get(url) #將此頁面的HTML GET下來
# print(r.text) #印出HTML
# soup = BeautifulSoup(r.text,"html.parser") #將網頁資料以html.parser
# sel = soup.select("div.title a") #取HTML標中的 <div class="title"></div> 中的<a>標籤存入sel
# for s in sel:
#     print(s["href"], s.text)

url = 'http://www.taiwantestcentral.com/WordList/BCTWordList.aspx?CategoryID=12'
r = requests.get(url)

soup = BeautifulSoup(r.text, "html.parser")
sel = soup.select("td")  # select 出td標籤
listLen = len(sel)//5 # 由於每五個td是一組資料，因此用整除法
wordList = [[None, None, None]] * listLen  # 宣告list指定大小

for i in range(0, listLen):
    word = sel[i*5].text  # 每五個抓其第一
    chinese = sel[i*5+2].text  # 每五個抓其第三
    wordList[i] = [i+1, word, chinese]  # 放進list

# for s in wordList:
#     print(s[0],s[1],s[2])

with open("word1250.txt", mode="w", encoding="utf-8") as file:
    for s in wordList:
        file.write(str(s[0])+','+s[1]+','+s[2]+'\n') # 第一個是數字要轉str
