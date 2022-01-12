"""
=============================================
Author:chenliang
Time:2022/1/11
E-mail:814122090@qq.com
Company:深圳市中晴云科技有限公司
=============================================
"""
import smtplib
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart

'''
邮箱账号：
端口号：465
授权码：pncmjnjobiflbfjc


'''
# 第一步：连接邮箱smtp服务器，并登录
smtp = smtplib.SMTP_SSL(host="smtp.qq.com",port="465")
smtp.login(user="814122090@qq.com",password="pncmjnjobiflbfjc")

# 第二步：构建一封邮件
# 创建一封多组件的邮件
msg = MIMEMultipart()
# 读取文件
with open("report.html","rb") as f:
    content = f.read()
# 创建邮件文本内容
text_msg = MIMEText(content,_subtype="html",_charset="utf8")
# 添加到多组件的邮件中
msg.attach(text_msg)
# 创建邮件的附件
report_file = MIMEApplication(content)
report_file.add_header('content-disposition', 'attachment',filename='26report.html')
# 将附件添加到多组件的邮件中
msg.attach(report_file)


msg["Subject"] = "api_test"
msg["From"] = "814122090@qq.com"
msg["To"] = "814122090@qq.com"

# 第三步：发送邮件
smtp.send_message(msg,from_addr="814122090@qq.com",to_addrs="814122090@qq.com")
