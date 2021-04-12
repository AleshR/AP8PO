#!/usr/bin/python3

import pandas as pd
from tinydb import TinyDB, Query, where
from UliPlot.XLSX import auto_adjust_xlsx_column_width


db_groups = TinyDB('../DBs/groups.json')
db_courses = TinyDB('../DBs/courses.json')
db_empls = TinyDB('../DBs/employees.json')
db_points = TinyDB('../DBs/points.json')
db_wrkflg = TinyDB('../DBs/work_flags.json')
  
out_file = '../Export/data_file.xls'
writer = pd.ExcelWriter(out_file, engine = 'xlsxwriter')

def Export():
	df1 = pd.DataFrame.from_dict(pd.json_normalize(db_groups.all()))
	df2 = pd.DataFrame.from_dict(pd.json_normalize(db_courses.all()))
	df3 = pd.DataFrame.from_dict(pd.json_normalize(db_empls .all()))
	df4 = pd.DataFrame.from_dict(pd.json_normalize(db_points.all()))
	df5 = pd.DataFrame.from_dict(pd.json_normalize(db_wrkflg.all()))
	
	del df1['tsmp']
	del df2['tsmp']
	del df3['tsmp']
	del df5['tsmp']
	
	df1.to_excel(writer, sheet_name = 'Skupiny')
	df2.to_excel(writer, sheet_name = 'Předměty')
	df3.to_excel(writer, sheet_name = 'Zaměstnanci')
	df4.to_excel(writer, sheet_name = 'Body')
	df5.to_excel(writer, sheet_name = 'Štítky')
	
	writer.save()
	
	return(print("Exported"))