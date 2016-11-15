#!/usr/bin/env python
# coding=utf-8
"""
the url structure of website
"""
import sys #utf-8，兼容汉字
reload(sys)
sys.setdefaultencoding("utf-8")
from handlers.weekreport import * #假设已经有了

url = [
    (r'/weekreport/add', AddReportHandler),
    (r'/weekreport/del/(\d+)', DelReportHandler),
    (r'/weekreport/edit/(\d+)', EditReportHandler),
    (r'/weekreport/query', QueryReportHandler),
    (r'/weekreport/list', ListReportHandler),
]
