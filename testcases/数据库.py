"""
=============================================
Author:chenliang
Time:2022/1/5
E-mail:814122090@qq.com
Company:深圳市中晴云科技有限公司
=============================================
"""

import pymysql

"""
主机：
port：3306
用户：future
密码：123456
"""

# 第一步：连接数据库
conn = pymysql.connect(host="120.78.128.25",
                       port=3306,
                       user="future",
                       password="123456",
                       # 通过设置游标类型，可以控制查询出来的数据类型
                       cursorclass=pymysql.cursors.DictCursor,
                       charset="utf8")


# 第二部：创建一个游标对象
cur = conn.cursor()

# 第三步：执行sql语句
sql = "SELECT id FROM futureloan.member WHERE mobile_phone=13367899876"
# 返回的是查询到的数据条数
res = cur.execute(sql)
print(res)

# 第四步：获取查询的数据
# 查询第一条数据
data = cur.fetchone()
# 查询所有数据
data1 = cur.fetchall()
# 删除
cur.execute(sql)
# 提交事务
conn.commit()

# pymysql 操作sql sever
# cx_oracle:   操作oracel
