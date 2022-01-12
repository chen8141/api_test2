"""
=============================================
Author:chenliang
Time:2022/1/5
E-mail:814122090@qq.com
Company:深圳市中晴云科技有限公司
=============================================
"""

import os
import jsonpath
import unittest
from lib.ddt import ddt,data
from common.readexcel import ReadExcel
from common.path import DATADIR
from common.handleconfig import conf
from common.handlerequest import SendRequest
from common.handlelog import log


filename = os.path.join(DATADIR,"api_cases_excel.xlsx")

@ddt
class TestWithdraw(unittest.TestCase):
    excel = ReadExcel(filename,"withdraw")
    cases = excel.read_data()
    requests = SendRequest()


    @data(*cases)
    def test_withdraw(self,case):
        url = conf.get("env","url") + case["url"]
        headers = eval(conf.get("env","headers"))
        method = case["method"]
        case["data"] = case["data"].replace("#phone#",conf.get("test_data","phone"))
        case["data"] = case["data"].replace("#pwd#", conf.get("test_data", "pwd"))
        if case["interface"] == "withdraw":
            case["data"] = case["data"].replace("#member_id#", str(self.member_id))
            headers["Authorization"] = self.token_value
        data = eval(case["data"])
        expected = eval(case["expected"])
        row = case["case_id"] + 1

        response = self.requests.send_request(url=url,headers=headers,method=method,json=data)
        res = response.json()

        if case["interface"] == "login":
            token = jsonpath.jsonpath(res,"$..token")[0]
            token_type = jsonpath.jsonpath(res,"$..token_type")[0]
            TestWithdraw.member_id = jsonpath.jsonpath(res,"$..id")[0]
            TestWithdraw.token_value = token_type + " " + token

        try:
            self.assertEqual(expected["code"],res["code"])
            self.assertEqual(expected["msg"],res["msg"])
        except AssertionError as e:
            self.excel.write_data(row=row,column=8,value="未通过")
            log.error("用例:{}未通过".format(case["title"]))
            log.exception(e)
            raise e
        else:
            self.excel.write_data(row=row,column=8,value="通过")
            log.info("用例:{}通过".format(case["title"]))






