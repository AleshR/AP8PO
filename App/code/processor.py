#!/usr/bin/python3

from tinydb import TinyDB, Query

db_groups = TinyDB('../DBs/groups.json')
db_courses = TinyDB('../DBs/courses.json')
db_empls = TinyDB('../DBs/employees.json')
db_points = TinyDB('../DBs/points.json')
db_wrkflg = TinyDB('../DBs/work_flags.json')


def point_calculate():
	print("hello")
