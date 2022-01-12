"""
=============================================
Author:chenliang
Time:2021/12/28
E-mail:814122090@qq.com
Company:深圳市中晴云科技有限公司
=============================================
"""
import os
import unittest
from common.path import CASEDIR
from lib.HTMLTestRunnerNew import HTMLTestRunner
from common.path import REPORTDIR
from common.handle_email import send_email


suite = unittest.TestSuite()
loader = unittest.TestLoader()
suite.addTest(loader.discover(CASEDIR))

report_file = os.path.join(REPORTDIR,"report.html")

runner = HTMLTestRunner(stream=open(report_file,'wb'),
                        title='api_test',
                        description='测试报告',
                        tester='陈亮')
# runner = unittest.TextTestRunner()
runner.run(suite)

send_email(report_file,"api_test")

