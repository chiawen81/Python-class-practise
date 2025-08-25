### 型別轉換
print("1. True+1",True+1)      # True會被當成 1
print("2. False+1",False+1)    # False會被當成 0

print("3. ",2.1+1)
print("4. ",int("2")+1)           # 字串轉整數
'''補充
    1. 轉換有小數點的字串成數字，需用float()
    2. 用int轉有小數點的字串(例如："2.1")，會報錯
'''
print("5. ",float("2.1"))         # 字串轉浮點數
print("6. ",float("2.1")+1)