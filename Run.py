# -*- coding:  UTF-8 -*-
import datetime
import urllib.parse
import redis
from configs import globaldata
from lib.Mysql import *
from lib.File import *
from lib.ExportExcel import *
from lib.Redis import *
from lib.Replace import *

# r = redis.Redis(host='172.24.29.229', port=6379, password='hanbin')
# value = {"id": 1, "name": "韩彬"}
# # r.set("name", value)
# # r.sadd('names', value)
# # has = r.hkeys('name')
# # has = r.hmset('record', value)
# # print(has)
# val = r.hmget("record", "name")
# print(val[0].decode())
# # val1ue = r.get('names')
# # print(value)
# with DB('local') as db:
#     db.execute("SELECT id,`type`,excelTitle,`sql` FROM tasks where id = 1")
#     data = db.fetchone()
#     print(data)
#     with REDIS() as redis_con:
#         is_success = redis_con.hmset("tasks", data)
#
#         print(is_success)


def run_task(task):
    with DB('local') as db:
        db.execute("SELECT id, `name`,`type`,execlTitle,`sql`,`email` FROM tasks where id = %s" % task)
        data = db.fetchone()
        with REDIS() as redis_con:
            # is_success = redis_con.hmset("tasks", data)
            sql = urllib.parse.unquote(data["sql"], encoding="utf-8", errors='replace')
            sql = replace(sql)
            globaldata.receivers = data["email"].split(",")
            globaldata.name = data["name"]
            excelTitle = data['execlTitle'].split(",")
            with DB("maowanapi") as maowanapi:
                maowanapi.execute(sql)
                with FILE() as file:
                    with ExportExcel(file) as Excel:
                        # , "设备号", "注册时间"   , data['uuid'], data['createTime']
                        Excel.append(excelTitle)
                        for data in maowanapi.fetchall():
                            insert_data = []
                            for filed in excelTitle:
                                insert_data.append(data[filed])
                            Excel.append(insert_data)
        db.execute("UPDATE `tasks` SET lastTime=%s WHERE `id`=%s", (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"
                                                                                                     ), task))


with REDIS() as redis_list:
    while True:
        task_id = redis_list.lpop("game_sdk_database_task")
        if task_id is not None and task_id != '':
            task_id = task_id.decode()
            run_task(task_id)



