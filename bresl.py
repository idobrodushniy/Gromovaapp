from flask import (
	Flask,
	render_template,
	url_for,
	redirect,
	abort,
	request,
	session
	)
import mysql.connector
from flask_login import (
			LoginManager,
			login_user
			)
from flask_debugtoolbar import (
	DebugToolbarExtension
	)
import temp

class CONNECTION():
	conn = mysql.connector.connect(user='root', password='******',
                              host='localhost',
                              database='******')	
app = Flask(__name__)
app.secret_key = 'saijfsdihfewihfiejiAsijwifheujnfeISFUSDNFS'
app.debug = True


@app.route('/sqldata', methods = ['GET'])
def home_data():
	if session.get('login') != 'Evgeniya':
		return redirect(url_for('login'))
	
	return render_template('first.html')

@app.route('/sqldata', methods = ['POST'])
def post():
	if session.get('login') != 'Evgeniya':
		return redirect(url_for('login'))
	if request.form.get('q') == 'Сохранить отчёты по БД':
		temp.save()
	return redirect(url_for('home_data'))

@app.route('/looser')
def looser():
	return render_template('forgot.html')

@app.route('/trees', methods = ['GET', 'POST'])
def trees():
	if session.get('login') != 'Evgeniya':
		return redirect(url_for('login'))
	conn = mysql.connector.connect(user='root', password='******',
                              host='localhost',
                              database='******')
	cursor = conn.cursor()
	cursor.execute('SELECT * FROM Trees;')
	db = cursor.fetchall()
	try:
		if (request.method == 'POST'):
			cursor.execute('UPDATE Trees SET name="{0}", type ="{1}" where id = {2}'.format(
				request.form.get('name'),
				request.form.get('type'),
				request.args.get('choice')
				))
			conn.commit()
			conn.close()
			return redirect(url_for('trees'))
	except:
		return render_template('error.html', treesupdate = 'ok')
	if request.args.get('Submit') == 'Выбрать':
		cursor.execute('SELECT * from Trees where id = {0}'.format(
			request.args.get('choice')))
		form = cursor.fetchall()
		return render_template('trees.html',
			 content = db,
			 form = form)
	conn.close()
	return render_template('trees.html', content = db)





@app.route('/household', methods = ['GET', 'POST'])
def household():
	if session.get('login') != 'Evgeniya':
		return redirect(url_for('login'))
	conn = mysql.connector.connect(user='root', password='******',
                              host='localhost',
                              database='******')
	cursor = conn.cursor()
	cursor.execute('SELECT * FROM Household;')
	db = cursor.fetchall()
	try:
		if (request.method == 'POST'):
			cursor.execute('UPDATE Household SET name="{0}", space={1}, status = "{2}"  WHERE id = {3} '.format(
				request.form.get('name'),
				request.form.get('space'),
				request.form.get('status'),
				request.args.get('choice')))
			conn.commit()
			conn.close()
			return redirect(url_for('household'))
	except:
		return render_template('error.html', householdupdate = 'ok')

	if request.args.get('Submit') == 'Выбрать':
		cursor.execute('SELECT * from Household where id = {0}'.format(
			request.args.get('choice')))
		form = cursor.fetchall()
		return render_template('household.html',
			 content = db,
			 form = form)
	conn.close()
	return render_template('household.html', content = db)


@app.route('/wk_salary', methods = ['GET', 'POST'])
def wk_salary():
	if session.get('login') != 'Evgeniya':
		return redirect(url_for('login'))
	conn = mysql.connector.connect(user='root', password='******',
                              host='localhost',
                              database='******')
	cursor = conn.cursor()
	cursor.execute('SELECT * FROM Wk_Salary')
	db = cursor.fetchall()
	try:
		if (request.method == 'POST'):
			cursor.execute('UPDATE Wk_Salary SET  salary = {0} WHERE id_wk = {1} '.format(
				request.form.get('salary'),
				request.form.get('id_wk')))
			conn.commit()
			conn.close()
			return redirect(url_for('wk_salary'))
	except:
		return render_template('error.html', wk_salaryupdate = 'ok')

	if request.args.get('Submit') == 'Выбрать':
		cursor.execute('SELECT * from Wk_Salary where id_wk = {0}'.format(
			request.args.get('choice')))
		form = cursor.fetchall()
		return render_template('wk_salary.html',
			 content = db,
			 form = form)
	conn.close()
	return render_template('wk_salary.html', content = db)

