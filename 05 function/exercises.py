####################################################################################################
#  語法練習：函式
#  講義來源：https://docs.google.com/document/d/1IdFIbR6MfRiY2Hcr0R9VM1uK8cnONpqE/edit?usp=sharing&ouid=113073999793927873424&rtpof=true&sd=true
####################################################################################################


# 共用程式碼
##################################################
import re


# 判斷是否為正整數
def isPositiveInt(str):
    return re.fullmatch(r"[1-9]\d*", str) is not None


# 題目
##################################################
# ### 題目一 ###
# 讓使用者輸入學號、姓名、科系，透過呼叫顯示這些訊息。

# stu_no = input("Q1. 請輸入學號")
# stu_name = input("Q1. 請輸入姓名")
# stu_major = input("Q1. 請輸入科系")


# def compute(stu_no, stu_name, stu_major):
#     print(
#         f"""Q1. 顯示學生訊息:
#           學號：{stu_no}
#           姓名：{stu_name}
#           科系：{stu_major}
#           """
#     )


# compute(stu_no, stu_name, stu_major)


# ### 題目二 ###
# # 讓使用者輸入2個數字做為參數，透過呼叫函式，回傳(return x*y)的乘積。

# q2_num1 = input("Q2. 請輸入第一個數字")
# q2_num2 = input("Q2. 請輸入第二個數字")


# def multiply(num1, num2):
#     if isPositiveInt(num1) and isPositiveInt(num2):
#         return int(num1) * int(num2)
#     else:
#         return None


# result = multiply(q2_num1, q2_num2)
# q2_answer = result if result else "格式有誤，請重新輸入"

# print(q2_answer)


# ### 題目三 ###
# # 讓使用者輸入2個整數，讓函數回傳這兩個整數連續加總的結果
# q3_num1 = input("Q3. 請輸入第一個數字")
# q3_num2 = input("Q3. 請輸入第二個數字")


# def sum_range(num1, num2):
#     total = 0  # 清空
#     if isPositiveInt(num1) and isPositiveInt(num2):
#         num1, num2 = int(num1), int(num2)  # 此為簡化寫法

#         for idx, item in enumerate(range(num1, num2 + 1)):
#             total = total + item
#     return total


# def print_sum_range(num1, num2):
#     sum_range_result = sum_range(num1, num2)
#     text = (
#         f"{num1}至{num2}之間的加總為{sum_range_result}"
#         if sum_range_result
#         else "格式有誤，請重新輸入數字"
#     )

#     return text


# print(print_sum_range(q3_num1, q3_num2))


# ### 題目四 ###
# # 使用者傳2個參數給函數，讓函數回傳「x的y次方」的值
# q4_num1 = input("Q4. 請輸入第一個數字")
# q4_num2 = input("Q4. 請輸入第二個數字")


# def print_square_num(ori_num, square_num):
#     text = ""

#     if isPositiveInt(ori_num) and isPositiveInt(square_num):
#         ori_num, square_num = int(ori_num), int(square_num)
#         answer = ori_num**square_num
#         text = f"{ori_num}的{square_num}次方為{answer}"
#     else:
#         text = "格式有誤，請重新輸入!"

#     return text


# print(print_square_num(q4_num1, q4_num2))


# ### 題目五 ###
# # 建立一個函式compute(a,x,y) 使用者輸入3個參數：a (字元)、x(個數)、y(列數)，印出 y列 x個的a字元。
# q5_char = input("Q5. 請輸入一個字元")
# q5_row = input("Q5. 請輸入要產生幾列")
# q5_per_row_create_num = input(f"Q5. 請輸入每列要產生幾個「{q5_char}」")


# # 每列產生的文案
# def create_per_row_text(per_row_create_num, char):
#     per_row_text = ""

#     for item in range(per_row_create_num):
#         per_row_text = per_row_text + char

#     return per_row_text


# # 組合每列文字
# def get_final_text(row_num, per_row_text):
#     final_text = ""

#     for idx, item in enumerate(range(row_num)):
#         final_text = final_text + per_row_text

#         if idx != row_num - 1:
#             final_text = final_text + "\n"

#     return final_text


# # 主程式
# def get_text(char, row_num, per_row_create_num):
#     if isPositiveInt(row_num) and isPositiveInt(per_row_create_num):
#         row_num, per_row_create_num = int(row_num), int(per_row_create_num)
#         per_row_text = create_per_row_text(per_row_create_num, char)
#         final_text = get_final_text(row_num, per_row_text)
#     else:
#         print("格式錯誤，請重新輸入")

#     return final_text


# print(
#     f"""最終產生的文案：
# {get_text(q5_char, q5_row, q5_per_row_create_num)}"""
# )


# ### 題目六 ###
# # 撰寫圓面積、長方形面積、三角形面積函式，透過輸入圓形半徑、長方形長、寬，三角形底和高，計算並輸出三個圖形面積與三個面積和。
# import math

# circle_radius = input("Q6. 請輸入辦圓形半徑")
# rectangle_length = input("Q6. 請輸入長方形的長")
# rectangle_width = input("Q6. 請輸入長方形的寬")
# triangle_length = input("Q6. 請輸入三角形的底")
# rectangle_height = input("Q6. 請輸入三角形的高")


# # 取得圓形面積
# def get_circle_area(radius):
#     if isPositiveInt(radius):
#         radius = int(radius)
#         return int(radius) ** 2 * math.pi


# # 取得長方形面積
# def get_rectangle_area(length, width):
#     if isPositiveInt(length) and isPositiveInt(width):
#         length, width = int(length), int(width)
#         return length * width


# # 取得三角形面積
# def get_triangle_area(length, height):
#     if isPositiveInt(length) and isPositiveInt(height):
#         length, height = int(length), int(height)
#         return length * height / 2


# # 取得面積總和
# def get_total_area(circle_area, rectangle_area, triangle_area):
#     return circle_area + rectangle_area + triangle_area


# circle_area = get_circle_area(circle_radius)
# rectangle_area = get_rectangle_area(rectangle_length, rectangle_width)
# triangle_area = get_triangle_area(triangle_length, rectangle_height)

# print(
#     f"""
# 圓形面積：{circle_area}
# 長方形面積：{rectangle_area}
# 三角形面積：{triangle_area}
# 總和面積：{get_total_area(circle_area,rectangle_area,triangle_area)}
#       """
# )


### 題目七 ###
# 輸入2個正整數x,y，傳入最大公因數函式內，函式回傳最大公因數計算結果


### 題目八 ###
# 某市區停車場車位不足，為鼓勵車輛提早移出，進行如下規範：
# (a). 2小時以內(含2小時)，每小時以30元計算
# (b). 2小時以上到4小時(含4小時)，每小時以50元計算
# (c). 4小時以上到6小時(含6小時)，每小時以80元計算
# (d). 6小時以上，每小時以100元計算
# 請撰寫程式輸入停車時數，傳入函數參數內，函數傳回停車費計算結果。


### 題目九 ###
# 使用函數撰寫骰子比大小程式，先由電腦模擬投擲三個骰子和，再由使用者輸入一個值(自訂)模擬投擲動作，透過亂數產生三個骰子和，並和電腦輸出結果比大小，印出"你贏了"或"你輸了"。
