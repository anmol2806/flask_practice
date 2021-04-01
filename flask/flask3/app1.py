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
	else : 
		
		return "Incorrect details " + render_template('login.html') +"retry"
		#return " Invalid user " 
	
	
	
@app.route('/login/<uname>')
def welcome(uname):
	return render_template('welcome.html',name=uname)

if __name__ == '__main__':
	app.run()