@app.route('/ch_salary', methods = ['GET', 'POST'])
def ch_salary():
	if session.get('login') != 'Evgeniya':
		return redirect(url_for('login'))
	conn = mysql.connector.connect(user='root', password='******',
                              host='localhost',
                              database='******')
	cursor = conn.cursor()
	cursor.execute('SELECT * FROM Ch_Salary')
	db = cursor.fetchall()
	try:
		if (request.method == 'POST'):
			print(request.form.get('salary'))
			print(request.form.get('id_ch'))
			cursor.execute('UPDATE Ch_Salary SET  salary = {0} WHERE id_chiefs = {1} '.format(
				request.form.get('salary'),
				request.form.get('id_ch')))
			conn.commit()
			conn.close()
			return redirect(url_for('ch_salary'))
	except:
		return render_template('error.html', ch_salaryupdate = 'ok')

	if request.args.get('Submit') == 'Выбрать':
		cursor.execute('SELECT * from Ch_Salary where id_chiefs = {0}'.format(
			request.args.get('choice')))
		form = cursor.fetchall()
		return render_template('ch_salary.html',
			 content = db,
			 form = form)
	conn.close()
	return render_template('ch_salary.html', content = db)

@app.route('/workers', methods = ['GET', 'POST'])
def workers():
	if session.get('login') != 'Evgeniya':
		return redirect(url_for('login'))
	conn = mysql.connector.connect(user='root', password='******',
                              host='localhost',
                              database='******')
	cursor = conn.cursor()
	cursor.execute('SELECT * FROM Workers;')
	db = cursor.fetchall()
	try:
		if (request.method == 'POST'):
			cursor.execute('UPDATE Workers SET name="{0}", surname="{1}", midname = "{2}",birthday = "{3}",adress = "{4}",id_chief = {5}  WHERE id = {6} '.format(
				request.form.get('name'),
				request.form.get('surname'),
				request.form.get('midname'),
				request.form.get('birthday'),
				request.form.get('adress'),
				request.form.get('id_chief'),
				request.args.get('choice')))
			conn.commit()
			conn.close()
			return redirect(url_for('workers'))
	except:
		return render_template('error.html', workersupdate = 'ok')
	if request.args.get('Submit') == 'Выбрать':
		cursor.execute('SELECT * from Workers where id = {0}'.format(
			request.args.get('choice')))
		form = cursor.fetchall()
		cursor.execute('SELECT id FROM Chiefs order by id')
		idchiefs = cursor.fetchall()
		return render_template('workers.html',
			 content = db,
			 form = form,
			 idchiefs = idchiefs)
	conn.close()
	return render_template('workers.html', content = db)

@app.route('/chiefs', methods = ['GET', 'POST'])
def chiefs():
	if session.get('login') != 'Evgeniya':
		return redirect(url_for('login'))
	conn = mysql.connector.connect(user='root', password='******',
                              host='localhost',
                              database='******')
	cursor = conn.cursor()
	cursor.execute('SELECT * FROM Chiefs;')
	db = cursor.fetchall() 
	try:
		if (request.method == 'POST'):
			cursor.execute('UPDATE Chiefs SET initials="{0}", adress="{1}", id_hshl = "{2}" WHERE ID = {3} '.format(
				request.form.get('initials'),
				request.form.get('adress'),
				request.form.get('household'),
				request.args.get('choice')))
			conn.commit()
			conn.close()
			return redirect(url_for('chiefs'))
	except:
		return render_template('error.html', chiefsupdate = 'ok')
	if request.args.get('Submit') == 'Выбрать':
		cursor.execute('SELECT * FROM Chiefs WHERE ID = {0}'.format(request.args.get('choice')))
		form = cursor.fetchall()
		cursor.execute('SELECT id FROM Household ORDER BY id;')
		householdname = cursor.fetchall()
		return render_template('chiefs.html', content = db, form = form,
							households = householdname)
	conn.close()
	return render_template('chiefs.html', content = db)

