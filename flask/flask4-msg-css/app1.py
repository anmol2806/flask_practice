from flask import *

app = Flask(__name__)


@app.route('/')
def abc():
	return render_template('login.html')


@app.route('/login' ,methods = ['POST'])
#def home():
#	return " Hi Champs of AIML "


def login():
	uname=request.form['uname']
	passwrd=request.form['pass']
	if uname== "ram" and passwrd=="sita":
		#return "Welcome %s" %uname
		return render_template('welcome.html',name=uname)
	elif uname== "ram" and passwrd!="sita":
		message="Incorrect password"
		return render_template('login.html',msg=message) 
	elif uname!= "ram" and passwrd=="sita":
		message="Incorrect username"
		return render_template('login.html',msg=message) 
	else : 
		message="Incorrect details"
		return render_template('login.html',msg=message) 
		#return " Invalid user " 
	
	
	
@app.route('/login/<uname>')
def welcome(uname):
	return render_template('welcome.html',name=uname)

if __name__ == '__main__':
	app.run()