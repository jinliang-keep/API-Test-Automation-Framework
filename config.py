import os
from dotenv import load_dotenv
load_dotenv()

# 环境基准地址
BASE_URL = "http://192.168.10.131:8888/api/private/v1"

# excel格式的测试用例文件配置
EXCEL_FILE = "./data/测试用例完整版.xlsx"
SHEET_NAME = "Sheet1"

# mysql配置
DB_HOST = os.getenv("DB_HOST", "")
DB_PORT = int(os.getenv("DB_PORT", "3306"))
DB_NAME = os.getenv("DB_NAME", "")
DB_USER = os.getenv("DB_USER", "")
DB_PASSWORD = os.getenv("DB_PASSWORD", "")


# mysql资源销毁
SQL1 = 'delete from sp_category where cat_name = "大码女装"'
SQL2 = 'delete from sp_attribute where cat_name = "VIP尺码"'
SQL3 = 'delete from sp_goods where goods_name = "大码牛仔裤"'