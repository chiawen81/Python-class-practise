# 基本語法
##################################################
'''
1. 元組的元素值不能改變
2. 無法刪除或更改個別資料，但可以整個覆蓋或刪除
3. 沒有內建的加入API，但可以利用"+"把元素加入元組 
   或是利用"*"複製元素
'''
###### 1. 元組型別 ######
########################
tuple1=(2,4,1,3,9,5)
print(tuple1)
# Output:(2, 4, 1, 3, 9, 5)


###### 2. 全部覆寫以改變值 ######
################################
tuple1=(2,4)
print(tuple1)
# Output:(2, 4)


'''
增加一個元素時後面加逗號 例如：
tuple1+=(1,)
'''
###### 3. 利用+相加群組 ######
#############################
tuple1+=(1,)
print(tuple1)
# Output:(2, 4, 1)
tuple1=tuple1+(2,4)
print(tuple1)
# Output:(2, 4, 1, 2, 4)


###### 4. 從串列中建立元組 ######
################################
tuple4=tuple([i for i in range(1,6)])
print(tuple4)
# Output:(1, 2, 3, 4, 5)


###### 5. 字串型別的元組 ######
##############################
tuple5=('python')
print(tuple5)
# Output:python
tuple5=tuple(tuple5)
print(tuple5)
# Output:('p', 'y', 't', 'h', 'o', 'n')


###### 6. 可以用的串列API ######
###############################
# len、max 、min、sum、in、not in、*、+ 
tuplt6=(1,2,3,4,5,6,7,8,9,10)
print(len(tuplt6))   # Output:10
print(max(tuplt6))   # Output:10
print(min(tuplt6))   # Output:1
print(1 in tuplt6)   # Output:True
print(5 not in tuplt6)   # Output:False


######### 7. 索引取值 #########
##############################
tuple7=(1,2,3,4,5)
print(tuple7[2])    # Output:3
print(tuple7[1:3])   # Output:(2,3)


###### 8. 利用*複製群組 ######
#############################
tuple8=(1,2,3)
print(tuple8*2)    # Output:(1, 2, 3, 1, 2, 3)


###### 9. 搭配迴圈應用 ######
############################
tuple9=(1,2,3,4,5,7,8,9)
for i in tuple9:
    print(i)
# Output:
# 1
# 2
# 3
# 4
# 5
# 7
# 8
# 9


###### 9. 刪除整組元組 ######
############################
del tuple9
print(tuple9)
# output:
# NameError: name 'tuple9' is not defined. Did you mean: 'tuple1'?