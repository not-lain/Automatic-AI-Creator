# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from distutils.log import debug
from flask import Flask, render_template, redirect, request
from flask import send_from_directory
from werkzeug.exceptions import RequestEntityTooLarge
from werkzeug.utils import secure_filename
import os



# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)
app.config['UPLOAD_DIRECTORY'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB
app.config['ALLOWED_EXTENSIONS'] = ['.jpg', '.jpeg', '.png', '.gif']


# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.
@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def hello_world():
	return render_template('index.html')




@app.route('/upload')
# ‘/’ URL is bound with hello_world() function.
def upload():
	return "upload"


# main driver function
if __name__ == '__main__':

	# run() method of Flask class runs the application
	# on the local development server.
	app.run(debug=True)
