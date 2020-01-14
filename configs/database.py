#!/usr/bin/python3
# 数据库配置


def get_mysql_config(name="maowanapi"):
    config = {
        'maowanapi': {
            "host": "127.0.0.1",
            "port": 3306,
            "db": "dbname",
            "user": "root",
            "passwd": "",
            "charset": "utf8mb4"
        },
        'local': {
            "host": "127.0.0.1",
            "port": 3306,
            "db": "dbname",
            "user": "root",
            "passwd": "",
            "charset": "utf8mb4"
        }
    }
    return config[name]
    # mysql = {
    #     "host": "rm-wz93t4ip4eh195l85o.mysql.rds.aliyuncs.com",
    #     "port": 3306,
    #     "db": "maowanapi",
    #     "user": "maowansdk",
    #     "passwd": "catplay@0904",
    #     "charset": "utf8mb4"
    # }
    # # mysql = {
    # #     "host": "127.0.0.1",
    # #     "port": 3306,
    # #     "db": "python",
    # #     "user": "python",
    # #     "passwd": "python",
    # #     "charset": "utf8mb4"
    # # }
    # return mysql


# def get_local_mysql_config():
#     mysql = {
#         "host": "172.24.29.229",
#         "port": 3306,
#         "db": "exportTask",
#         "user": "exportTask",
#         "passwd": "exportTask",
#         "charset": "utf8mb4"
#     }
#     return mysql

