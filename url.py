#!/usr/bin/env python
# coding=utf-8
"""
the url structure of website
"""
import sys #utf-8，兼容汉字
reload(sys)
sys.setdefaultencoding("utf-8")
from handlers.user import * 
from handlers.index import * 
from handlers.week import * 
from handlers.day import * 

url = [
    (r'/index', IndexHandler),
    (r'/login', LoginHandler),
    (r'/logout', LogoutHandler),
    (r'/manage_day', DayHandler),
    (r'/manage_day/del', DelDayHandler),
    (r'/manage_day/edit', EditDayHandler),
    (r'/manage_week', WeekHandler),
    (r'/manage_week/del', DelWeekHandler),
    (r'/manage_week/edit', EditWeekHandler),
]
