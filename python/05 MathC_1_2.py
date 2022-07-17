# pip3 install sympy
from sympy import *
import random
import time


def AnglesToRadians(angles):  # 角度轉弧度
    return angles * pi / 180


def CalcTrigonometricFunction(func, angels):
    result = ''
    radians = AnglesToRadians(angels)  # 先轉弧度
    match func:
        case 'sin':
            result = sin(radians)
        case 'cos':
            result = cos(radians)
        case 'tan':
            result = tan(radians)
        case 'cot':
            result = cot(radians)
        case 'sec':
            result = sec(radians)
        case 'csc':
            result = csc(radians)
        case _:  # defalut，要在最後
            result = result
    # return round(N(result), 4) # 小數到4位
    return result

# for i in range(1,46): # 印出sin 1~45度
#     print(str(i).rjust(2)+'°=',round(N(CalcTrigonometricFunction('sin', i)),4)) # 四捨五入到小數四位


q1List = ['sin', 'cos', 'tan', 'cot', 'sec', 'csc']
q2List = [30, 45, 60]

print('\n輸入exit即可離開\n\n所有答案以分數表示\n\n根號x請以sqrt(x)輸入,例如根號3請書輸入sqrt(3)，分母不可有根號\n')

userTestTimes = input('請輸入測驗次數 = ?')
if not userTestTimes.isdigit():  # if not , str.isdigit()判斷是否是數字
    print('\n輸入次數非數字\n')
else:
    TotalStart = time.time()  # 總時間起時
    testTimes = 0  # 測驗次數
    rightTimes = 0  # 正確次數
    errorTimes = 0  # 錯誤次數
    for i in range(1, int(userTestTimes) + 1):  # range要+1
        q1 = q1List[random.randint(0, len(q1List))-1]  # random len 要-1
        q2 = q2List[random.randint(0, len(q2List))-1]  # random len 要-1
        question = q1 + str(q2) + '°'  # 題目
        ans = str(CalcTrigonometricFunction(q1, q2))  # 答案

        start = time.time()  # 此題起時
        # time.sleep(60) # 秒
        userAns = input('\n請輸入' + question + ' = ?')
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
        print(question + ' = ' + ans + ' , ' +
              goodJob + '共花費 ' + str(elapsedTime) + ' 秒')
    TotalEnd = time.time()  # 總時間迄時
    TotalElapsedTime = round(TotalEnd-TotalStart, 1)  # 總花費時間
    print('\n測驗 ' + str(testTimes) + ' 次，共花費 ' + str(TotalElapsedTime) +
          ' 秒\n答對 ' + str(rightTimes) + ' 題，答錯 ' + str(errorTimes) + ' 題，正確率 ' +
          ('0' if testTimes == 0 else str(100*round(rightTimes/testTimes, 2))) +
          ' %，平均每題作答時間 ' + ('0' if testTimes == 0 else str(round(TotalElapsedTime/testTimes, 1))) + ' 秒\n')
