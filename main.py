#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Jerry'
import time
from datetime import date, timedelta,datetime
from tkinter import *
from seckill.seckill_taobao import ChromeDrive


def main():
    # 指定当天晚上20点
    current_time_ms = int(round(time.time() * 1000))
    today_time = time.strftime("%Y-%m-%d 20:00:00", time.localtime())
    today_time_obj = datetime.strptime(today_time, '%Y-%m-%d %H:%M:%S')
    today_time_ms = int(time.mktime(today_time_obj.timetuple()) * 1000.0 + today_time_obj.microsecond / 1000)
    seckill_time=today_time
    if current_time_ms>today_time_ms :
        seckill_time = (date.today() + timedelta(days= 1)).strftime("%Y-%m-%d 20:00:00")
    print("抢购时间："+seckill_time)
    ChromeDrive(seckill_time = seckill_time).sec_kill()

if __name__ == '__main__':
    main()
