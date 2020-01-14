# -*- coding:  UTF-8 -*-

import re
import datetime


def replace(sql):
    yesterday = get_yesterday()
    today = get_today()
    sql = re.sub(r'yesterdayStartTime', "'" + yesterday.strftime('%Y-%m-%d') + ' 00:00:00' + "'", sql)
    sql = re.sub(r'yesterdayEndTime', "'" + yesterday.strftime('%Y-%m-%d') + ' 23:59:59' + "'", sql)
    sql = re.sub(r'todayStartTime', "'" + today.strftime('%Y-%m-%d') + ' 00:00:00' + "'", sql)
    sql = re.sub(r'todayEndTime', "'" + today.strftime('%Y-%m-%d') + ' 23:59:59' + "'", sql)
    return sql


def get_yesterday():
    today = datetime.date.today()
    one_day = datetime.timedelta(days=1)
    yesterday = today - one_day
    return yesterday


def get_today():
    today = datetime.date.today()
    return today

