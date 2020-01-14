# -*- coding:  UTF-8 -*-
# 导出数据至excel文件

from lib.Mysql import *
from lib.File import *
from lib.ExportExcel import *


with DB("maowanapi") as db:
    db.execute("SELECT uid as '账号',mobile,uuid,createTime,a.pid as pid FROM `ucusers` as a LEFT JOIN `users_game_role_log` as b ON a.ucid = b.ucid WHERE `pid` IN ('1375','1382') AND created_at  >= '2019-12-09 00:00:00' GROUP BY a.ucid  ORDER BY a.pid LIMIT 10")
    with FILE() as file:
        with ExportExcel(file) as Excel:
            # , "设备号", "注册时间"   , data['uuid'], data['createTime']
            Excel.append(["账号", "手机号", "pid"])
            for data in db.fetchall():
                Excel.append([data['账号'], data['mobile'], data['pid']])




