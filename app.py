import os
#import matplotlib.pyplot as plt
#Define backend as tensorflow
os.environ['KERAS_BACKEND']='tensorflow'
#It is important to import keras after changing backend
import keras
from flask import Flask, render_template,request
from scipy.misc import imsave, imread, imresize
import numpy as np
#import keras.models
import re
from PIL import Image

import sys 
sys.path.append(os.path.abspath("./model"))
from load import * 


app = Flask(__name__)

global model, graph

model, graph = init()
	
#def convertImage(imgData1):
#	imgstr = re.search(r'base64,(.*)',imgData1).group(1)
#	print(imgstr)
#	with open('output'+str(i)+'.png','wb') as output:
#		output.write(imgstr.decode('base64'))
	

@app.route('/') 
def index():
	return render_template("index.html")

@app.route('/predict/',methods=['GET','POST'])
def predict():
	#imgData = request.get_data()
	#convertImage(imgData)	
	i=np.random.randint(10)
	x = imread('output'+str(i)+'.png',mode='L')
	
	img_in = imresize(x,(28,14))
	# inp=img_in[6:7]
	# print img_in.shape
	img_in =img_in.reshape((1,392))
	
	
	with graph.as_default():
		    img_inp = img_in.reshape((28,14))
		    pred = model.predict([img_in,np.zeros_like(img_in)])
		    pred=np.array(pred[0])
		    img_out = pred.reshape((28,14))
	
		    # axarr[1].imshow(img_inp)
		    # axarr[0].imshow(img)
		   
		    imsave('./static/a.png', img_inp)
		    imsave('./static/b.png', img_out)
		    return ' '
		    # return base64encode(img_inp), base64encode(img)
		 
	
		 
	

if __name__ == "__main__":
	#decide what port to run the app in
	#port = int(os.environ.get('PORT', 5000))

	#run the app locally on the givn port
	app.run(host='127.0.0.1', port=1245)



