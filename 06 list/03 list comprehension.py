# 共用程式碼
##################################################
import re

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# 判斷是否為正整數
def isPositiveInt(str):
    return re.fullmatch(r"[1-9]\d*", str) is not None


# 常見應用
##################################################

##### 基本型（只有 for）#####
# 原本寫法：
list_a = []
for item in range(10):
    list_a.append(item)
# list comprehension 寫法：
list_b = [item for item in range(10)]
print(list_a)
print(list_b)


##### 篩選型（for + if）#####


##### 轉換型（for + if else）#####


##### 巢狀迴圈型（雙層 for）#####
