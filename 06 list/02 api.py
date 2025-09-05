# 共用程式碼
##################################################
import re

list_ex1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# 判斷是否為正整數
def isPositiveInt(str):
    return re.fullmatch(r"[1-9]\d*", str) is not None


# 常用語法
##################################################
# cp1：append()
# 用途：在串列的最後面插入元素
# 基本寫法：list_example.(<要插入的元素>)
list_ex1.append("end")
print(f"cp1. 在最後面加入元素：{list_ex1}")


# cp2：insert()
# 用途：在串列的特定位置插入元素
# 基本寫法：list_example.insert(<插入的索引值>,<要插入的元素>)
list_ex1.insert(0, "start")
print(f"cp2. 在最前面加入元素：{list_ex1}")


# cp3：pop()
# 用途：刪除串列元素
# 基本寫法：
# 1. 刪除串列最後一個元素：list_ex.pop()
# 2. 刪除串立中特定位置的元素：
list_ex1.pop()
list_ex1.pop(1)
print("cp3", list_ex1)


# cp4：remove()
# 用途：刪除串列中第一個符合某值的元素
# 基本寫法：list_example.remove(<某值>)
list_ex1.remove(5)
print("cp4", list_ex1)


# cp5：count()
# 用途：計算某值在串列裡出現的次數
# 基本寫法：list_example.count(<某值>)
list_ex2 = ["a", "b", "b", "c", "c", "c"]
print(f"cp5. b出現的次數為 {list_ex2.count("b")} 次")
print(f"cp5. z出現的次數為 {list_ex2.count("z")} 次")


# cp6：index()
# 用途：回傳第一個某元素所在的位置(索引值)
# 基本寫法：list_example.index(<某元素>)
print(f"cp6. b第一次出現的索引值為 {list_ex2.index("b")}")
# print(f"cp6. z第一次出現的索引值為 {list_ex2.index("z")}")
# ps. 如果沒有該元素的話會報錯


# cp7：sort()
# 用途：將串列的各數值作升冪排列
# 基本寫法：list_example.sort()
list_ex3 = [5, 4, 2, 8, 132, 3, 22, 55, 4, 5, 2]
list_ex3.sort()
print(f"cp7. 升冪排列：{list_ex3}")

# cp8：reverse()
# 用途：將串列的各數值
# 基本寫法：
list_ex3.reverse()
print(f"cp8. 降冪排列:{list_ex3}")
