import openpyxl
from config import EXCEL_FILE, SHEET_NAME


def read_excel():

    # 打开excel文件
    workbook = openpyxl.load_workbook(EXCEL_FILE)

    # 选择表
    worksheet = workbook[SHEET_NAME]

    data = []
    # 取表头
    keys = [cell.value for cell in worksheet[2]]
    # 取数据
    for row in worksheet.iter_rows(min_row=3, values_only=True):
        dict_data = dict(zip(keys, row))
        if dict_data["is_true"]:
            data.append(dict_data)

    # 关闭文件
    workbook.close()

    return data