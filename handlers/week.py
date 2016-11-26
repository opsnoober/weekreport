#!/usr/bin/env python
# coding=utf-8
from base import BaseHandler
from methods.db import DB


class WeekHandler(BaseHandler):
    def get(self):
        self.render("week/manage_week.html")

class DelWeekHandler(BaseHandler):
    def get(self):
        pass

class EditWeekHandler(BaseHandler):
    def get(self):
        pass



