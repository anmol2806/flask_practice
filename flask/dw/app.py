from flask import *

app = Flask(__name__)

@app.route('/')
def x():
	return render_template("login.html")

@app.route('/login',methods = ['POST'])
def login():
	uname = request.form['usrname']
	password = request.form['password']
	if uname == 'diwaker' and password == 'prashar':
		return render_template('page1.html')

@app.route('/hello')
def hello():
	return render_template("login.html")

@app.route('/page')
def page():
	return render_template("page2.html")



if __name__ == '__main__':
	app.run()