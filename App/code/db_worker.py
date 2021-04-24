#!/usr/bin/python3

from tinydb import TinyDB, Query, where
from time import time
import json
import hashlib

QueryBuilder = Query()

#LOAD DBs
db_groups = TinyDB('../DBs/groups.json')
db_courses = TinyDB('../DBs/courses.json')
db_empls = TinyDB('../DBs/employees.json')
db_points = TinyDB('../DBs/points.json')
db_wrkflg = TinyDB('../DBs/work_flags.json')

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
"""
class Bodiky():
	LECTURE = 1.8
	EXCERC = 1.2
	SEMIN = 1.2
	
	LECTURE_EN = 2.4
	EXCERC_EN = 1.8
	SEMIN_EN = 1.8

	CREDIT = 0.2
	CLASS_CREDIT = 0.3
	EXAM = 0.4

	CREDIT_EN = 0.2
	CLASS_CREDIT_EN = 0.3
	EXAM_EN = 0.4

#print(Points.LECTURE + Points.EXAM)

#CREATIONS
#group creation
#Ke všem databazim doplnit db.close() - pro jisttou, at neni konflikt
def create_group(shortcut, grade, sem, std_no, form, degree, lang):
	group = {
			 'Shortcut' : shortcut,\
			 'Grade' : 	grade,\
			 'Semester' : sem,\
			 'Students' : std_no,\
			 'Form' : form,\
			 'Degree' : degree,\
			 'Language' : lang,\
			}
	
	stmp = str(float(time()))+shortcut
	hash_stmp = hashlib.sha1(stmp.encode())

	return(db_groups.insert({'name':shortcut, 'info':group, 'tsmp': str(hash_stmp.hexdigest())}))
#course creation
def create_course(shortcut, weeks, predn, cv, semin, zak, lang, classR, group_list):
	course = {  
				'Shortcut' : shortcut,\
				'Weeks' : weeks,\
				'Predn' : predn,\
				'CV' : cv,\
				'Seminar' : semin,\
				'End' : zak,\
				'Language' : lang,\
				'Class_capacity' : classR,\
				'Group_list' : group_list,\
			}

	stmp = str(float(time()))+shortcut
	hash_stmp = hashlib.sha1(stmp.encode())

	return(db_courses.insert({'name': shortcut, 'info':course, 'tsmp': str(hash_stmp.hexdigest())}))

#employee creation
def create_empl(name, surname, w_mail, p_mail, pts_wo_eng, pts_w_eng, doct, oblig, flags):
	employee = {
				'Name' : name,\
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
	
	stmp = str(float(time()))+surname
	hash_stmp = hashlib.sha1(stmp.encode())

	return(db_empls.insert({'name': (name + ' ' +surname),'info':employee, 'tsmp': str(hash_stmp.hexdigest())}))

#workflag creation - doplnit propojeni employee --> DB
def create_wrkflg(name, employee, course, flag_type, stds_no, hrs, weeks, lang, flag_points):
	workflag = {
				'Flag_name' : name,\
				'Employee' : employee,\
				'Course' : course,\
				'Flag_type' : flag_type,\
				'Students' : stds_no,\
				'Hours' : hrs,\
				'Weeks' : weeks,\
				'Language' : lang,\
				'Flag_points' : flag_points,\
				}

	stmp = str(float(time()))+name
	hash_stmp = hashlib.sha1(stmp.encode())

	return(db_wrkflg.insert({'name':name, 'info':workflag, 'tsmp': str(hash_stmp.hexdigest())}))

"""
Points function works with arguments:
	name == name of subject like Vařacha Pavel
	course == name of course
	lang == language of lessons
	points == amount of points
	operation == add || subs
"""

def points_rec(name, course, lang, points, operation):

	if(db_points.search(Query().Name.matches(name))):

		all_pts = db_points.get(Query().Name == name)['Points']

		if (all_pts <= 0) and (operation == 'subs'):
			print('Points --> we get bottom barrier == 0')
			return(db_points.update({'Points' : 0}, Query().Name.matches(name)))

		elif operation == 'add':
			print('Add points --> ', points+all_pts)
			return(db_points.update({'Points' : (points+all_pts)}, Query().Name.matches(name)))

		elif operation == 'subs':
			print('Substract points --> ', all_pts-points)
			return(db_points.update({'Points' : (all_pts-points)}, Query().Name.matches(name)))

	else:
		points_rec = {
					'Name' : name,\
					'Course' : course,\
					'Language' : lang,\
					'Points' : points
		}
		
		print('Let\'s create some new record braško...')
		return(db_points.insert(points_rec))

#points_rec('Pavel Vařacha', 'AP8AK', 'CZ', 50, 'subs')



#Easy remove DB record (not implemented in tinyDB - deletion by given index)
def delete_record(db,index):
	file = db.all()[index]
	return(db.remove((QueryBuilder.tsmp == file['tsmp'])))

#write to DB with change
#to je jebání....
#Je to kurva hotove... toho si musim vypalit na CDčko, znovu to vymyslet nechci!
def update_db(db, idx, idy, itm):
	info = db.all()[idx]['info']
	tsmp = db.all()[idx]['tsmp']
	element = list(info)[idy]
	
	info.update({element : itm})
	print(info)

	db.update({'info': info}, Query().tsmp == tsmp)
	print(db.all()[idx]['info'])


def cnt_points(db, idx, idy, itm):
	return	print("Points!!!")
#update_db(db_groups,0,1,'sdsdsd!!!')


"""
Jak na to?!
Takže předpokládám, že ten enum je cesta. Konec konců mi vrací samotný db.all() dict.
Já teď potřebuju přijít na to, jak iterovat dict. 
Musim vzít první argument (např Shortcut) a v query provést update záznamu v JSONU.

Priklad update:

db.update({'a': 2}, Query().a.exists())
Musim to slozit tak, že 'a' bude parametr daný přes column a 2 bude given text

"""

#delete_record(db_wrkflg,1)

def test():
	"""
	#test group creation
	create_group('SWI',4,'LS',36,'P','Bc.','cz')
	print(db_groups.all())
	
	#test course creation
	create_course('AP8PO',14,1,3,2,'z','cz',24,1)
	print(db_courses.all())

	#test employee creation
	create_empl('Pavel', 'Vařacha', 'varacha@utb.cz', 'pavel.varacha@gmail.com', 526, 767,\
	False, 1, 'neco')
	print(db_empls.all())

	#test flags creation
	create_wrkflg('Cvičení AP8PO 1', 'Pavel Vařacha', 'AP8PO' ,'Přednáška', 11, 2, 14,\
	'CZ', 12.5)
	
	print(db_wrkflg.all())

	print('length of db_group: ', len(db_groups))
	print('length of db_wrkflg: ', len(db_wrkflg))
	print('length of db_empls: ', len(db_empls))
	print('length of db_courses: ', len(db_courses))
	print('length of db_points: ', len(db_points))

	file = db_groups.all()

	print(len(file)) #number of records
	#print(len(file[0]['name'])) #number of letters in name
	#print((file[0]['info']['Surname'])) #number of objects in info

	#for x in file[0]['info']:
	#	val = file[0]['info'][x]
	#	print(val)
	#print(file[0]['info'])
"""
""""
for x in range(1,50):
	pass
	test()
"""