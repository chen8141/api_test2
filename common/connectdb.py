"""
=============================================
Author:chenliang
Time:2022/1/5
E-mail:814122090@qq.com
Company:深圳市中晴云科技有限公司
=============================================
"""

import pymysql
from common.handleconfig import conf


class DB:
    def __init__(self):
        # 创建一个连接对象
        self.conn = pymysql.connect(host=conf.get("db","host"),
                                    port=conf.get("db","port"),
                                    user=conf.get("db","user"),
                                    password=conf.get("db","pwd"),
                                    charset=conf.get("db","charset"),
                                    cursorclass=pymysql.cursors.DictCursor)
        # 创建一个游标
        self.cur = self.conn.cursor()

    def find_one(self,sql):
        """获取查询出来的第一条数据"""
        self.conn.commit()
        self.cur.execute(sql)
        data = self.cur.fetchone()
        return data

    def find_all(self,sql):
        """获取查询出来的所有数据"""
        self.conn.commit()
        self.cur.execute(sql)
        data = self.cur.fetchall()
        return data

    def close(self):
        """关闭游标，断开连接"""
        self.cur.close()
        self.conn.close()




