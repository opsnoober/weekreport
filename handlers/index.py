#!/usr/bin/env python
# coding=utf-8
import tornado.web
import time

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html",title="首页")

