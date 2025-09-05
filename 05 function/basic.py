####################################################################################################
#  語法練習：函式
#  講義來源：https://docs.google.com/document/d/1IdFIbR6MfRiY2Hcr0R9VM1uK8cnONpqE/edit?usp=sharing&ouid=113073999793927873424&rtpof=true&sd=true
####################################################################################################


### chp1：無回傳值 ###
def printNumber(starNum, endNum):
    for item in range(starNum, endNum + 1):
        print(item)


printNumber(1, 4)


### chp2：有回傳值 ###
user_input_num1 = int(input("chp2. 請輸入第一個回傳值"))
user_input_num2 = int(input("chp2. 請輸入第二個回傳值"))


def addNum(num1, num2):
    total = num1 + num2
    return total


print(f"總和為{addNum(user_input_num1, user_input_num2)}")


### chp3：預帶參數 ###
new_task_num = int(input("chp3 請輸入今天的任務數"))


def today_task_num(new_task_num, maintain_tack_num=2):
    return maintain_tack_num + new_task_num


print(f"今日任務總數為{today_task_num(new_task_num)}")
