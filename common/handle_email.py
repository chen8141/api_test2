"""
=============================================
Author:chenliang
Time:2022/1/12
E-mail:814122090@qq.com
Company:深圳市中晴云科技有限公司
=============================================
"""




import smtplib
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from common.handleconfig import conf

def send_email(filename,title):
    """

    :param filename: 文件路径
    :param title: 标题
    :return:
    """
    # 第一步：连接邮箱smtp服务器，并登录
    smtp = smtplib.SMTP_SSL(host=conf.get("email","host"),port=conf.getint("email","port"))
    smtp.login(user=conf.get("email","user"),password=conf.get("email","password"))

    # 第二步：构建一封邮件
    # 创建一封多组件的邮件
    msg = MIMEMultipart()
    # 读取文件
    with open(filename,"rb") as f:
        content = f.read()
    # 创建邮件文本内容
    text_msg = MIMEText(content,_subtype="html",_charset="utf8")
    # 添加到多组件的邮件中
    msg.attach(text_msg)
    # 创建邮件的附件
    report_file = MIMEApplication(content)
    report_file.add_header('content-disposition', 'attachment',filename=filename)
    # 将附件添加到多组件的邮件中
    msg.attach(report_file)


    msg["Subject"] = title
    msg["From"] = conf.get("email","from_addr")
    msg["To"] = conf.get("email","to_addr")

    # 第三步：发送邮件
    smtp.send_message(msg,from_addr=conf.get("email","from_addr"),to_addrs=conf.get("email","to_addr"))
