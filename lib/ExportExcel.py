# -*- coding:  UTF-8 -*-

import openpyxl
from lib.MailSend import *


class ExportExcel:
    def __init__(self, file_path):
        # wb = load_workbook(file_path)
        # sheet_names = wb.get_sheet_names()  #
        # self.ws = wb.get_sheet_by_name(sheet_names[0])  # index为0为第一张表
        # 实例化对象excel对象
        self.file_path = file_path
        self.excel_obj = openpyxl.Workbook()

        # excel 内当前活跃的sheet工作表
        self.excel_obj_sheet = self.excel_obj.active
        # 给单元格赋值
        # excel_obj_sheet['A1'] = 4
        # excel_obj_sheet.append(["账号", "手机号", "设备号", "注册时间"])
        # excel_obj_sheet.append([1, 2, 3])
        # excel_obj_sheet.append([1, 2, 3])
        # excel_obj_sheet.append([1, 2, 3])
        # excel_obj_sheet.append([1, 2, 3])
        # excel_obj_sheet.append([1, 2, 3])
        # excel_obj_sheet['A3'] = datetime.datetime.now()

        # 文件保存
        # self.excel_obj.save(file_path)

    def __enter__(self):
        # return self.ws
        return self.excel_obj_sheet

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.excel_obj.save(self.file_path)
        send_mail(self.file_path)
