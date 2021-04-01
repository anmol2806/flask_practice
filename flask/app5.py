from flask import  *

#create object of required class
app = Flask(__name__)
# app is an object

@app.route('/')
def abc():
	return	render_template('login.html')

@app.route('/login',methods = ['POST'])
def login():
	uname=request.form['uname']
	passwrd=request.form['pass']
	if uname== "Anmol" and passwrd== "Nagpal":
		return render_template("index.html")
	else:
		return "Welcome %s" %uname


# in order to execute command app.run(),whenever the program is loaded
if __name__ =="__main__":
	app.run(debug=True)