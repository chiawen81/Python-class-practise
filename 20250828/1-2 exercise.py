# 共用程式碼 #
########################
########################
import random


# 判斷倍數
def IsMuti(num, muti_num):
    return True if (num % muti_num == 0) else False


# 題目 #
########################
########################

### Q1. 使用亂數器產生10個亂數
q1_random_record = ""

for idx in range(10):
    r_int = random.randint(0, 100)
    q1_random_record = q1_random_record + str(r_int) + "   "

print("Q1. 使用亂數器產生10個亂數", q1_random_record)


#####################################################################
### Q2. 產生10個亂數，並判斷各有多少奇偶數
q2_random_record = ""
q2_random_even_count = 0
q2_random_odd_count = 0

for idx in range(10):
    num = random.randint(1, 100)
    if num % 2 == 0:
        q2_random_even_count += 1
    else:
        q2_random_odd_count += 1

    q2_random_record = q2_random_record + str(num) + "   "

print(
    f"""Q2.
      q2_random_record:{q2_random_record}
      奇數數量：{q2_random_odd_count}
      偶數數量：{q2_random_even_count}
      """
)


#####################################################################
### Q3. 產生100個亂數，判斷各有多少3、5、7的倍數，以及非3、5、7的倍數
q4_num_list = random.sample(range(1, 1001), 100)
muti3_count = 0
muti5_count = 0
muti7_count = 0
other_count = 0

# 跑迴圈
for itemIdx in range(100):
    miss = 0

    if IsMuti(q4_num_list[itemIdx], 3):
        muti5_count += 1
    else:
        miss += 1

    if IsMuti(q4_num_list[itemIdx], 5):
        muti5_count += 1
    else:
        miss += 1

    if IsMuti(q4_num_list[itemIdx], 7):
        muti7_count += 1
    else:
        miss += 1

    if miss == 3:
        other_count += 1

print(
    f"""Q3.
      3的倍數共有{muti3_count}個
      5的倍數共有{muti5_count}個
      7的倍數共有{muti7_count}個
      以上皆非共有{other_count}個
      """
)


#####################################################################
### Q4. 承上題，需計算出同為3與5的倍數、同為3與7的倍數、同為5與7的倍數、同為3/5/7的倍數、僅為3/5/7的倍數、以上皆非，讓總數相加為100
q4_num_list = random.sample(range(1, 1001), 100)
muti3_count = 0
muti5_count = 0
muti7_count = 0
muti35_count = 0
muti37_count = 0
muti57_count = 0
muti357_count = 0
other_count = 0

for idx in range(100):
    num = q4_num_list[idx]
    isMuti_3 = IsMuti(num, 3)
    isMuti_5 = IsMuti(num, 5)
    isMuti_7 = IsMuti(num, 7)

    if isMuti_3 and isMuti_5 and isMuti_7:
        muti357_count += 1
    elif isMuti_3 and isMuti_5:
        muti35_count += 1
    elif isMuti_3 and isMuti_7:
        muti37_count += 1
    elif isMuti_5 and isMuti_7:
        muti57_count += 1
    elif isMuti_3:
        muti3_count += 1
    elif isMuti_5:
        muti5_count += 1
    elif isMuti_7:
        muti7_count += 1
    else:
        other_count += 1

print(
    f"""Q4.
      僅為3的倍數：{muti3_count}
      僅為5的倍數：{muti5_count}
      僅為7的倍數：{muti7_count}
      3、5的倍數：{muti35_count}
      3、7的倍數：{muti37_count}
      5、7的倍數：{muti57_count}
      同為3/5/7的倍數：{muti357_count}
      以上皆非：{other_count }

"""
)
