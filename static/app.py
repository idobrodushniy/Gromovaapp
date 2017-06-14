from flask import (
	Flask,
	render_template,
	url_for,
	redirect,
	abort
	)
import mysql.connector


app = Flask(__name__)
app.debug = True
@app.route('/sqldata')
def home_data():
	conn = mysql.connector.connect(user='root', password='1Balance1',
                            	host='localhost',database='xxx1')
	print('Connected!!!!!!!!!!!!!!!!')
	cursor = conn.cursor()
	cursor.execute('SELECT * FROM results')
	render = cursor.fetchall()
	print(conn)
	return render_template('first.html', content1 = render)
	if (request.method == 'POST'):
		return 0
if __name__ == '__main__':
	app.run()
	