@app.route('/density', methods = ['GET', 'POST'])
def density():
	if session.get('login') != 'Evgeniya':
		return redirect(url_for('login'))
	conn = mysql.connector.connect(user='root', password='******',
                              host='localhost',
                              database='******')
	cursor = conn.cursor()
	cursor.execute('SELECT * FROM density;')
	db = cursor.fetchall()
	cursor.execute('SELECT DISTINCT id_tree FROM  density  order by id_tree')
	id_tree = cursor.fetchall()
	cursor.execute('SELECT DISTINCT id_hshl FROM  density  order by id_hshl')
	id_hshl = cursor.fetchall()
	try:
		if (request.method == 'POST'):
			cursor.execute('UPDATE density SET treedensity = {0}, middleage = {1} WHERE id_hshl = {2} and id_tree = {3} '.format(
				request.form.get('treedensity'),
				request.form.get('middleage'),
				request.form.get('id_hshl'),
				request.form.get('id_tree')
				))
			conn.commit()
			conn.close()
			return redirect(url_for('density'))
	except:
		return render_template('error.html', densityupdate = 'ok')

	if request.args.get('Submit') == 'Выбрать':
		cursor.execute('SELECT * FROM density WHERE id_hshl = {0} and id_tree = {1} '.format(
			request.args.get('choice'),
			request.args.get('choice1')
			))
		form = cursor.fetchall()
		return render_template('density.html', content = db, form = form,id_tree = id_tree, id_hshl = id_hshl)
	
	conn.close()
	return render_template('density.html', content = db,id_tree = id_tree, id_hshl = id_hshl)

@app.route('/login', methods = ['GET', 'POST'])
def login():
	if (request.method == 'GET'):
		session['login'] = None
		session['password'] = None
		return render_template('login.html')
	else:
		login = request.form.get('login')
		password = request.form.get('password')
		if (login != 'Evgeniya') or (password != 'Gromova'):
			return (render_template('login.html', error = ' Not valid password!'))
		session['login'] = login
		session['password'] = password
		return redirect(url_for('home_data'))


@app.route('/error')
def error():
	return render_template('error.html', content = ' Это страница ошибочек!')



@app.route('/worktypes', methods = ['GET', 'POST'])
def worktypes():
	if session.get('login') != 'Evgeniya':
		return redirect(url_for('login'))
	conn = mysql.connector.connect(user='root', password='******',
                              host='localhost',
                              database='******')
	cursor = conn.cursor()
	cursor.execute('SELECT * FROM Worktypes ORDER BY id;')
	db = cursor.fetchall()
	try:
		if request.method == 'POST':
			cursor.execute('UPDATE Worktypes SET type = "{0}" WHERE id = {1}'.format(
				request.form.get('type'),
				request.form.get('id')))
			conn.commit()
			conn.close()
			return redirect(url_for('worktypes'))
	except:
		return render_template('error.html', worktypesupdate='ok' )
	if request.args.get('Submit') == 'Выбрать':
		cursor.execute('SELECT * FROM Worktypes WHERE id = {0} ORDER BY id'.format(
						request.args.get('choice')
						))
		form = cursor.fetchall()
		return render_template('worktypes.html', content = db, form = form)
	conn.close()
	return render_template('worktypes.html', content = db)

@app.route('/wt_wk')
def wt_wk():
	if session.get('login') != 'Evgeniya':
		return redirect(url_for('login'))
	conn = mysql.connector.connect(user='root', password='******',
                              host='localhost',
                              database='******')
	cursor = conn.cursor()
	cursor.execute('SELECT * FROM Wt_Wk ORDER BY id_wk')
	db = cursor.fetchall()
	conn.close()
	return render_template('wt_wk.html', content = db)



