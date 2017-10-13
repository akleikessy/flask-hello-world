#----Flask Hello World!---#

#import the Flask class from the flask package
from flask import Flask

#create an application object
app = Flask(__name__)

#use decorator patterns to link the view function to url

@app.route("/")
@app.route("/hello")

#define the view using a function, which returns a string

def hello_world():
	return "Hello, World!"

#start the development server using the run() method

if __name__ == "__main__":
	app.run()