import random

### 定數迴圈（Count-controlled）
##########################################
"""
定義：
在迴圈開始前，可計算出執行次數（可能是固定常數，或可由輸入 n 算出）。
"""
# 產生60個亂數(範圍1-49)，每6個一列，排成6*10的矩形格式
combine_str = ""

for i in range(60):
    num = random.randint(1, 49)
    combine_str = combine_str + str(num) + " "
    if (i + 1) % 6 == 0:
        combine_str = combine_str + "\n"

print(
    f"""定數迴圈
      {combine_str}"""
)
#
#
#
### 不定數迴圈（Event/Condition-controlled）
##########################################
"""
定義：
無法在一開始就知道會跑幾次，結束取決於某個事件／條件何時成立（資料內容、使用者輸入、IO 狀態、隨機等）。
"""
# 請使用 while 迴圈，每次產生一個 1～10 的亂數，一直重複下去，直到「第一次產生出 7」為止就停止，並印出總共試了幾次。
num_cache = 0
try_count = 0
num_record = ""

while num_cache != 7:
    try_count += 1
    num = random.randint(1, 10)
    num_cache = num
    num_record = num_record + str(num) + " "

print(
    f"""不定數迴圈
      嘗試了第{try_count}次
      歷史紀錄：{num_record}
      """
)
