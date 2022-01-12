"""
=============================================
Author:chenliang
Time:2021/12/30
E-mail:814122090@qq.com
Company:深圳市中晴云科技有限公司
=============================================
"""

import os
import random
import unittest
from lib.ddt import ddt,data
from common.readexcel import ReadExcel
from common.path import DATADIR
from common.handlerequest import SendRequest
from common.handleconfig import conf
from common.handlelog import log

@ddt
class TestRegister(unittest.TestCase):
    excel = ReadExcel(os.path.join(DATADIR,"api_cases_excel.xlsx"),"register")
    cases = excel.read_data()
    requests = SendRequest()

    @data(*cases)
    def test_register(self,case):
        url = conf.get("env","url") + case["url"]
        method = case["method"]
        phone = self.random_phone()
        case["data"] = case["data"].replace("#phone#",phone)
        data = eval(case["data"])
        headers = eval(conf.get("env","headers"))
        expected = eval(case["expected"])
        row = case["case_id"] + 1

        response = self.requests.send_request(url=url,method=method,json=data,headers=headers)
        res = response.json()

        try:
            self.assertEqual(expected["code"],res["code"])
            self.assertEqual(expected["msg"],res["msg"])
        except AssertionError as e:
            self.excel.write_data(row=row,column=8,value="未通过")
            log.error("用例：{}未通过".format(case["title"]))
            log.exception(e)
            raise e
        else:
            self.excel.write_data(row=row,column=8,value="通过")
            log.info("用例：{}通过".format(case["title"]))


    def random_phone(self):
        phone = '150'
        for i in range(8):
            n = random.randint(1,9)
            phone += str(n)

        return phone



@ddt
class TestLogin(unittest.TestCase):
    excel = ReadExcel(os.path.join(DATADIR,"api_cases_excel.xlsx"),"login")
    cases = excel.read_data()
    request = SendRequest()


    @data(*cases)
    def test_login(self,case):
        url = conf.get("env","url") + case["url"]
        method = case["method"]
        data = eval(case["data"])
        headers = eval(conf.get("env","headers"))
        expected = eval(case["expected"])
        row = case["case_id"] + 1

        response = self.request.send_request(url=url,method=method,json=data,headers=headers)
        res = response.json()

        try:
            self.assertEqual(expected['code'],res['code'])
            self.assertEqual(expected['msg'],res['msg'])
        except AssertionError as e:
            self.excel.write_data(row=row,column=8,value="未通过")
            log.error("用例:{},未通过".format(case["title"]))
            log.exception(e)
            raise e
        else:
            self.excel.write_data(row=row, column=8, value="通过")
            log.info("用例:{},通过".format(case["title"]))





