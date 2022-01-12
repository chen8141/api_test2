"""
=============================================
Author:chenliang
Time:2021/12/29
E-mail:814122090@qq.com
Company:深圳市中晴云科技有限公司
=============================================
"""


import os

# res = os.path.abspath(__file__)
# print(res)
# # 获取指定文件路径的父级目录路径
# res2 = os.path.dirname(res)
# print(res2)
# res3 = os.path.dirname(res2)
# print(res3)


BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CONFDIR = os.path.join(BASEDIR,"conf")

DATADIR = os.path.join(BASEDIR,"data")

LOGDIR = os.path.join(BASEDIR,"logs")

REPORTDIR = os.path.join(BASEDIR,"reports")

CASEDIR = os.path.join(BASEDIR,"testcases")

