# import module/package
from flask import Flask

#create object of required class
app = Flask(__name__)
# app is an object


@app.route('/')
def index():
    return "<html><h1>Hello</h1></html>"

# in order to execute command app.run(),whenever the program is loaded
if __name__ =="__main__":
	app.run()