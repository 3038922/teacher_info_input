import openpyxl  # excel操作模块


class getData:

    def __init__(self, path):
        wb = openpyxl.load_workbook(path)

        # 读取表格
