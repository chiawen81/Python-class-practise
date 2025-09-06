####################################################################################################
#  語法練習：串列
#  講義來源：https://docs.google.com/document/d/1RyNQFOkhgpnxqpBctsN1txDgIGqQnyKD/edit?usp=sharing&ouid=113073999793927873424&rtpof=true&sd=true
####################################################################################################


# 共用程式碼
##################################################
import re


# 判斷是否為正整數
def isPositiveInt(str):
    return re.fullmatch(r"[1-9]\d*", str) is not None


##################################################
### 題目一 ###
# 使用隨機方式產生樂透號碼 6個數字(1~49)，並存放入串列中，印出結果
import random


def get_lotto():
    lotto = []
    for item in range(6):
        num = random.randint(1, 49)
        lotto.append(num)
    return lotto


print(f"Q1. 取得樂透號碼{get_lotto()}")


### 題目二 ###
# 承上，上述產生的樂透號碼不可重複
def get_lotto_without_same():
    lotto = []

    for item in range(6):
        while True:
            num = random.randint(1, 49)

            if num not in lotto:
                lotto.append(num)
                break

    return lotto


print(f"Q2. 取得不重複的樂透號碼{get_lotto_without_same()}")


### 題目三 ###
# 人工輸入12個正整數，存入串列，排序後輸出結果

# Step1：取得user輸入的字串，並要求user以","分隔這12個正整數
original_data = input("Q3. 請輸入12個正整數，並以','號區隔")


# Step2：將這12個正整數裝進陣列裡
def trans_data_to_list():
    new_list = []

    if "," in original_data:
        new_list = original_data.split(",")

    return new_list


# Step3：驗證並轉成陣列包數字
def trans_int(list_str):
    new_list = []

    # 驗證：使用者有輸入12個數字
    if len(list_str) == 12:
        new_list = [int(item) for item in list_str if isPositiveInt(item)]

    return new_list


# 主程式
def get_list():
    list_str = trans_data_to_list()
    # print(f"取得陣列：{list_str}")

    list_num = trans_int(list_str)
    # print(f"取得轉成數字後的陣列：{list_num}")

    new_list = list_num.sort() if (len(list_num) == 12) else []
    # print(f"取得排列後的陣列：{  list_num}")

    return new_list


print(f"main-取得排列後的陣列：{get_list()}")
