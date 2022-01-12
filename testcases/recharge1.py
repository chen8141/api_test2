"""
=============================================
Author:chenliang
Time:2022/1/4
E-mail:814122090@qq.com
Company:深圳市中晴云科技有限公司
=============================================
"""

import jsonpath
import os
import unittest
from lib.ddt import ddt,data
from common.readexcel import ReadExcel
from common.handleconfig import conf
from common.path import DATADIR
from common.handlerequest import SendRequest
from common.handlelog import log
from common.connectdb import DB
from decimal import Decimal
from common.handledata import CaseData,replace_data


@ddt
class TestRecharge(unittest.TestCase):
    excel = ReadExcel(os.path.join(DATADIR,"api_cases_excel.xlsx"),"recharge")
    cases = excel.read_data()
    requests = SendRequest()
    db = DB()

    @classmethod
    def setUpClass(cls):
        url = conf.get("env","url") + "/member/login"
        data = {
            "mobile_phone":conf.get("test_data","phone"),
            "pwd":conf.get("test_data","pwd")
        }
        headers = eval(conf.get("env","headers"))
        response = cls.requests.send_request(url=url,method="post",headers=headers,json=data)
        res = response.json()
        token = jsonpath.jsonpath(res,"$..token")[0]
        token_type = jsonpath.jsonpath(res,"$..token_type")[0]
        CaseData.member_id = str(jsonpath.jsonpath(res,"$..id")[0])
        CaseData.token_value = token_type + " " + token
        # 设置类属性
        # member_id = jsonpath.jsonpath(res, "$..id")[0]
        # setattr(CaseData,member_id)


    @data(*cases)
    def test_recharge(self,case):
        url = conf.get("env","url") + case["url"]
        method = case["method"]
        case["data"] = replace_data(case["data"])
        # case["data"] = case["data"].replace("#member_id#",str(self.member_id))
        data = eval(case["data"])
        expected = eval(case["expected"])
        row = case["case_id"] + 1
        headers = eval(conf.get("env","headers"))
        headers["Authorization"] = getattr(CaseData,"token_value")
        # 请求前，获取余额
        if case["check_sql"]:
            sql = "SELECT leave_amount FROM futureloan.member WHERE mobile_phone={}".format(
                conf.get("test_data","phone"))
            start_money = self.db.find_one(sql)["leave_amount"]

        response = self.requests.send_request(url=url,headers=headers,json=data,method=method)
        res = response.json()
        # 请求后获取余额
        if case["check_sql"]:
            sql = "SELECT leave_amount FROM futureloan.member WHERE mobile_phone={}".format(
                conf.get("test_data","phone"))
            end_money = self.db.find_one(sql)["leave_amount"]

        try:
            self.assertEqual(expected["code"],res["code"])
            self.assertEqual(expected['msg'],res["msg"])
            # 判断用例是否需要sql校验
            if case["check_sql"]:
                # 需要校验则充值后的余额减去充值前的余额和充值金额做比对
                self.assertEqual(end_money-start_money,Decimal(str(data["amount"])))

        except AssertionError as e:
            self.excel.write_data(row=row,column=8,value="未通过")
            log.error("用例：{}未通过".format(case["title"]))
            log.exception(e)
            raise e
        else:
            self.excel.write_data(row=row,column=8,value="通过")
            log.info("用例：{}通过".format(case["title"]))