@app.route('/apparate', methods = ['GET','POST'] )
def apparate():
	if session.get('login') != 'Evgeniya':
		return redirect(url_for('login'))
	conn = mysql.connector.connect(user='root', password='******',
                              host='localhost',
                              database='******')
	cursor = conn.cursor()
	cursor.execute('SELECT * FROM  Apparate')
	db = cursor.fetchall()
	try:
		if request.method == 'POST':
			cursor.execute('UPDATE Apparate SET type = "{0}" where id = {1}'.format(
				request.form.get('type'),
				request.form.get('id')
				))
			conn.commit()
			return redirect(url_for('apparate'))
	except:
		return render_template('error.html', apparateupdate='ok')
	if request.args.get('Submit')== 'Выбрать':
		cursor.execute('SELECT * FROM Apparate WHERE id = {0} ORDER BY ID'.format(
			request.args.get('choice')
			))
		form = cursor.fetchall()
		return render_template('apparate.html', content = db, form = form)
	conn.close()
	return render_template('apparate.html', content = db)


@app.route('/app_hous', methods = ['GET','POST'])
def app_hous():
	if session.get('login') != 'Evgeniya':
		return redirect(url_for('login'))
	conn = mysql.connector.connect(user='root', password='******',
                              host='localhost',
                              database='******')
	cursor = conn.cursor()
	cursor.execute('SELECT * FROM  App_Hous')
	db = cursor.fetchall()
	return render_template('app_hous.html', content = db)


