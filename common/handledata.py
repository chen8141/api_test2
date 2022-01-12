"""
=============================================
Author:chenliang
Time:2022/1/6
E-mail:814122090@qq.com
Company:深圳市中晴云科技有限公司
=============================================
"""

import re
from common.handleconfig import conf

class CaseData:
    '''这个类专门用来保存，用例执行过程中提取出来给其他用例用的数据'''
    pass

def replace_data(s):
    r1 = "#(.+?)#"
    while re.search(r1,s):
        res = re.search(r1,s)
        data = res.group()
        key = res.group(1)
        try:
            s = s.replace(data,conf.get("test_data",key))
        except Exception:
            s = s.replace(data,getattr(CaseData,key))

    return s



# def replace_data(s):
#     r1 = "#(.+?)#"
#     while re.search(r1,s):
#         res = re.search(r1,s)
#         key = res.group(1)
#         try:
#             s = re.sub(r1,conf.get("test_data", key), s, 1)
#         except Exception:
#             s = re.sub(r1,getattr(CaseData,key), s, 1)
#
#     return s
