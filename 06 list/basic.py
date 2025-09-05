# 基本語法
# cp1:使用list指令將元組創建為串列
cp1_list = list((1, 2, 3, 4, 5))
print(cp1_list)


# cp2:切片
"""基本寫法：
your_list[start:end:step]

1. **start**：開始的索引（包含這個位置）
2. **end**：結束的索引（不包含這個位置）
3. **step**：步進（每次跳幾格，預設是 `1`）
"""
cp2_list = ["A", "B", "C", "D", "E"]
print(cp2_list[2:])  # 從索引值2到最後
print(cp2_list[:2])  # 從頭到索引值2(不含索引值本人)
print(cp2_list[2:4])  # 相當於js的slice
print(cp2_list[::-1])  # 相當於反轉該串列
print(cp2_list[4:0:-2])  # 相當於反轉後，每個兩個取值
# 輸出結果：['E', 'C']
print(cp2_list[4::-2])  # 相當於反轉後，每個兩個取值
# 輸出結果：['E', 'C', 'A']
