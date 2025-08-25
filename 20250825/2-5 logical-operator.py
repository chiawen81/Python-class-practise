### 邏輯運算子
'''
1. 用途：用於組合布林值（Boolean）的運算子
2. 主要運算子：
    (1) and：當兩個布林值都為 True 時，結果才為 True
    (2) or：當至少一個布林值為 True 時，結果為 True
    (3) not：對布林值取反
'''

# and 的範例
print(True and True)   # 輸出 True
print(True and False)  # 輸出 False

# or 的範例
print(True or False)   # 輸出 True
print(False or False)  # 輸出 False

# not 的範例
print(not True)        # 輸出 False
print(not False)       # 輸出 True



### 特殊用法
'''
    1. 當and與or混用時，會先計算and，再計算or
    2. 短路運算：
        (1) 在and運算中，如果第一個條件為False，則不會計算第二個條件
        (2) 在or運算中，如果第一個條件為True，則不會計算第二個條件
'''
# 範例：and與or混用
level=input("請輸入你的等級(A/B)")
score=int(input("請輸入你的成績"))
if level=="A" and score>=90 or level=="B" and score>=80:
    print("level:",level,"score:",score,"可以蓋三個好寶寶章")
else: 
    print("level:",level,"score:",score,"再接再厲!")