@app.route('/delete', methods = ['GET','POST'])
def delete():
	if session.get('login') != 'Evgeniya':
		return redirect(url_for('login'))
	conn = mysql.connector.connect(user='root', password='******',
                              host='localhost',
                              database='******')
	cursor = conn.cursor()
	
	if request.args.get('q') == 'Деревья':
		cursor.execute('SELECT * FROM Trees;')
		db = cursor.fetchall()
		if request.method == 'POST':
			cursor.execute('DELETE FROM Trees WHERE id = {0}'.format(
				request.form.get('choice')
				))
			conn.commit()
			return redirect('/delete?q=Деревья')
		return render_template('delete.html', content = db, trees = 'ok')
	
	if request.args.get('q') == 'Начальники':
		cursor.execute('SELECT * FROM Chiefs;')
		db = cursor.fetchall()
		if request.method == 'POST':
			cursor.execute('DELETE FROM Chiefs WHERE id = {0}'.format(
				request.form.get('choice')
				))
			conn.commit()
			return redirect('/delete?q=Начальники')
		return render_template('delete.html', content = db, chiefs = 'ok')
	
	if request.args.get('q') == 'Хозяйства':
		cursor.execute('SELECT * FROM Household')
		db = cursor.fetchall()
		if request.method == 'POST':
			cursor.execute('DELETE FROM Household WHERE id = {0}'.format(
				request.form.get('choice')
				))
			conn.commit()
			return redirect('/delete?q=Хозяйства')
		return render_template('delete.html', content = db, household = 'ok')
	
	if request.args.get('q') == 'Работники':
		cursor.execute('SELECT * FROM Workers ')
		db = cursor.fetchall()
		if request.method == 'POST':
			cursor.execute('DELETE FROM Workers WHERE id = {0}'.format(
				request.form.get('choice')
				))
			conn.commit()
			return redirect('/delete?q=Работники')
		return render_template('delete.html', content = db, workers = 'ok')
	
	if request.args.get('q') == 'Плотность':
		cursor.execute('SELECT * FROM density')
		db = cursor.fetchall()
		cursor.execute('SELECT  DISTINCT id_hshl FROM density ')
		id_hshl  = cursor.fetchall()
		cursor.execute('SELECT  DISTINCT id_tree FROM density ')
		id_tree  = cursor.fetchall()
		if request.method == 'POST':
			cursor.execute('DELETE FROM density WHERE id_hshl = {0} and id_tree = {1}'.format(
				request.form.get('choice'),
				request.form.get('choice1')
				))
			conn.commit()
			return redirect('/delete?q=Плотность')
		return render_template('delete.html', content = db, density = 'ok',
			id_tree = id_tree, id_hshl = id_hshl)
	
	if request.args.get('q') == 'ЗарплатаНач':
		cursor.execute('SELECT * FROM Ch_Salary ORDER BY id_chiefs')
		db = cursor.fetchall()
		if request.method == 'POST':
			cursor.execute('DELETE FROM Ch_Salary WHERE id_chiefs = {0}'.format(
				request.form.get('choice')))
			conn.commit()
			return redirect('/delete?q=ЗарплатаНач')
		return render_template('delete.html', content = db,ch_salary = 'ok')

	if request.args.get('q') == 'ЗарплатаРаб':
		cursor.execute('SELECT * FROM Wk_Salary ORDER BY id_wk')
		db = cursor.fetchall()
		if request.method == 'POST':
			cursor.execute('DELETE FROM Wk_Salary WHERE id_wk = {0}'.format(
				request.form.get('choice')))
			conn.commit()
			return redirect('/delete?q=ЗарплатаРаб')
		return render_template('delete.html',content = db, wk_salary = 'ok')

	if request.args.get('q') == 'Аппаратура':
		cursor.execute('SELECT * FROM Apparate ORDER BY id')
		db = cursor.fetchall()
		if request.method == 'POST':
			cursor.execute('DELETE FROM Apparate WHERE id = {0}'.format(
				request.form.get('choice')
				))
			conn.commit()
			return redirect('/delete?q=Аппаратура')

		return render_template('delete.html',content = db,apparate = 'ok')

	if request.args.get('q') == 'Типы работ':
		cursor.execute('SELECT * FROM Worktypes ORDER BY id')
		db = cursor.fetchall()
		if request.method == 'POST':
			cursor.execute('DELETE FROM Worktypes WHERE id = {0}'.format(
				request.form.get('choice')))
			conn.commit()
			return redirect('/delete?q=Типы+работ')
		return render_template('delete.html',content = db,worktypes='ok')

	if request.args.get('q') == 'Работник-Типы работ':
		cursor.execute('SELECT * FROM Wt_Wk ORDER BY id_wk')
		db = cursor.fetchall()
		cursor.execute('SELECT DISTINCT id_wk FROM Wt_Wk ORDER BY id_wk')
		id_wk = cursor.fetchall()
		cursor.execute('SELECT DISTINCT id_wt FROM Wt_Wk ORDER BY id_wt ')
		id_wt = cursor.fetchall()
		if request.method == 'POST':
			cursor.execute('DELETE FROM Wt_Wk WHERE id_wk={0} AND id_wt={1}'.format(
				request.form.get('choice'),
				request.form.get('choice1')
				))
			conn.commit()
			return redirect('/delete?q=Работник-Типы+работ')
		return render_template('delete.html',
			content = db,
		 	wt_wk = 'ok',
			id_wk = id_wk,
			id_wt=id_wt)

	if request.args.get('q') == 'Хозяйство-Аппаратура':
		cursor.execute('SELECT * FROM App_Hous ORDER BY id_hshl')
		db = cursor.fetchall()
		cursor.execute('SELECT DISTINCT id_hshl FROM App_Hous ORDER BY id_hshl')
		id_hshl = cursor.fetchall()
		cursor.execute('SELECT DISTINCT id_app FROM App_Hous ORDER BY id_app')
		id_app = cursor.fetchall()
		if request.method == 'POST':
			cursor.execute('DELETE FROM App_Hous WHERE id_hshl={0} AND id_app={1}'.format(
				request.form.get('choice'),
				request.form.get('choice1')
				))
			conn.commit()
			return redirect('/delete?q=Хозяйство-Аппаратура')
		return render_template('delete.html',
			content = db,
			app_hous = 'ok',
			id_hshl = id_hshl,
			id_app = id_app
			)
	return render_template('delete.html',starter = 'ok')

