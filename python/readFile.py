# 程式不可以隨邊tab換段落，不然會有error

# 寫入
    # 分三段
# file = open("test.txt",mode="w",encoding="utf-8")
# file.write("測試中文\n好棒棒")
# file.close()

    # 一段式寫法
# with open("test.txt",mode="w",encoding="utf-8") as file:
#     file.write("測試中文\n好棒棒")

# 讀取
# sum = 0
# with open("test.txt",mode="r",encoding="utf-8") as file:
    # 全檔輸出
#     data = file.read()
# print(data)

    # 逐行處理
#     for line in file:
#         sum+=int(line)
# print(sum)

# 使用JSON
import json
with open("abc.json",mode="r",encoding="utf-8") as file:
    data = json.load(file) # 是字典資料
    keys=data.keys()
# print(keys)
for key in keys:
    print(key,"|",data[key])