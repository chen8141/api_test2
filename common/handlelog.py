"""
============================
Author:柠檬班-木森
Time:2020/2/12   21:31
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

import os
import logging
from common.handleconfig import conf
from common.path import LOGDIR

class HandleLog(object):

    @staticmethod
    def create_logger():
        mylog = logging.getLogger(conf.get('log','name'))
        mylog.setLevel(conf.get('log','level'))
        sh = logging.StreamHandler()
        sh.setLevel(conf.get('log','sh_level'))
        mylog.addHandler(sh)
        fh = logging.FileHandler(filename=os.path.join(LOGDIR,"log.log"),encoding="utf8")
        fh.setLevel(conf.get('log','fh_level'))
        mylog.addHandler(fh)
        formater = '%(asctime)s - [%(filename)s-->line:%(lineno)d] - %(levelname)s: %(message)s'
        fm = logging.Formatter(formater)
        sh.setFormatter(fm)
        fh.setFormatter(fm)

        return mylog

log = HandleLog.create_logger()

















#         formater = '%(asctime)s - [%(filename)s-->line:%(lineno)d] - %(levelname)s: %(message)s'
#         fm = logging.Formatter(formater)
#         sh.setFormatter(fm)
#         fh.setFormatter(fm)
#
#         return mylog
#
# log = HandleLog.create_logger()


