### 亂數產生器
import random

# seed()
# 用途：設定種子值，讓每次產生的隨機數字相同
# 寫法：seed(<寫法>)
random.seed(10)

# random()
# 用途：隨機產生0-1之間的浮點數
r = random.random()
print("r:", r)

# uniform()
# 用途：隨機產生某數之間的浮點數（本範例為1-50）
# 寫法：uniform(<起始值>,<終值>)
r_50 = random.uniform(1, 50)
print("r_50", r_50)
"""
random.uniform(0,1) 即為 random.random()
"""

# randint()
# 用途：隨機產生某樹之間的整數（本範例為1-50）
# 寫法：randint(<起始值>,<終值>)
r_50_int = random.randint(1, 50)  # 隨機產生0-50之間的整數
print(r_50_int)
print("r_50_int)", r_50_int)


# randrandge()
# 用途：隨機產生某數之間，符合條件的數字
# 寫法：randrange(<起始值>,<終值>,<間隔數>)
r_randrange = random.randrange(5, 31, 2)
print("r_randrange)", r_randrange)


# choice()
# 用途：產生某陣列中的任一數
r_choice = random.choice([1, 2, 3, 4, 5])
print("r_choices_specify", r_choice)


# choices()
# 用途：功能同choice()，但可以指定要產生幾個任意數(可能會重複)
# 寫法：choices(<某陣列>,k=<產出幾個數字>)
r_choices_specify = random.choices([5, 10, 15, 220, 25, 30], k=3)
print("r_choices_specify", r_choices_specify)


# sample()
# 用途：功能同choices()，但不會重複出現
r_choices_sample = random.sample([5, 10, 15, 220, 25, 30], k=3)
print("r_choices_sample", r_choices_sample)
