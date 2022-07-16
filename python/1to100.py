for i in range(0, 10):  # 0~9
    for j in range(1, 11):  # 1~10
        result = str(i * 10 + j)
        iMod = i % 2  # 十位數%值
        jMod = j % 2  # 個位數%值

        # if的寫法
        # if iMod ==0 and jMod == 0:#十位數偶數，個位數偶數
        #     result = result
        # if iMod ==0 and jMod == 1:#十位數偶數，個位數奇數
        #     result = ''
        # if iMod ==1 and jMod == 0:#十位數奇數，個位數偶數
        #     result = ''
        # if iMod ==1 and jMod == 1:#十位數奇數，個位數奇數
        #     result = result

        # match_case的寫法
        match (iMod, jMod):  # 可傳變數
            case (0, 0) | (1, 1): # | = 或
                result = ''
            case (0, 1) | (1, 0):
                result = result
            case _:  # defalut，要在最後
                result = result

        printLen = 4
        # x.rjust(n)[:n] 小括號是補多長，中括號是多長切掉
        # rjust:左側填補空格(靠右對齊) ljust:右側填補空格(靠左對齊)
        print(result.rjust(printLen)[:printLen], end='') 
    print()  # newline
