# ### 巢狀迴圈(nested loop)
# for outsideIdx in range(1, 4):
#     print(f"外層迴圈第{outsideIdx}圈")

#     for insideIdx in range(1, 7):
#         print(f"內層第{insideIdx}圈")


### 列印出九九乘法表
for firstNum in range(1, 10):
    for secondNum in range(1, 10):
        if secondNum == 1:
            print("==========我是分隔線===========")

        print(f"{firstNum}*{secondNum}={firstNum*secondNum}")
