# Fire-Detection-and-Alert-System
Gdrive Link : https://drive.google.com/drive/folders/1lVBkZrROC2fTk5H0ti8iy83XRuSr5oAN?usp=sharing

![REALTIME TESTING]( /image.gif "TESTING")<!-- .element height="100%" width="150%" -->

This Project takes input (Image) from sources like Camera attached to drone, CCTV camera, or mobile app, and predicts the chance of Fire or Smoke in the images. The Project uses a Convolutional Neural Network, The CNN was trained on Images containing Manually cropped scenes of Forest Fires, Dark Smoke, Fire in Buildings, Fire in Farms, etc and Images which don't have fire.

## Model
Model: "sequential"
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
conv2d (Conv2D)              (None, 222, 222, 32)      896       
_________________________________________________________________
conv2d_1 (Conv2D)            (None, 220, 220, 64)      18496     
_________________________________________________________________
max_pooling2d (MaxPooling2D) (None, 110, 110, 64)      0         
_________________________________________________________________
dropout (Dropout)            (None, 110, 110, 64)      0         
_________________________________________________________________
conv2d_2 (Conv2D)            (None, 108, 108, 64)      36928     
_________________________________________________________________
max_pooling2d_1 (MaxPooling2 (None, 54, 54, 64)        0         
_________________________________________________________________
dropout_1 (Dropout)          (None, 54, 54, 64)        0         
_________________________________________________________________
conv2d_3 (Conv2D)            (None, 52, 52, 128)       73856     
_________________________________________________________________
max_pooling2d_2 (MaxPooling2 (None, 26, 26, 128)       0         
_________________________________________________________________
dropout_2 (Dropout)          (None, 26, 26, 128)       0         
_________________________________________________________________
conv2d_4 (Conv2D)            (None, 24, 24, 128)       147584    
_________________________________________________________________
max_pooling2d_3 (MaxPooling2 (None, 12, 12, 128)       0         
_________________________________________________________________
dropout_3 (Dropout)          (None, 12, 12, 128)       0         
_________________________________________________________________
flatten (Flatten)            (None, 18432)             0         
_________________________________________________________________
dense (Dense)                (None, 128)               2359424   
_________________________________________________________________
dense_1 (Dense)              (None, 64)                8256      
_________________________________________________________________
dense_2 (Dense)              (None, 32)                2080      
_________________________________________________________________
dropout_4 (Dropout)          (None, 32)                0         
_________________________________________________________________
dense_3 (Dense)              (None, 1)                 33        
=================================================================
Total params: 2,647,553
Trainable params: 2,647,553
Non-trainable params: 0
_________________________________________________________________

## Results
### ACCURACY
![Accuracy]( /Images/acc.png "Accuracy")
### LOSS
![Loss]( /Images/loss.png "Loss")

## References
1. https://breckon.org/toby/publications/papers/dunnings18fire.pdf

2. https://breckon.org/toby/publications/papers/samarth19fire.pdf

3. https://github.com/tobybreckon/fire-detection-cnn

4. https://www.pyimagesearch.com/2019/11/18/fire-and-smoke-detection-with-keras-and-deep-learning/

5. https://www.kaggle.com/delllectron/fire-detection-computer-vision

6. https://www.tensorflow.org/api_docs/python/tf/keras

7. https://docs.opencv.org/master/d6/d00/tutorial_py_root.html

