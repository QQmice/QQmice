# pip install pyinstaller
# pyinstaller -F '.\06 word309B1B2.py'
import random
import time

wordList = []  # 宣告list為空
with open('06 word309B1B2.txt', mode='r', encoding='utf-8') as file:
    for line in file:
        list = line.split("￡")
        wordList.append(list)

# for s in wordList:
#     print(s[0],s[1])

print('\n輸入exit即可離開\n\n大小寫要注意\n\n')

userTestTimes = input('請輸入測驗次數 = ? ')
wordListLen = len(wordList)
if not userTestTimes.isdigit():  # if not , str.isdigit()判斷是否是數字
    print('\n輸入次數非數字\n')
elif int(userTestTimes) > wordListLen:
    print('\n輸入次數超過單字數' + str(wordListLen) + '\n')
else:
    TotalStart = time.time()  # 總時間起時
    testTimes = 0  # 測驗次數
    rightTimes = 0  # 正確次數
    errorTimes = 0  # 錯誤次數
    for i in range(1, int(userTestTimes) + 1):  # range要+1
        rand = random.randint(0, wordListLen)-1  # random len 要-1
        qList = wordList.pop(rand)  # 去掉此次以免重複
        question = qList[1].rstrip()  # 題目 rstrip()刪除尾隨的換行符號
        ans = qList[0]  # 答案
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
        wordListLen -= 1
    TotalEnd = time.time()  # 總時間迄時
    TotalElapsedTime = round(TotalEnd-TotalStart, 1)  # 總花費時間
    print('\n測驗 ' + str(testTimes) + ' 次，共花費 ' + str(TotalElapsedTime) +
          ' 秒\n答對 ' + str(rightTimes) + ' 題，答錯 ' + str(errorTimes) + ' 題，正確率 ' +
          ('0' if testTimes == 0 else str(100*round(rightTimes/testTimes, 2))) +  # 防分母0之處理
          ' %，平均每題作答時間 ' + ('0' if testTimes == 0 else str(round(TotalElapsedTime/testTimes, 1))) + ' 秒\n')  # 防分母0之處理
