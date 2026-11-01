# API Test Automation Framework

基于 Python + pytest + Requests + PyMySQL + Allure 搭建的接口自动化测试框架。
采用 **Excel 数据驱动**，将测试数据与测试代码分离；封装了请求发送、用例解析、参数提取、HTTP/SQL 双断言和 Allure 报告生成，用于练习接口自动化测试的完整流程。

> 被测接口服务部署在本地虚拟机中，未包含在本仓库内。运行测试前需自行启动被测服务。

## 技术栈

- Python 3.x
- pytest（测试运行、参数化）
- Requests（HTTP 请求）
- PyMySQL（数据库断言）
- Allure（测试报告）
- openpyxl（读取 Excel 测试用例）

## 框架结构
```text
├── data/                  # Excel 测试用例文件
├── testcases/
│   └── test_runner.py     # 统一用例执行入口，读取 Excel 并参数化执行
├── utils/
│   ├── analyse_case.py    # 解析用例数据，组装请求参数
│   ├── send_request.py    # 封装 HTTP 请求发送与数据库查询
│   ├── asserts.py         # HTTP 响应断言 + 数据库断言
│   ├── extractor.py       # 从响应中提取 token 等变量，供后续用例使用
│   ├── excel_utils.py     # Excel 用例读取
│   └── allure_utils.py    # Allure 报告步骤与描述初始化
├── config.py              # 读取环境变量配置
├── conftest.py            # pytest fixture / 全局配置
├── pytest.ini             # pytest 运行配置
├── requirements.txt
└── .env.example           # 环境变量模板（真实 .env 不上传）
```

## 核心能力

- **Excel 数据驱动**：测试用例写在 `data/测试用例完整版.xlsx` 中，`test_runner.py` 读取后通过 `pytest.mark.parametrize` 逐条执行，新增用例只需改 Excel，不改代码。
- **参数提取与关联**：登录用例成功后，`extractor.py` 从响应中提取 token 写入全局变量，后续用例通过模板引用该变量，实现接口间的依赖传递。
- **HTTP + 数据库双断言**：`asserts.py` 同时支持对响应 JSON 做 JSONPath 断言，以及对数据库执行 SQL 校验，覆盖“接口返回正确”和“数据落库正确”两层。
- **Allure 报告**：每个用例的执行步骤、请求数据、响应文本和断言结果都会输出到 Allure 报告，便于定位失败原因。
- **敏感信息隔离**：数据库连接和接口地址通过 `.env` 管理，仓库中只保留 `.env.example` 占位模板。
