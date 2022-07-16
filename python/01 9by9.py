for i in range(1, 10):
    for j in range(1, 10):
        # 乘積
        product = str(i * j)  # 轉字串，因為print
        # 因為九九乘法最多兩位數，若長度不足兩位時
        if len(product) < 2:
            product = " " + product  # 左邊補空白
        print(str(i) + ' x ' + str(j) + ' = ' + product + '   ', end='')
    print()  # newline
