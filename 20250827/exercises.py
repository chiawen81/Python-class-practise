#########################
# 題目來源：
# https://docs.google.com/document/d/1IGsSwwHXx2twSJKaDlN7zLnArKCchKly/edit
#########################

#########################
# 共用程式碼
#########################
import re


# 判斷是否為正整數
def isPositiveInt(str):
    return re.fullmatch(r"[1-9]\d*", str) is not None


# 排序大小
def sortNum(numAry, isDsc=False):
    new_nums = sorted(numAry, reverse=isDsc)
    return new_nums


#########################
# 題目
#########################
# ### 1. 使用者輸入任意兩個正整數，算出二者之間的總合
# import re

# q1_firstNum = input("Q1. 請輸入第一個數字")
# q1_secondNum = input("Q1. 請輸入第二個數字")
# q1_total = 0

# # 驗證須為正整數
# if isPositiveInt(q1_firstNum) and isPositiveInt(q1_secondNum):
#     # 排序大小
#     new_numAry = sortNum([q1_firstNum, q1_secondNum])

#     # 計算兩數之間的加總
#     for item in range(int(new_numAry[0]), int(new_numAry[1]) + 1):
#         q1_total += item
#     print(f"兩數總和為{q1_total}")

# else:
#     print("發生錯誤，需傳入正整數~!")


# ### 2. 使用者輸入任意兩個正整數，算出二者之間的「偶數總合」
# q2_firstNum = input("Q2. 請輸入第一個數字")
# q2_secondNum = input("Q2. 請輸入第二個數字")
# q2_total = 0

# # 驗證須為正整數
# if isPositiveInt(q2_firstNum) and isPositiveInt(q2_secondNum):
#     # 排序大小
#     new_numAry = sortNum([q2_firstNum, q2_secondNum])

#     # 計算兩數之間的偶數加總
#     for item in range(int(new_numAry[0]), int(new_numAry[1]) + 1):
#         if item % 2 == 0:
#             q2_total += item
#     print(f"Q2. 兩數之間的偶數總和為{q2_total}")

# else:
#     print("發生錯誤，需傳入正整數~!")


### 3.


# ### 4. 計算1到任意數之間，5的倍數的總合
# q4_num = input("Q4. 請輸入任意一個正整數")
# q4_total = 0
# # 驗證是正整數
# if isPositiveInt(q4_num):
#     # 跑迴圈
#     for item in range(1, int(q4_num) + 1):
#         if item % 5 == 0:
#             q4_total += item
#     print(f"Q2. 兩數之間的偶數總和為{q4_total}")
# else:
#     print("發生錯誤，需傳入正整數~!")


# # 5. 利用「%」、「//」求得反轉的數字（ex:12345→54321）
# user_input = input("Q5. 請輸入任意一個正整數: ")
# reversed_str = ""

# # 驗證是正整數
# if isPositiveInt(user_input):
#     num = int(user_input)
#     digit_count = len(user_input)

#     for i in range(1, digit_count + 1):
#         print(f"第{i}圈，目前數字是 {num}")
#         digit = num % 10
#         print(f"正在處理的位數是 {digit}")
#         reversed_str += str(digit)
#         print(f"新字串是 {reversed_str}")
#         num //= 10
#         print(f"下個迴圈要處理的數字是 {num} --------")

# else:
#     print("發生錯誤，需傳入正整數~!")


# 6. 輸入一個正整數，求n!值
# q6_num = input("Q6. 請輸入任意正整數求n!")
# total = 1

# # 驗證是正整數
# if isPositiveInt(q6_num):
#     q6_num = int(q6_num)

#     for item in range(1, q6_num + 1):
#         total = total * item


# else:
#     print("發生錯誤，需傳入正整數~!")

# print(f"Q6. {q6_num}! 為 {total}")
