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

