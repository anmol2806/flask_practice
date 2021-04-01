# import module/package
from flask import Flask

#create object of required class
app = Flask(__name__)
# app is an object


@app.route('/home/')
def index1():
    return "Hello I am root"


@app.route('/')
def index():
    return "Hello 122"

# in order to execute command app.run(),whenever the program is loaded
if __name__ =="__main__":
	app.run()