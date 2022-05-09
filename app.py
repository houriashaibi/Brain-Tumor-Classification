from flask import Flask, render_template, request
from keras.models import load_model
from keras.preprocessing import image


from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D, Conv3D, BatchNormalization, Activation
from keras import backend as K
import os
from PIL import Image
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
import matplotlib.pyplot as plt
from matplotlib.pyplot import imshow
import pandas as pd
from path import PATH


app = Flask(__name__)

model = load_model('brain-tumor-model.h5')
classes = os.listdir(PATH+'Training')


def names(number):
    if(number == 0):
        return classes[0]
    elif(number == 1):
        return classes[1]
    elif(number == 2):
        return classes[2]
    elif(number == 3):
        return classes[3]

#dic = {0 : 'glioma_tumor', 1 : 'meningioma_tumor', 2 : 'no_tumor', 3 : 'pituitary_tumor'}
#model = load_model('brain-tumor-model.h5')

model.make_predict_function()

def predict_label(img_path):
	#i = image.load_img(img_path, target_size=(150,150))
	#i = image.img_to_array(i)/255.0
	#i = i.reshape(1, 150,150,3)
	#p = (model.predict(i) > 0.5).astype("int32")
	#return dic[p[0]]
    img = image.load_img(img_path)
    x = np.array(img.resize((150,150)))
    x = x.reshape(1,150,150,3)
    p = model.predict_on_batch(x)
    classification = np.where(p == np.amax(p))[1][0]
    return names(classification)


# routes
@app.route("/", methods=['GET', 'POST'])
def main():
	return render_template("index.html")

@app.route("/about")
def about_page():
	return "..!!!"

@app.route("/submit", methods = ['GET', 'POST'])
def get_output():
	if request.method == 'POST':
		img = request.files['my_image']

		img_path = "static/" + img.filename	
		img.save(img_path)

		p = predict_label(img_path)

	return render_template("index.html", prediction = p, img_path = img_path)


if __name__ =='__main__':
	#app.debug = True
    
    app.run()
