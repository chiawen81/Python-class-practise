#########################
# 題目來源：
# https://docs.google.com/document/d/1gyuk66bQsMqpUYnBXSg4DWz5LXqB_880/edit
#########################

#########################
# 共用程式碼
#########################
import re


# 判斷是否為正整數
def isPositiveInt(str):
    return re.fullmatch(r"[1-9]\d*", str) is not None


# ### 題目一 ###
# # 由使用者輸入10個數字，找出其中的最小值並且輸出
# q1_min_num = 0
# q1_record = ""

# for idx in range(10):
#     user_input = int(input(f"Q1. 請輸入第{idx+1}個數字"))
#     q1_record = q1_record + str(user_input) + " "

#     if idx == 0:
#         q1_min_num = user_input
#     else:
#         q1_min_num = user_input if (q1_min_num > user_input) else q1_min_num

# print(f"user的輸入紀錄：{q1_record}，最小值為{q1_min_num}")


# ### 題目二 ###
# # 使用者任意輸入數字，一旦輸入值為9999則結束
# # 並找出其所輸入的最小值，並輸出
# q2_min_num = 0
# q2_record = ""

# while True:
#     user_input = input("Q2. 請輸入數字")
#     q2_min_num = int(user_input) if q2_record == "" else q2_min_num
#     q2_record = q2_record + user_input + " "

#     if int(user_input) == 9999:
#         break
#     else:
#         q2_min_num = int(user_input) if (q2_min_num > int(user_input)) else q2_min_num

# print(f"user的輸入紀錄：{q2_record}，最小值為{q2_min_num}")


### 題目三 ###
# 由使用者輸入兩個正整數a、b，且a需小於b
# 輸出從a到b(包含a 、b)之間4或9的倍數(一列輸出10個數字，欄寬為4、靠左對齊)。
# 輸出4或9的倍數共有幾個數
# 輸出4或9的倍數加總和
q3_num1 = input("Q3. 請輸入第一個正整數")
q3_num2 = input("Q3. 請輸入第二個正整數(需大於第一個數字)")
q3_record_muti49 = ""
q3_total = 0

if isPositiveInt(q3_num1) and isPositiveInt(q3_num2) and (q3_num2 > q3_num1):
    q3_num1 = int(q3_num1)
    q3_num2 = int(q3_num2)
    valid_count = 0

    for idx, item in enumerate(range(q3_num1, q3_num2 + 1)):
        if item % 4 == 0 or item % 9 == 0:
            q3_record_muti49 = q3_record_muti49 + str(item) + " "
            q3_total = q3_total + item
            valid_count += 1

            if idx + 1 % 10 == 0:
                q3_record_muti49 = q3_record_muti49 + "\n"

else:
    print("輸入格式錯誤! 請重新輸入!")


print(
    f"""
       1. 第一個正整數{q3_num1}，第二個正整數{q3_num2}
       2. 4或9倍數為：
       {q3_record_muti49}
       3. 共有{valid_count}個
       4. 總和為
      """
)
