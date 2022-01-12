"""
=============================================
Author:chenliang
Time:2021/12/31
E-mail:814122090@qq.com
Company:深圳市中晴云科技有限公司
=============================================
"""

import jsonpath
import os
import unittest
from lib.ddt import ddt,data
from common.readexcel import ReadExcel
from common.path import DATADIR
from common.handleconfig import conf
from common.handlerequest import SendRequest
from common.handlelog import log
from common.handledata import CaseData,replace_data

@ddt
class TestRecharge(unittest.TestCase):
    excel = ReadExcel(os.path.join(DATADIR,"api_cases_excel.xlsx"),"recharge")
    cases = excel.read_data()
    requests = SendRequest()

    @classmethod
    def setUpClass(cls):
        url = conf.get("env","url") + "/member/login"
        data = {
            "mobile_phone":conf.get("test_data","phone"),
            "pwd":conf.get("test_data","pwd"),
        }
        headers = eval(conf.get("env", "headers"))
        response = cls.requests.send_request(method="post",url=url, headers=headers, json=data)
        res = response.json()
        token = jsonpath.jsonpath(res, "$..token")[0]
        token_type = jsonpath.jsonpath(res, "$..token_type")[0]
        CaseData.member_id = str(jsonpath.jsonpath(res,"$..id")[0])
        CaseData.token_value = token_type + " " + token


    @data(*cases)
    def test_recharge(self,case):
        url = conf.get("env","url") + case["url"]
        method = case["method"]
        # 替换参数中的用户id
        case["data"] = replace_data(case["data"])
        data = eval(case["data"])
        headers = eval(conf.get("env","headers"))
        #在请求中加入setupclass中提取的token
        headers["Authorization"] = getattr(CaseData,"token_value")

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

