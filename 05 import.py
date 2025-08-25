# import
# 1. 用途：
#    (1) 將其他 Python 檔案或模組的功能引入到
#    (2) 匯入模組的基本語法：
#       - import 模組名稱
#       - from 模組名稱 import 函式名稱
# 2. 常用的模組：
#       os：與作業系統互動（檔案、目錄等）
#       sys：Python 直譯器相關功能
#       math：數學運算
#       datetime：日期與時間處理
#       random：隨機數產生
#       re：正則表達式
#       json：JSON 資料處理
#       csv：CSV 檔案處理
#       collections：進階資料結構（如 Counter, defaultdict）
#       itertools：高效能迭代工具
#       requests：HTTP 請求（需安裝）
#       pandas：資料分析（需安裝）
#       numpy：數值運算（需安裝）


# 模組<數學運算>：計算圓的面積
import math
radius = 5 # 假設半徑為5
area = math.pi * radius**2 #此即為半徑的平方 乘以 圓周率(math.pi)
print(area)

# 模組<日期與時間處理>：獲取當前日期和時間
import datetime
nowTime = datetime.datetime.now()  
print(nowTime)