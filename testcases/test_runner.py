import logging
import allure
import jsonpath
import pymysql
import pytest
import requests

from utils.analyse_case import analyse_case
from utils.asserts import http_assert, jdbc_assert
from utils.excel_utils import read_excel
from jinja2 import Template
from utils.allure_utils import allure_init
from utils.extractor import json_extractor, jdbc_extractor
from utils.send_request import send_http_request, send_jdbc_request


class TestRunner:

    data = read_excel()

    #保存全局变量
    global_data = {}

    @pytest.mark.parametrize("case", data)
    def test_case(self, case):

        global_data = self.global_data

        # 引用全局变量
        case = eval(Template(str(case)).render(global_data))

        # 初始化allure报告
        allure_init(case)

        # 0、测试用例的描述信息日志
        logging.info(f"0.用例ID:{case["id"]} 模块：{case["feature"]} 场景：{case["story"]} 标题：{case["title"]}")

        # 核心步骤1：解析请求数据
        request_data = analyse_case(case)

        # 核心步骤2：发送请求
        res = send_http_request(request_data)

        # 核心步骤3：断言
        # HTTP响应断言
        http_assert(case, res)

        # sql断言
        jdbc_assert(case)

        # 核心步骤4：提取
        # json提取
        json_extractor(case, res, global_data)

        # 数据库提取
        jdbc_extractor(case, global_data)