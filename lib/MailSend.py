# -*- coding:  UTF-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
from configs.mail import *
from configs import globaldata


def send_mail(file_path):
    config = get_mail_config()
    # receivers = [receiver]  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
    message = MIMEMultipart()
    message['From'] = 'hanbinjls@163.com'
    message['To'] = "接收结果邮箱"
    subject = '发送导出结果'
    message['Subject'] = Header(subject, 'utf-8')
    # 邮件正文内容
    message.attach(MIMEText('发送导出结果', 'plain', 'utf-8'))
    # 构造附件1，传送当前目录下的 test.txt 文件
    att1 = MIMEText(open(file_path, 'rb').read(), 'base64', 'utf-8')
    att1["Content-Type"] = 'application/octet-stream'
    # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
    att1["Content-Disposition"] = 'attachment; filename="' + file_path + '"'
    message.attach(att1)

    # try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(config['mail_host'], config['mail_port'])  # 25 为 SMTP 端口号
    smtpObj.login(config['mail_user'], config['mail_pass'])
    smtpObj.sendmail(config['sender'], globaldata.receivers, message.as_string())


# class MailSend:
#     def __init__(self):
#         self.senData = [
#             "1837261009@qq.com",
#             "日志导出记录",
#             "data/20200109181307.xlsx"
#         ]
#         print("进入")
#
#     def __enter__(self):
#         # return self.senData
#         print("进入循环")
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         try:
#             config = get_mail_config()
#             message = MIMEText(self.senData[1], 'plain', 'utf-8')
#             message['From'] = config['sender']
#             message['To'] = self.senData[0]
#             subject = '日志导出记录'
#             message['Subject'] = Header(subject, 'utf-8')
#             # 构造附件1（附件为TXT格式的文本）
#             att1 = MIMEText(open(self.senData[2], 'rb').read(), 'base64', 'utf-8')
#             att1["Content-Type"] = 'application/octet-stream'
#             att1["Content-Disposition"] = 'attachment; filename="data.xlsx"'
#             message.attach(att1)
#
#             smtp_obj = smtplib.SMTP_SSL()
#             smtp_obj.connect(config['mail_host'], config['mail_port'])  # 25 为 SMTP 端口号
#             smtp_obj.login(config['mail_user'], config['mail_pass'])
#             smtp_obj.sendmail(config['sender'], self.senData[0], message.as_string())
#             print("邮件发送成功")
#         except smtplib.SMTPException as e:
#             print("Error: 无法发送邮件" + e.strerror)
