import numpy as np
import cv2
from keras.models import load_model

emotions = {0 : 'angry', 1 : 'disgusted', 2 : 'fearful', 3 : 'happy', 4 : 'neutral', 5 : 'sad', 6 : 'surprised'}


# Load the trained model
model = load_model('model.h5')

picture_size = 48
img = cv2.imread("PrivateTest_731447.jpg")

# Preprocessing the data
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
data = cv2.resize(gray_img, (picture_size, picture_size))
data = np.expand_dims(data, axis=-1)
data = np.expand_dims(data, axis=0)

predictions = model.predict(data)

print("Predicted emotion :",emotions[np.argmax(predictions)])