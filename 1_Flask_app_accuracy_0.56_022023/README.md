# Emotion Detection using Deep Learning

## Introduction

This project aims to classify the emotion on a person's face into one of **seven categories**, using deep convolutional neural networks. The model is trained on the **FER-2013** dataset which was published on International Conference on Machine Learning (ICML). This dataset consists of 35887 grayscale, 48x48 sized face images with **seven emotions** - angry, disgusted, fearful, happy, neutral, sad and surprised.

## Dependencies

* Python 3, [OpenCV](https://opencv.org/), [Tensorflow](https://www.tensorflow.org/)
* To install the required packages, run `pip install -r requirements.txt`.

## Model

[Emotion Detction Notebook](https://github.com/amitbakde99/Emotion-Detection-Project/blob/main/Emotion_Detection.ipynb)

The repository is currently compatible with `tensorflow-2.0` and makes use of the Keras API using the `tensorflow.keras` library.

* This implementation by default detects emotions on all faces in the webcam feed. With a simple 4-layer CNN, the test accuracy reached 60% in 20 epochs.
* About [Training and Validation Loss](https://github.com/amitbakde99/Emotion-Detection-Project/blob/main/Training%20and%20Validation%20Loss.md)

![my image](https://github.com/amitbakde99/Emotion-Detection-Project/blob/main/imgs/Screenshot%202022-12-23%20122412.jpg)

## Review of the Dataset FER 2013

* The dataset is not realistic because as we can observe background is white and this is very crystal clear image and we can just observe the image based on their facial expression it is easily can be classified, if we for example train our deep learning model on this plain images and then we deploy it in the real time environment, then our model will definitely fail. Because all of the previous images on which we trained our deep learning model was front looking image but this will not be in the real case. Thats why dataset should be realistic. On this dataset the accuracy will be low due to above mention reasons.

![alt text](https://github.com/amitbakde99/Emotion-Detection-Project/blob/main/imgs/Screenshot%202022-12-23%20122231.jpg)

* There is imbalance problem in dataset, as we can see happy images are in highest numbers of 1774 and for disgusted we only have 111 files. Typically deep learning architecture must have same size of classes ideally. If it is not then deep learning architecture will be biased towards the happy class for example. it will not be robust for digusted and accuracy will be lower towrds the same. Solution to this is data augumentation. We can increase the images by rotating the images, scale the images zoom in zoom out and other combinations. We can also use GANs to produce more files.
* Intra class variations means some images are of human but,some are paintings, cartoons.
* Occulusion means some images the faces are hidden by hands or by eyeglasses.
* Contrast variations means some images have more contrast or less contrast which will effect the accuracy of the model. 
* Outliers means some images are completely unrelated with the class they are present in.


## Algorithm

* First, the **haar cascade** method is used to detect faces in each frame of the webcam feed.

* The region of image containing the face is resized to **48x48** and is passed as input to the CNN.

* The network outputs a list of **softmax scores** for the seven classes of emotions.

* The emotion with maximum score is displayed on the screen.


## Flask App

This Webpage takes the image from the user and predict the emotion with the help of deep learning model which is integrated at the backend.

Results

![image](https://github.com/amitbakde99/Emotion-Detection-Project/blob/main/imgs/Screenshot%202022-12-23%20130558.jpg)

## References

* "Challenges in Representation Learning: A report on three machine learning contests." I Goodfellow, D Erhan, PL Carrier, A Courville, M Mirza, B
   Hamner, W Cukierski, Y Tang, DH Lee, Y Zhou, C Ramaiah, F Feng, R Li,  
   X Wang, D Athanasakis, J Shawe-Taylor, M Milakov, J Park, R Ionescu,
   M Popescu, C Grozea, J Bergstra, J Xie, L Romaszko, B Xu, Z Chuang, and
   Y. Bengio. arXiv 2013.
