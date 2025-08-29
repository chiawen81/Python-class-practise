### 共用程式
################################################
import random

#
#
#

# ### break
# ################################################
# """
# 1. 用途：迴圈內使用break敘述時，迴圈會立即中止
# 2. 應用：將迴圈設為無窮迴圈，在迴圈內判斷符合特定條件時用break終止迴圈
# """

# ### 題目一 ###
# # 當使用者輸入「end」，終止執行

# while True:
#     user_text = input("請輸入文字")

#     if user_text == "end":
#         print("===== end =====")
#         break


# ### 題目二 ###
# # 以亂數產生器產生兩個數，請user輸入兩數之合，若答錯將繼續作答，反之則結束。
# n1 = random.randint(1, 100)
# n2 = random.randint(1, 100)

# while True:
#     answer = input(f"{n1} + {n2} 為多少?")
#     if int(answer) == n1 + n2:
#         print("答對!")
#         break
#     else:
#         print("答錯! 請更正答案!")


# ### 題目三 ###
# # 隨機產生一組四則運算式，計算n1與n2的結果
# # 減法不得產生負數，除法取到小數點第2位數
# # 請user輸入結果，若答錯將繼續作答，反之則結束。
# q3_n1 = random.randint(1, 100)
# q3_n2 = random.randint(1, 100)
# idx = random.randint(0, 3)
# operator = ["+", "-", "×", "÷"][idx]
# print(q3_n1, q3_n2, operator)


# # 取得答案
# def GetUserAns(q3_n1, q3_n2, operator):
#     q3_answer = 0

#     if operator == "+":
#         q3_answer = q3_n1 + q3_n2
#     elif operator == "-":
#         q3_answer = q3_n1 - q3_n2
#     elif operator == "×":
#         q3_answer = q3_n1 * q3_n2
#     else:
#         q3_answer = q3_n1 / q3_n2
#         q3_answer = round(q3_answer, 2)

#     return q3_answer


# # 跑迴圈
# while True:
#     q3_answer = GetUserAns(q3_n1, q3_n2, operator)

#     if q3_answer > 0:
#         # 問題
#         q3_user_answer = float(input(f"Q3. 請輸入 {q3_n1} {operator} {q3_n2} 為多少?"))

#         # 檢核使用者的答案
#         if q3_answer == q3_user_answer:
#             print("答對!")
#             break
#         else:
#             print("答錯! 請更正答案!")

# #
# #
# #

### continue
################################################
"""
1. 用途：當執行到 continue 時，會跳過這一輪剩下的程式碼，直接進入下一輪的迴圈。
"""

### 題目一 ###
# 列出從1 到15的數，但排除5的倍數，再將顯示出來的數相加
q4_record_str = ""
q4_total = 0

for item in range(1, 16):
    if item % 5 == 0:
        continue

    q4_record_str = q4_record_str + str(item) + " "
    q4_total += item

print(
    f""" 1-15 中，非 5 的倍數有：{q4_record_str}
 其總和為：{q4_total}
      """
)