@app.route('/add', methods = ['POST','GET'])
def add():
	if session.get('login') != 'Evgeniya':
		return redirect(url_for('login'))
	conn = mysql.connector.connect(user='root', password='******',
                              host='localhost',
                              database='******')
	cursor = conn.cursor()
	if request.args.get('q') == 'Хозяйства':
		cursor.execute('SELECT * FROM Household')
		db = cursor.fetchall()
		try:
			if (request.form.get('name') == "" or request.form.get('space') == "" or request.form.get('status') == "" or request.form.get('type') == ""):
				raise Exception()
			if request.method == 'POST':
				cursor.execute('INSERT INTO Household(name,space,status) values("{0}",{1},"{2}")'.format(
					request.form.get('name'),
					request.form.get('space'),
					request.form.get('status'),
					))
				conn.commit()
				return redirect('/add?q=Хозяйства')
			return render_template('add.html', content = db, householdadd = 'ok')
		except:
			return render_template('error.html',householdadd = 'ok')
	
	if request.args.get('q') == 'Начальники':
		cursor.execute('SELECT * FROM Chiefs')
		db = cursor.fetchall()
		cursor.execute('SELECT id FROM Household order by id')
		id_hshl = cursor.fetchall()
		try:
			if (request.form.get('initials') == "" or request.form.get('adress') == "" or request.form.get('id_hshl') == ""):
				raise Exception()
			if request.method == 'POST':
				cursor.execute('INSERT INTO Chiefs(initials,adress,id_hshl) values("{0}","{1}",{2})'.format(
					request.form.get('initials'),
					request.form.get('adress'),
					request.form.get('id_hshl'),
					))
				conn.commit()
				return redirect('/add?q=Начальники')
			return render_template('add.html',
									content = db,
									chiefsadd = 'ok',
									id_hshl = id_hshl)
		except:
			return render_template('error.html',chiefsadd = 'ok')


	if request.args.get('q') == 'Деревья':
		cursor.execute('SELECT * FROM Trees')
		db = cursor.fetchall()
		try:
			if (request.form.get('name') == ""  or request.form.get('type') == ""):
				raise Exception()
			if request.method == 'POST':
				cursor.execute('INSERT INTO Trees(name,type) values("{0}","{1}")'.format(
					request.form.get('name'),
					request.form.get('type')
					))
				conn.commit()
				return redirect('/add?q=Деревья')
			return render_template('add.html',
									content = db,
									treesadd = 'ok')
		except:
			return render_template('error.html',treesadd = 'ok')
	
	if request.args.get('q') == 'Работники':
		cursor.execute('SELECT * FROM Workers')
		db = cursor.fetchall()
		cursor.execute('SELECT id FROM Chiefs ORDER BY id')
		id_chiefs = cursor.fetchall()
		try:
			if (request.form.get('name') == ""  
				or request.form.get('surname') == "" 
				or request.form.get('birthday') == ""  
				or request.form.get('midname') == "" 
				or request.form.get('adress') == ""):
					raise Exception()
			if request.method == 'POST':
				cursor.execute('INSERT INTO Workers(name,surname,midname,birthday,adress,id_chief) VALUES("{0}","{1}","{2}","{3}","{4}",{5})'.format(
					request.form.get('name'),
					request.form.get('surname'),
					request.form.get('midname'),
					request.form.get('birthday'),
					request.form.get('adress'),
					request.form.get('id_chief'),
					))
				conn.commit()
				return redirect('add?q=Работники')

			return render_template('add.html',
									content = db,
									workersadd = 'ok',
									id_chiefs = id_chiefs)
		except:
			return render_template('error.html', workersadd = 'ok')

	if request.args.get('q') == 'Плотность':
		cursor.execute('SELECT * FROM density')
		db = cursor.fetchall()
		cursor.execute('SELECT id FROM Household order by id')
		id_hshl = cursor.fetchall()
		cursor.execute('SELECT id FROM Trees order by id')
		id_tree = cursor.fetchall()
		try:
			if (request.form.get('treedensity') == "" 
				or request.form.get('middleage') == ""):
				raise Exception()
			if request.method == 'POST':
				cursor.execute('INSERT INTO density(id_hshl,id_tree,treedensity,middleage) VALUES({0},{1},"{2}","{3}")'.format(
					request.form.get('id_hshl'),
					request.form.get('id_tree'),
					request.form.get('treedensity'),
					request.form.get('middleage'),
					))
				conn.commit()
				return redirect('add?q=Плотность')
		except:
			return render_template('error.html',densityadd = 'ok')
		return render_template('add.html',
							content = db,
							densityadd = 'ok',
							id_hshl = id_hshl,
							id_tree = id_tree)

	if request.args.get('q') == 'ЗарплатаНач':
		cursor.execute('SELECT * FROM Ch_Salary')
		db = cursor.fetchall()
		cursor.execute('SELECT id from Chiefs ORDER BY id')
		id_chiefs = cursor.fetchall()	
		try:	
			if request.method == 'POST':
				cursor.execute('INSERT INTO Ch_Salary(id_chiefs,salary) VALUES ({1},{0})'.format(
					request.form.get('ch_salary'),
					request.form.get('id_chief')
					))
				conn.commit()
				return redirect('add?q=ЗарплатаНач')
		except:
			return render_template('error.html', ch_salaryadd='ok')
		return render_template('add.html',
							content = db,
							ch_salaryadd = 'ok',
							id_chiefs = id_chiefs)

	if request.args.get('q') == 'ЗарплатаРаб':
		cursor.execute('SELECT * FROM Wk_Salary')
		db = cursor.fetchall()
		cursor.execute('SELECT id from Workers ORDER BY id')
		id_wk = cursor.fetchall()	
		try:	
			if request.method == 'POST':
				cursor.execute('INSERT INTO Wk_Salary(id_wk, salary) VALUES ({1},{0})'.format(
						request.form.get('wk_salary'),
						request.form.get('id_wk')
						))
				conn.commit()
				return redirect('add?q=ЗарплатаРаб')
		except:
			return render_template('error.html', wk_salaryadd='ok')
		return render_template('add.html',
							content = db,
							wk_salaryadd='ok',
							id_wk = id_wk)

	if request.args.get('q') == 'Аппаратура':
		cursor.execute('SELECT * FROM Apparate')
		db = cursor.fetchall()
		try:
			if request.method == 'POST':
				cursor.execute('INSERT INTO Apparate(type) VALUES ("{0}")'.format(
					request.form.get('type')))
				conn.commit()
				return redirect('add?q=Аппаратура')
		except:
			return render_template('error.html',apparateadd ='ok')
		return render_template('add.html',
				content = db,
				apparateadd = 'ok'
				)

	if request.args.get('q') == 'Типы работ':
		cursor.execute('SELECT * FROM Worktypes ORDER BY id')
		db = cursor.fetchall()
		try:
			if request.method == 'POST':
				cursor.execute('INSERT INTO Worktypes(type) VALUES("{0}")'.format(
					request.form.get('type')))
				conn.commit()
				return redirect('add?q=Типы+работ')
		except:
			return render_template('error.html',worktypesadd='ok')
		return render_template('add.html', 
				content=db,
				worktypesadd='ok')

	if request.args.get('q') == 'Работник-Типы работ':
		cursor.execute('SELECT * FROM Wt_Wk ORDER BY id_wk')
		db = cursor.fetchall()
		cursor.execute('SELECT id FROM Workers ORDER BY id')
		id_wk = cursor.fetchall()
		cursor.execute('SELECT id FROM Worktypes ORDER BY id')
		id_wt = cursor.fetchall()
		try:
			if request.method == 'POST':
				cursor.execute('INSERT INTO Wt_Wk(id_wk,id_wt) VALUES({0},{1})'.format(
					request.form.get('id_wk'),
					request.form.get('id_wt'),
					))
				conn.commit()
				return redirect('add?q=Работник-Типы+работ')
		except:
			return render_template('error.html',wt_wkadd = 'ok')
		return render_template('add.html',
				content = db,
				wt_wkadd ='ok',
				id_wk = id_wk,
				id_wt = id_wt)
	
	if request.args.get('q') == 'Хозяйство-Аппаратура':
		cursor.execute('SELECT * FROM App_Hous ORDER BY id_hshl')
		db = cursor.fetchall()
		cursor.execute('SELECT id FROM Household ORDER BY id')
		id_hshl = cursor.fetchall()
		cursor.execute('SELECT id FROM Apparate ORDER BY id')
		id_app = cursor.fetchall()
		try:
			if request.method == 'POST':
				cursor.execute('INSERT INTO App_Hous(id_hshl,id_app) VALUES({0},{1})'.format(
					request.form.get('id_hshl'),
					request.form.get('id_app'),
					))
				conn.commit()
				return redirect('add?q=Хозяйство-Аппаратура')
		except:
			return render_template('error.html',app_housadd = 'ok')
		return render_template('add.html',
				content = db,
				app_housadd ='ok',
				id_hshl = id_hshl,
				id_app = id_app)
		
	return render_template('add.html',starter = 'ok')


