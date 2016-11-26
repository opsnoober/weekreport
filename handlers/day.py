#!/usr/bin/env python
# coding=utf-8
from base import BaseHandler
import tornado.web
from methods.db import DB


class DayHandler(BaseHandler):

    @tornado.web.authenticated

    def get(self):
        sql = 'select * from report'
        rows = DB.query(sql)
        self.render("day/manage_day.html",rows=rows)

    def post(self):
        user_name = self.get_argument('user_name')
        week = self.get_argument('week')
        work_type = self.get_argument('work_type','')
        work_content = self.get_argument('work_content','')
        create_time = self.get_argument('create_time','')
        argument_data = {
		'user_name': user_name,
        	'week': week,
        	'work_type':work_type,
        	'work_content':work_content,
        	'create_time':create_time
	}
        for v in argument_data.values():
            print v
        sql = 'insert into report (user_name,week,work_type,work_content,create_time) \
          values("%(user_name)s","%(week)s","%(work_type)s","%(work_content)s","%(create_time)s")' %(argument_data)
        DB.execute(sql)
        self.redirect('/manage_day')


class EditDayHandler(BaseHandler):
    def post(self):
        id = self.get_argument('id')
        week = self.get_argument('week','')
        work_type = self.get_argument('work_type','')
        work_content = self.get_argument('work_content','')
        create_time = self.get_argument('create_time','')
        argument_data = {
                'id': id,
                'week': week,
                'work_type':work_type,
                'work_content':work_content,
                'create_time':create_time
        }
        for v in argument_data.values():
            print v
        sql = 'update report set work_type="%(work_type)s",work_content="%(work_content)s",create_time="%(create_time)s" \
          where id="%(id)s"' %(argument_data)
        DB.execute(sql)
        self.redirect('/manage_day')


class DelDayHandler(BaseHandler):

    @tornado.web.authenticated
    def post(self):

        delete = self.get_argument('delete')
        sql = 'delete from report where id=%s' % delete
        DB.execute(sql)       
        self.redirect('/manage_day')
        
