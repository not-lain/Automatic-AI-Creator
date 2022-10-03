from flask import Flask, render_template, request
from keras.models import load_model
from keras.preprocessing import image
import os 
from PIL import Image
import cv2
import numpy as np
app = Flask(__name__)

dic = {0 : 'no', 1 : 'yes'}


model = load_model("model.h5")
# model._make_predict_function()

def predict_label(img_path):
	# i = cv2.imread('./static/img.jpeg')
	# i = i.resize(224,224)
	# i = i.reshape((1, 224,224,3))
	# p = model.predict_classes(i)
	# return dic[p[0]]
	return "yes"


# routes
@app.route("/", methods=['GET', 'POST'])
def kuch_bhi():
	return render_template("home.html")

@app.route("/about")
def about_page():
	return "About You..!!!"


@app.route("/submit", methods = ['GET', 'POST'])
def get_hours():
	if request.method == 'POST':
		img = request.files['my_image']
		img = Image.open(img)
		img.save('./static/img.jpeg')
		p = predict_label(img)



	return render_template("home.html", prediction = p, img_path = "static/img.jpeg")





if __name__ =='__main__':
	#app.debug = True
	app.run(debug = True)