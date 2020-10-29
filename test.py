import sys
sys.path.append('/Users/Dell/AppData/Local/Programs/Python/Python37/Lib/site-packages')

from cv2 import cv2 #pip install opencv-python
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.python.keras.models import load_model
print("LOADING MODEL...")
reconstructed_model = load_model("./model_fire.h5")
def predict(img):
    img = cv2.resize(img, (224,224),  interpolation = cv2.INTER_NEAREST)
    img = img.reshape((1,) + img.shape)
    #print(img.shape)
    res = reconstructed_model.predict(img)
    return(float(res)) #0- Fire, 1- No- Fire
print("MODEL LOADED SUCCESSFULLY ")
cam = cv2.VideoCapture("./DataSets/Video/videoplayback.mp4")

while True:
    ret, img = cam.read()
    if ret==False:
        print("Something Went Wrong!")
        continue

    key_pressed = cv2.waitKey(1)&0xFF #Bitmasking to get last 8 bits
    if key_pressed==ord('q'):
        break
    #cv2.imshow("frame",img)
    result = predict(img)
    if result>0.50:
        print("No Fire")
        img = cv2.putText(img, 'NO FIRE', (50, 50) , cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0) , 1, cv2.LINE_AA)
        cv2.imshow("frame",img)
    elif result<0.50:
        print("Fire")
        img = cv2.putText(img, 'ALERT FIRE', (50, 50) , cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0) , 1, cv2.LINE_AA)
        cv2.imshow("frame",img)
    #print(result)
