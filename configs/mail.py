#!/usr/bin/python3
# 邮箱配置


def get_mail_config():
    mail = {
        "mail_host": "smtp.163.com",
        "mail_port": 25,
        "mail_user": "xxxxx@163.com",
        "mail_pass": "xxxx",
        "sender": "hanbinjls@163.com",
        "receivers": ""
    }
    # mysql = {
    #     "host": "127.0.0.1",
    #     "port": 3306,
    #     "db": "python",
    #     "user": "python",
    #     "passwd": "python",
    #     "charset": "utf8mb4"
    # }
    return mail
