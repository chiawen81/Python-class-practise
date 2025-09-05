############################################################
# ※特別聲明※                                              #
# 內建fn可用於所有可迭代的物件，非串列特有的語法               #
############################################################

"""
python裡，串列（list）有自己的串列方法
同時，python本身也有很多內建函式


<兩大類差異>
1. 串列方法（list methods）：
只能用在串列本身上，例如 .append()、.sort()。

2. 內建函式（built-in functions）：
可以作用在任何可迭代物件（list、tuple、set、dict…），例如 len()、max()。

"""

# 共用程式碼
##################################################
import re

test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# 判斷是否為正整數
def isPositiveInt(str):
    return re.fullmatch(r"[1-9]\d*", str) is not None


# 題目
##################################################
# cp1：len()
# 計算陣列的長度
print(f"CP1 串列長度為：{len(test_list)}")


# cp2：sum()、max()、min()
# 計算物件的加總、最大值、最小值
print(f"cp2 加總為{sum(test_list)}")
print(f"cp3 最大值為{max(test_list)}")
print(f"cp3 最小值為{min(test_list)}")


# cp3：sorted()

# cp4：enumerate()

# cp5：map(func, iterable)

# cp6：filter(func, iterable)
