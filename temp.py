import mysql.connector
import csv

def save():
	conn = mysql.connector.connect(user='root', password='*****',
	                              host='localhost',
	                              database='****')	
	cursor = conn.cursor()
	cursor.execute('SELECT * FROM Household')
	Household_db = cursor.fetchall()
	with open('Household.csv','w') as f:
		Household = csv.DictWriter(f,['id','Наименование','Площадь','Состояние зелёного массива'])
		Household.writeheader()
		for i in Household_db:
			Household.writerow({'id':i[0],'Наименование':i[1],'Площадь':i[2],'Состояние зелёного массива':i[3]})

	cursor.execute('SELECT * FROM Chiefs')
	Chiefs_db = cursor.fetchall()
	with open('Chiefs.csv','w') as f:
		Chiefs = csv.DictWriter(f,['id','Инициалы','Адрес','id Хозяйства'])
		Chiefs.writeheader()
		for i in Chiefs_db:
			Chiefs.writerow({'id':i[0],'Инициалы':i[1],'Адрес':i[2],'id Хозяйства':i[3]})

	cursor.execute('SELECT * FROM Workers')
	Workers_db = cursor.fetchall()
	with open('Workers.csv','w') as f:
		Workers = csv.DictWriter(f,['id','Имя','Фамиля','Отчество','Дата рождения','Адрес','id начальника'])
		Workers.writeheader()
		for i in Workers_db:
			Workers.writerow({'id':i[0],'Имя':i[1],'Фамиля':i[2],'Отчество':i[3],'Дата рождения':i[4],'Адрес':i[5],'id начальника':i[6]})

	cursor.execute('SELECT * FROM Trees')
	Trees_db = cursor.fetchall()
	with open('Trees.csv','w') as f:
		Trees = csv.DictWriter(f,['id','Название','Тип дерева'])
		Trees.writeheader()
		for i in Trees_db:
			Trees.writerow({'id':i[0],'Название':i[1],'Тип дерева':i[2]})

	cursor.execute('SELECT * FROM Apparate')
	Apparate_db = cursor.fetchall()
	with open('Apparate.csv','w') as f:
		Apparate = csv.DictWriter(f,['id','Тип Аппаратуры'])
		Apparate.writeheader()
		for i in Apparate_db:
			Apparate.writerow({'id':i[0],'Тип Аппаратуры':i[1]})

	cursor.execute('SELECT * FROM Ch_Salary')
	Ch_Salary_db = cursor.fetchall()
	with open('Ch_Salary.csv','w') as f:
		Ch_Salary = csv.DictWriter(f,['id Начальника','Зарплата'])
		Ch_Salary.writeheader()
		for i in Ch_Salary_db:
			Ch_Salary.writerow({'id Начальника':i[0],'Зарплата':i[1]})

	cursor.execute('SELECT * FROM Wk_Salary')
	Wk_Salary_db = cursor.fetchall()
	with open('Wk_Salary.csv','w') as f:
		Wk_Salary = csv.DictWriter(f,['id Работника','Зарплата'])
		Wk_Salary.writeheader()
		for i in Wk_Salary_db:
			Wk_Salary.writerow({'id Работника':i[0],'Зарплата':i[1]})

	cursor.execute('SELECT * FROM density')
	density_db  = cursor.fetchall()
	with open('density.csv','w') as f:
		density = csv.DictWriter(f,['id Хозяйства','id Дерева','Плотность','Средний возраст'])
		density.writeheader()
		for i in density_db:
			density.writerow({'id Хозяйства':i[0],'id Дерева':i[1],'Плотность':i[2],'Средний возраст':i[3]})

	cursor.execute('SELECT * FROM Worktypes ')
	Worktypes_db = cursor.fetchall()
	with open('Worktypes.csv','w') as f:
		Worktypes = csv.DictWriter(f,['id','Тип работы'])
		Worktypes.writeheader()
		for i in Worktypes_db:
			Worktypes.writerow({'id':i[0],'Тип работы':i[1]})

	cursor.execute('SELECT * FROM Wt_Wk')
	Wt_Wk_db = cursor.fetchall()
	with open('Wt_Wk.csv','w') as f:
		Wt_Wk = csv.DictWriter(f,['id Работника','id Типа работы'])
		Wt_Wk.writeheader()
		for i in Wt_Wk_db:
			Wt_Wk.writerow({'id Работника':i[0],'id Типа работы':i[1]})

	cursor.execute('SELECT * FROM App_Hous')
	App_Hous_db = cursor.fetchall()
	with open('App_Hous.csv','w') as f:
		App_Hous = csv.DictWriter(f,['id Хозяйства','id Аппаратуры'])
		App_Hous.writeheader()
		for i in App_Hous_db:
			App_Hous.writerow({'id Хозяйства':i[0],'id Аппаратуры':i[1]})
	conn.close()