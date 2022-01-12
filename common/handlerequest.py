"""
=============================================
Author:chenliang
Time:2021/12/30
E-mail:814122090@qq.com
Company:深圳市中晴云科技有限公司
=============================================
"""

import requests

class SendRequest(object):

    def __init__(self):
        self.session = requests.session()

    def send_request(self,url,method,headers=None,params=None,json=None,data=None,files=None):
        if method == "get":
            response = requests.get(url=url,headers=headers,params=params)
        elif method == "post":
            response = requests.post(url=url,headers=headers,json=json,data=None,files=None)
        elif method == "patch":
            response = requests.post(url=url, headers=headers, json=json, data=None, files=None)

        return response
