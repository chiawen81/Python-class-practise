### elif
"""
其實就是 if...else 的縮寫
"""
a=int(input("請輸入數字:"))
if a>0:
    if a==100:
        print("考滿分")
    elif a>=60:
        print("""及格
          ps.這裡進到elif!
          """)
        if a>=90:
            print("太優秀了!")
    
    elif a<60:
        print("不及格")
    
else:
    print("缺考")