@app.route('/query')
def query():
	if session.get('login') != 'Evgeniya':
		return redirect(url_for('login'))
	conn = mysql.connector.connect(user='root', password='******',
                              host='localhost',
                              database='******')
	cursor = conn.cursor()
	if request.args.get('q') == 'Запрос1':
		cursor.execute('SELECT * from Workers where id_chief = 1')
		query1 = cursor.fetchall()
		return render_template('query.html',query1=query1)
	
	if request.args.get('q') == 'Запрос2':
		cursor.execute('SELECT name from Trees WHERE id IN (SELECT DISTINCT id_tree FROM density  WHERE treedensity > 30) ')
		query2 = cursor.fetchall()
		return render_template('query.html',query2 = query2)
	if request.args.get('q') == 'Запрос3':
		cursor.execute('SELECT id_wk,COUNT(*) AS Count_works  FROM Wt_Wk GROUP BY id_wk ')
		query3 = cursor.fetchall()
		return render_template('query.html',query3 = query3)
	if request.args.get('q') == 'Запрос4':
		cursor.execute('SELECT name,surname,midname from Workers where id in (SELECT id_wk from Wt_Wk GROUP BY id_wk having COUNT(*) = (SELECT COUNT(id) FROM Worktypes))')
		query4 = cursor.fetchall()
		return render_template('query.html',query4 = query4)
	if request.args.get('q') == 'Запрос5':
		cursor.execute('SELECT AVG(salary) FROM Wk_Salary')
		query5 = cursor.fetchall()
		return render_template('query.html',query5 = query5)
	if request.args.get('q') == 'Запрос6':
		cursor.execute('SELECT id,type FROM Apparate WHERE id NOT IN (SELECT id_app FROM App_Hous)')
		query6 = cursor.fetchall()
		return render_template('query.html',query6 = query6)
	if request.args.get('q') == 'Запрос7':
		cursor.execute('SELECT id_hshl,id_tree FROM density UNION SELECT id,name FROM Trees')
		query7 = cursor.fetchall()
		return render_template('query.html',query7 = query7)
	if request.args.get('q') == 'Запрос8':
		cursor.execute('SELECT id,name FROM Workers WHERE id  IN (SELECT id_wk from Wt_Wk) ORDER BY id')
		query8 = cursor.fetchall()
		return render_template('query.html', query8 = query8)
	if request.args.get('q') == 'Запрос9':
		cursor.execute('SELECT Workers.id,name,surname,midname,birthday,Workers.adress,Chiefs.id,initials,Chiefs.adress FROM Workers JOIN Chiefs on Chiefs.id = Workers.id_chief ORDER BY Workers.id')
		query9 = cursor.fetchall()
		return render_template('query.html', query9 = query9)
	if request.args.get('q') == 'Запрос10':
		cursor.execute('SELECT Household.id,Household.name,Household.space,Household.status,Chiefs.id,Chiefs.initials,Chiefs.adress from Household JOIN Chiefs ON Chiefs.id_hshl = Household.id ORDER BY Household.id')
		query10 = cursor.fetchall()
		return render_template('query.html', query10 = query10)
	return render_template('query.html',starter = 'ok')
if __name__ == '__main__':
	app.run()
