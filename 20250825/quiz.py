#########################
# 題目來源：
# https://docs.google.com/document/d/1mGSF2hmyN_UpWNOEVKNSoksKOJymUVQl/edit?rtpof=true
#########################


### 1. 判斷偶數的函式
def isEven(num):
    if num % 2 == 0:
        return True
    else:
        return False


print("是否為偶數：", isEven(int(input("Q1. 請輸入數字判斷奇偶數"))))


### 2.判斷是否為3或5的倍數
def isMultipleOf3or5(num):
    if num % 3 == 0 and num % 5 == 0:
        print(f"{num}是3跟5的倍數")
    elif num % 3 == 0 and num % 5 != 0:
        print(f"{num}是3的倍數")
    elif num % 3 != 0 and num % 5 == 0:
        print(f"{num}是5的倍數")
    else:
        print(f"{num}不是3或5的倍數")


isMultipleOf3or5(int(input("Q2. 請輸入數字")))


### 3. 判斷閏年
"""
    1. 每四年一閏
    2. 每百年不閏
    3. 每四百年再閏
"""


def isLeapYear(year):
    if year % 4 == 0:
        if year % 400 == 0:
            return True
        elif year % 100 == 0:
            return False
        else:
            return True
    else:
        return False


print("是否為閏年：", isLeapYear(int(input("Q3. 請輸入年份判斷是否為閏年"))))


### 4. 任意數字做運算
import re

num1 = int(input("Q4. STEP1: 請輸入第一個數字"))
num2 = int(input("Q4. STEP2: 請輸入第二個數字 "))
operator = input("Q4. STEP3: 請輸入運算子(+,-,*,%): ")


def calculate(num1, num2, operator):
    if inputInvalid(num1, num2, operator):
        if operator == "+":
            return num1 + num2
        if operator == "-":
            return num1 - num2
        if operator == "*":
            return num1 * num2
        if operator == "%":
            return num1 % num2


def inputInvalid(num1, num2, operator):
    if re.fullmatch(r"\d+", str(num1)) == False:
        return {"isInvalid": True, "msg": "第一個數字無效"}
    elif re.fullmatch(r"\d+", str(num2)) == False:
        return {"isInvalid": True, "msg": "第二個數字無效"}
    elif operator in ["+", "-", "*", "%"] == False:
        return {"isInvalid": True, "msg": "運算子無效"}
    else:
        return {"isInvalid": False}


print(f"運算結果 {num1} {operator} {num2} =", calculate(num1, num2, operator))


### 5. 判斷字元種類
import re


def judgeCharType(char):
    if char.isdigit():
        return "數字"
    elif re.match(r"[a-zA-Z]", char):
        return "英文字母"
    elif re.match(r"[\W_]", char):
        return "符號"
    else:
        return "其他"


char = input("Q5. 請輸入一個字元")
print(f"你輸入的字元：{char}, 類型：{judgeCharType(char)}")


### 6. 判斷對應等級
def judgeLevel(score):
    if score >= 90:
        return "A"
    elif score >= 80 and score < 90:
        return "B"
    elif score >= 70 and score < 80:
        return "C"
    elif score >= 60 and score < 70:
        return "D"
    else:
        return "F"


score = int(input("請輸入你的分數"))
print(f"你的分數：{score}, 對應等級為：{judgeLevel(score)}")


### 7. 判斷對應折扣
def judgeDiscount(price):
    if price >= 8000:
        if price >= 38000:
            return "7折"
        elif price >= 28000 and price < 38000:
            return "8折"
        elif price >= 18000 and price < 28000:
            return "9折"
        else:
            return "9.5折"
    else:
        return "無折扣"


price = int(input("請輸入購買金額"))
print(f"購買金額:{price}, 對應折扣為:{judgeDiscount(price)}")


### 10. 任三個整數做升冪排列
def ascAllNum(num1, num2, num3):
    firstNum = None
    secondNum = None
    thirdNum = None

    if num1 >= num2 and num1 >= num3:
        thirdNum = num1
        firstNum, secondNum = ascNum(num2, num3)

    elif num2 >= num1 and num2 >= num3:
        thirdNum = num2
        firstNum, secondNum = ascNum(num1, num3)

    elif num3 >= num1 and num3 >= num2:
        thirdNum = num3
        firstNum, secondNum = ascNum(num1, num2)
    return firstNum, secondNum, thirdNum


def ascNum(num1, num2):
    return (num2, num1) if (num1 >= num2) else (num1, num2)


print("升冪排列結果：", ascAllNum(3, 1, 2))
