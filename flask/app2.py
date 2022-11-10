from flask import Flask, render_template, request
# from scipy.misc import save_img, imread, imresize
from PIL import Image
import numpy as np
import re
import sys
import os
import base64
import cv2
from skimage import io
from werkzeug.utils import secure_filename
# import logging





global graph, model


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = "static" 



@app.route('/')
def index_view():
    print(' ############# ', flush=True)
    print(' base ', flush=True)
    print(' ############# ', flush=True)
    return render_template('index.html')


def convertImage(imgData):
	print(' beginning of function ', flush=True)
	imgstr = re.search(b'base64,(.*)', imgData).group(1)
	print(' line 31 ', flush=True)
	print(' after re.search ', flush=True)
	with open('output.png', 'wb') as output:
		output.write(base64.b64decode(imgstr))
		print(' finished function ', flush=True)



@app.route('/submit', methods=['GET', 'POST'])
def predict():
	try:
		print(' ############# ', flush=True)
		print(' predict page ', flush=True)
		print(' ############# ', flush=True)
		imgData = request.get_data()
		print(' before function ', flush=True)
		print(' ############# ', flush=True)
		convertImage(imgData)
		print(' reshaping ... ', flush=True)
		x = Image.open('output.png')
		x = np.invert(x)
		x = x.resize((224,224), Image.ANTIALIAS)  
		x = x.reshape(1, 224, 224, 3)
		print(' ############# ', flush=True)
		print(' finished reshaping ', flush=True)
		print(' ############# ', flush=True)
		with graph.as_default():
			print(' predicting ... ', flush=True)
			out = model.predict(x)
			print(f"finished predicting with out = {out} ", flush=True)
			print(out)
			print(np.argmax(out, axis=1))

			response = np.array_str(np.argmax(out, axis=1))
	except :
		pass
	return "hello"


if __name__ == '__main__':
    app.run(debug=True, port=8000)
