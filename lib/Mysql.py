# -*- coding:  UTF-8 -*-

import pymysql
from configs.database import *


class DB:
    def __init__(self, name):
        config = get_mysql_config(name)
        self.con = pymysql.connect(host=config['host'], port=config['port'], db=config['db'], user=config['user'], passwd=config['passwd'], charset=config['charset'])
        self.cur = self.con.cursor(cursor=pymysql.cursors.DictCursor)

    def __enter__(self):
        return self.cur

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.con.commit()
        self.cur.close()
        self.con.close()

