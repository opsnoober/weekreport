#!/usr/bin/env python
# coding=utf-8
import tornado.web
import time

class AddReportHandler(tornado.web.RequestHandler):
    def get(self):
        #self.render("index.html")
        self.write("增加一条记录")

class DelReportHandler(tornado.web.RequestHandler):
    def get(self,rid):
        self.write("删除id为%s的记录"%rid)

class EditReportHandler(tornado.web.RequestHandler):
    def get(self,rid):
        self.write("编辑id为%s的记录"%rid)

class QueryReportHandler(tornado.web.RequestHandler):
    def get(self):
        qid=self.get_argument('qid','')
        qname=self.get_argument('qname','')
        if qid:
            self.write("查询id为%s的记录"%qid)
        elif qname:
            self.write("查询name为%s的记录"%qname)

class ListReportHandler(tornado.web.RequestHandler):
    def get(self):
        page_limit=5
        #执行sql查询db.execute("select * from weekreport desc by create_time limit %s" %page_limit);
        self.write("显示最新%s条记录"%page_limit)
        
