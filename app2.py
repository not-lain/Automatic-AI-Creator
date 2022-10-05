from flask import Flask, render_template, request
# from scipy.misc import save_img, imread, imresize
import numpy as np
import re
import sys
import os
import base64


global graph, model


app = Flask(__name__)


@app.route('/')
def index_view():
    return render_template('index.html')


def convertImage(imgData):
	imgstr = re.search(b'base64,(.*)', imgData).group(1)
	with open('output.png', 'wb') as output:
	    output.write(base64.b64decode(imgstr))


@app.route('/predict/', methods=['GET', 'POST'])
def predict():
	imgData = request.get_data()
	convertImage(imgData)
	x = imread('output.png', mode='L')
	x = np.invert(x)
	x = imresize(x, (224, 224))
	x = x.reshape(1, 224, 224, 3)

	with graph.as_default():
		out = model.predict(x)
		print(out)
		print(np.argmax(out, axis=1))

		response = np.array_str(np.argmax(out, axis=1))
		return response


if __name__ == '__main__':
    app.run(debug=True, port=8000)
