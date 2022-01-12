"""
=============================================
Author:chenliang
Time:2022/1/5
E-mail:814122090@qq.com
Company:深圳市中晴云科技有限公司
=============================================
"""

import re
from common.handleconfig import conf

# s = "123#python#123456#python#56416"

# re.findall()

# re.search()
# search：匹配出第一个符合要求的数据，返回的是一个对象
# group：可以获取匹配到数据

# re.match()
# 从字符串头部匹配符合的数据，返回一个对象（如果数据不在头部返回None）

# res = re.sub("python","java",s,1)
# print(res)
# 替换的方法




# r1 = r"#(.+?)#"
# res = re.search(r1,s)
# data = res.group()
# key = res.group(1)
# # print(key)
# s = s.replace(data, conf.get("test_data",key))
# print(s)

def replace_data(s):
    r1 = "#(.+?)#"
    while re.search(r1,s):
        res = re.search(r1,s)
        data = res.group()
        key = res.group(1)
        s = s.replace(data,conf.get("test_data",key))
    return s

s = '{"mobile_phone":"#phone#","pwd":"#pwd#"}'

s = replace_data(s)
print(s)



