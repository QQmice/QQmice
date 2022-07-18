# pip install requests
# pip install beautifulsoup4
# pip install pyinstaller
# pyinstaller -F '.\04 word1250.py'
from bs4 import BeautifulSoup
import requests
import random
import time

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
listLen = len(sel)//5  # 由於每五個td是一組資料，因此用整除法
wordList = [[None, None, None]] * listLen  # 宣告list指定大小

for i in range(0, listLen):
    word = sel[i*5].text  # 每五個抓其第一
    chinese = sel[i*5+2].text  # 每五個抓其第三
    wordList[i] = [i+1, word, chinese]  # 放進list

# for s in wordList:
#     print(s[0],s[1],s[2])

# with open("word1250.txt", mode="w", encoding="utf-8") as file:
#     for s in wordList:
#         file.write(str(s[0])+','+s[1]+','+s[2]+'\n') # 第一個是數字要轉str

print('\n輸入exit即可離開\n\n大小寫要注意\n\n因為使用BeautifulSoup須保持網路連線\n')

userTestPos = input('請輸入測驗起點(1~13) = ? ')
userTestTimes = 100
wordListLen = len(wordList)
if not userTestPos.isdigit():  # if not , str.isdigit()判斷是否是數字
    print('\n輸入起點非數字\n')
elif (int(userTestPos) < 1) or (int(userTestPos)-1 > wordListLen//userTestTimes):
    print('\n輸入起點超過範圍' + '\n')
else:
    TotalStart = time.time()  # 總時間起時
    testTimes = 0  # 測驗次數
    rightTimes = 0  # 正確次數
    errorTimes = 0  # 錯誤次數
    startPos = (int(userTestPos)-1)*100
    for i in range(1, int(userTestTimes) + 1):  # range要+1
        rand = random.randint(startPos, startPos+99)  # random len 要-1
        qList = wordList.pop(rand)  # 去掉此次以免重複
        qIndex = qList[0]  # 索引
        question = qList[2]  # 題目
        ans = qList[1]  # 答案
        start = time.time()  # 此題起時
        # time.sleep(60) # 秒
        userAns = input('\n請輸入 ' + question + ' 的英文 = ? ')
        if userAns == 'exit':  # exit 可離開
            break
        end = time.time()  # 此題迄時
        elapsedTime = round(end-start, 1)  # 花費時間
        testTimes += 1
        # goodJob = '答對了！' if ans == userAns else '答錯了！' # 由於要計算正確錯誤次數，因此無法寫一行
        if ans == userAns:
            goodJob = '答對了！'
            rightTimes += 1
        else:
            goodJob = '答錯了！'
            errorTimes += 1
        print('答案是 ' + ans + ' , ' +
              goodJob + '共花費 ' + str(elapsedTime) + ' 秒')
    TotalEnd = time.time()  # 總時間迄時
    TotalElapsedTime = round(TotalEnd-TotalStart, 1)  # 總花費時間
    print('\n測驗 ' + str(testTimes) + ' 次，共花費 ' + str(TotalElapsedTime) +
          ' 秒\n答對 ' + str(rightTimes) + ' 題，答錯 ' + str(errorTimes) + ' 題，正確率 ' +
          ('0' if testTimes == 0 else str(100*round(rightTimes/testTimes, 2))) + # 防分母0之處理
          ' %，平均每題作答時間 ' + ('0' if testTimes == 0 else str(round(TotalElapsedTime/testTimes, 1))) + ' 秒\n') # 防分母0之處理
