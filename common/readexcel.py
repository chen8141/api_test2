"""
============================
Author:柠檬班-木森
Time:2020/2/7   21:34
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

import openpyxl

class ReadExcel(object):

    def __init__(self,filename,sheetname):
        self.filename = filename
        self.sheetname = sheetname

    def open(self):
        self.workbook = openpyxl.load_workbook(self.filename)
        self.sheet = self.workbook[self.sheetname]

    def read_data(self):
        self.open()
        datas = list(self.sheet.rows)
        title = [i.value for i in datas[0]]
        cases = []
        for i in datas[1:]:
            value = [c.value for c in i]
            case = dict(zip(title,value))
            cases.append(case)

        return cases

    def write_data(self,row,column,value):
        self.open()
        self.sheet.cell(row=row,column=column,value=value)
        self.workbook.save(self.filename)

