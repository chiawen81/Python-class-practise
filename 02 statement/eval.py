###eval
'''
1. 用途：將字串當成程式碼執行
2. 可用範圍：
    (1) 只能執行「表達式」（expression），例如：數學運算、函式呼叫、資料結構操作等。
    (2) 不能執行多行語句（statement），例如：for、while、def 等。
3. 風險：有資安疑慮，因為它可以執行任何 Python 程式碼
    =>除非有非常特殊且安全的需求，否則應避免使用 eval
    =>eval 幾乎不會在正式專案中出現，在 code review 會被抓錯
'''

# 情境一：計算字串形式的數學表達式
print(eval("3+5"))
print(eval("3.2+5"))


# 情境二：運算變數或函式
x=10
print(eval("x+5"))


# 情境三：呼叫函式
def greet(name):
    return f"Hello, {name}!"

print(eval("greet('Wen')"))


# 情境四：操作資料結構
my_list = [1, 2, 3]
print(eval("my_list[1] * 10"))  # 輸出 20