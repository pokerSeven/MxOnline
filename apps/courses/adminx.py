# _*_ coding: utf-8 _*_
__author__ = 'lhj'
__date__ = '2017/7/26 0:00'

import xadmin
from .models import Course,Lesson,Video,CourseResource


class CourseAdmin(object):
	list_display = ['name', 'desc', 'detail', 'degree','students','fav_nums','click_nums','image','learn_times','add_time']
	search_fields = ['name', 'desc', 'detail', 'degree','students','fav_nums','click_nums','image','learn_times']
	list_filter = ['name', 'desc', 'detail', 'degree','students','fav_nums','click_nums','image','learn_times','add_time']


class LessonAdmin(object):
	list_display = ['couse', 'name','add_time']
	search_fields = ['couse', 'name']
	list_filter = ['couse__name', 'name','add_time']


class VideoAdmin(object):
	list_display = ['couse', 'name', 'add_time']
	search_fields = ['couse', 'name']
	list_filter = ['couse', 'name', 'add_time']


class CourseResourceAdmin(object):
	list_display = ['couse', 'name', 'download','add_time']
	search_fields = ['couse', 'name','download']
	list_filter = ['couse', 'name','download', 'add_time']


xadmin.site.register(Course,CourseAdmin)
xadmin.site.register(Lesson,LessonAdmin)
xadmin.site.register(Video,VideoAdmin)
xadmin.site.register(CourseResource,CourseResourceAdmin)