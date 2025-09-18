# 基本語法：字典(dictionary)
##################################################
'''NOTE:
1. 形式：
    - 以大括號括起來，由一或多個數對組成
    - 一組數對由(key)與數值(value)組成
2. 和JS物件的差異：
    - 鍵的類型：
      Python的鍵值可雜湊，JS只能是字串或symbol
    - 順序行為：
      Python字典輸出時，數對是按插入順序呈現；JS是按整數索引>字串>symbol
    - 原型鏈影響：
      JS會繼承原型鏈(prototype chain)上的方法；Python不會有額外屬性
'''

###### 1. 資料形式 ######
########################
dict1A={}
print(dict1A)     
#Output:{}

dict1B={
    "Taipei":"101",
    ("x", "y"): 100,
    42:"Hi",
    "1":{},
    "2":[1,2,3,4],
    "3":True
}
print(dict1B)
#Output:
# {'Taipei': '101', ('x', 'y'): 100, 42: 'Hi', '1': {}, '2': [1, 2, 3, 4], '3': True}
'''NOTE:
相較於JS只能接受將字串與symbol為型別的鍵值，Python可接受雜湊型別的鍵值
'''


###### 2. 新增鍵值進dict ######
##############################
dict2={"Eric":30}
dict2["Anna"]=18
print(dict2)
#Output:{'Eric': 30, 'Anna': 18}


###### 3. 搭配迴圈應用 ######
############################
for i in dict1B:
    print(i,dict1B[i])
# Output:
# Taipei 101
# ('x', 'y') 100
# 42 Hi
# 1 {}
# 2 [1, 2, 3, 4]
# 3 True


###### 4. 排順序 ######
######################
dict4={4:123,2:123,100:123}
list4=sorted(dict4)
print(list4)
# Output:[2, 4, 100]
'''NOTE:
    可使用串列的排序方法sorted，但型別也會轉成串列
'''


###### 5. 其他常用的API ######
#############################
'''
NOTE:
有 len、max 、min、sum、in、not in
'''
dict5={"1":1,"2":2,"3":3}
print(len(dict1B))   # Output:6
print(max(dict5))   # Output:3
print(min(dict5))   # Output:1
print("Taipei" in dict1B)   # Output:True
print("New Taipei" not in dict1B)   # Output:True



###### 6. 比較運算子 ######
##########################
'''NOTE:可用「==」 、「 !=」等比較運算子
'''
dict6A={"Eric":22,"Anna":6}
dict6B={"Tom":23}
dict6C={"Eric":22}
dict6D={"Eric":22}
print(dict6A==dict6B)   # Output:False
print(dict6C==dict6D)   # Output:True
print(dict1A!=dict6C)   # Output:True
print(dict6A["Eric"]==dict6C["Eric"])   # Output:True


###### 7-1. 刪除：del ######
###########################
'''NOTE:刪除單一鍵值'''
dict7A={
    "Taipei":"101",
    ("x", "y"): 100,
    42:"Hi",
}
del dict7A[42]
print(dict7A)   # Output:{'Taipei': '101', ('x', 'y'): 100}

'''NOTE:刪除整個dict'''
# del dict7
# print(dict7)
# Output:
# NameError: name 'dict7' is not defined. Did you mean: 'dict2'?
'''NOTE:因為dict被刪除了，所以會報「not defined」的錯誤
'''


###### 7-2. 刪除：pop()、popitem()、clear() ######
#################################################
'''NOTE:
    利用pop()，刪除某一數對
'''
dict7B={
    "Taipei":"101",
    ("x", "y"): 100,
    42:"Hi",
}
dict7B.pop(42)
print('pop()後的值：',dict7B)
# Output:
# pop()後的值： {'Taipei': '101', ('x', 'y'): 100}

'''NOTE:
    利用popitem()，刪除最後一個數對
'''
dict7B.popitem()
print(dict7B)
# Output:
# {'Taipei': '101'}

'''NOTE:
    利用clear()，清空所有數對(變成空dict)
'''
dict7B.clear()
print(dict7B)
# Output:
# {}


###### 8. 取得所有key、vlaue ######
##################################
'NOTE:取得所有key'
print(dict1B.keys())   
# Output:
# dict_keys(['Taipei', ('x', 'y'), 42, '1', '2', '3']) 

'NOTE:取得所有vlaue'
print(dict1B.values())   
# Output:
# dict_values(['101', 100, 'Hi', {}, [1, 2, 3, 4], True])

'NOTE:取得所數對'
print(dict1B.items())  
# Output:
# dict_items([('Taipei', '101'), (('x', 'y'), 100), (42, 'Hi'), ('1', {}), ('2', [1, 2, 3, 4]), ('3', True)])
'''NOTE:
    1. 透過這三個API所吐出來的資料不是串列（list），而是 「視圖物件」（view objects）。
    2. 視圖物件」（view objects）可用for迴圈
'''


###### 9. 複製與合併 ######
##########################
dic9A = {1:'rad',2:'Yellow',3:'Green'}
dic9B = {4:'black',1:'Blue'}
'''NOTE:
    利用copy()，進行複製
    ps. 此為「淺拷貝」
'''
dic9C = dic9A.copy()
print(dic9C)
# Output:
# {1: 'rad', 2: 'Yellow', 3: 'Green'}

'''NOTE:
    利用update()，進行合併
    ps. 當兩者有鍵值相同時，被合併(後者)的值會覆蓋前者
'''
dic9A.update(dic9B)
print(dic9A)
# Output:
# {1: 'Blue', 2: 'Yellow', 3: 'Green', 4: 'black'} 