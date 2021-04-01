from flask import *

app = Flask(__name__)
@app.route('/')
def abc():
	return render_template('login.html')

@app.route('/login',methods = ['POST'])
def login():
	uname=request.form['uname']
	passwrd=request.form['pass']
	if uname== "ram" and passwrd=="sita":
		#return "Welcome %s" %uname
		return render_template('welcome.html')

	elif uname== "ram" and passwrd!="sita":
		message='Incorrect Password'
		return render_template('login.html',msg=message)

	elif uname!= "ram" and passwrd=="sita":
		message='Incorrect name'
		return render_template('login.html',msg=message)
	else : 
		message='incorrect credentials'
		return render_template('login.html',msg=message)
		#return " Invalid user " 

if __name__ == '__main__':
	app.run()