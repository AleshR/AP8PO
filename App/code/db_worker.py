#!/usr/bin/python3

from tinydb import TinyDB, Query

#LOAD DBs

db_groups = TinyDB('../DBs/groups.json')
db_courses = TinyDB('../DBs/courses.json')
db_empls = TinyDB('../DBs/employees.json')
db_points = TinyDB('../DBs/points.json')
db_wrkflg = TinyDB('../DBs/work_flags.json')

#CREATIONS
#group creation
def create_group(shortcut, grade, sem, std_no, form, degree, lang):
	group = {'Shortcut' : shortcut,\
			 'Grade' : 	grade,\
			 'Semester' : sem,\
			 'Students' : std_no,\
			 'Form' : form,\
			 'Degree' : degree,\
			 'Language' : lang,\
			}

	return(db_groups.insert(group))

#course creation
def create_course(shortcut, weeks, predn, cv, semin, zak, lang, classR, group_list):
	course = {  'Shortcut' : shortcut,\
				'Weeks' : weeks,\
				'Predn' : predn,\
				'CV' : cv,\
				'Seminar' : semin,\
				'End' : zak,\
				'Language' : lang,\
				'Class_capacity' : classR,\
				'Group_list' : group_list,\
			}

	return(db_courses.insert(course))

#employee creation
def create_empl(name, surname, w_mail, p_mail, pts_wo_eng, pts_w_eng, doct, oblig, flags):
	employee = {'Name' : name,\
				'Surname' : surname,\
				'NameAll' : (name + ' ' +surname),\
				'Work_mail' : w_mail,\
				'Priv_mail' : p_mail,\
				'Point_wo_Engl' : pts_wo_eng,\
				'Points_w_Engl' : pts_w_eng,\
				'Doctor_deg' : doct,\
				'Obligation' : oblig,\
				'Flags' : flags,\
				}

	return(db_empls.insert(employee))

#workflag creation - doplnit propojeni employee --> DB
def create_wrkflg(name, employee, course, flag_type, stds_no, hrs, weeks, lang, flag_points):
	workflag = {'Flag_name' : name,\
				'Employee' : employee,\
				'Course' : course,\
				'Flag_type' : flag_type,\
				'Students' : stds_no,\
				'Hours' : hrs,\
				'Weeks' : weeks,\
				'Language' : lang,\
				'Flag_points' : flag_points,\
				}

	return(db_wrkflg.insert(workflag))

# #EDITIONS

# def edit_group():

# def edit_course():

# def edit_empl():

# def edit_wrkflg():

# #DELETE FNCs

# def del_group():

# def del_course():

# def del_empl():

# def del_wrkflg():

##Tady doplnit score fnc
"""
Hodina přednášky – double – 1,8
Hodina cvičení – double – 1,2
Hodina semináře – double – 1,2
Hodina přednášky anglicky – double – 2,4
Hodina cvičení anglicky – double – 1,8
Hodina semináře anglicky – double – 1,8
Udělení jednoho zápočtu – double – 0,2
Udělení jednoho klasifikovaného zápočtu – double – 0,3
Udělení jedné zkoušky – double – 0,4
Udělení jednoho zápočtu anglicky – double – 0,2
Udělení jednoho klasifikovaného zápočtu anglicky – double – 0,3
Udělení jedné zkoušky – anglicky - double – 0,4
#def points():
"""

def test():
	#test group creation
	#create_group('SWI',4,'LS',36,'P','Bc.','cz')
	#print(db_groups.all())

	#test course creation
	#create_course('AP8PO',14,1,3,2,'z','cz',24,1)
	#print(db_courses.all())

	#test employee creation
	#create_empl('Pavel', 'Vařacha', 'varacha@utb.cz', 'pavel.varacha@gmail.com', 526, 767,\
	#False, 1, 'neco')
	#print(db_empls.all())

	#test flags creation
	#create_wrkflg('Cvičení AP8PO 1', 'Pavel Vařacha', 'AP8PO' ,'Přednáška', 11, 2, 14,\
	#'CZ', 12.5)
	#print(db_wrkflg.all())

test()
