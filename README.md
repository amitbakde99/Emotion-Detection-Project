# ZAF004_CV_EmotionDetection

### Methodology 

Model was trained on FER Dataset with 7 emotion classes - happy, sad, Angry, disgust, fear, surprise, neutral
Mobilenet Model was used with first 15 layers as non-trainable
Model was achieving an accuracy of 71 in train data and 61 in test data.
model.h5 has the best model weights
load_predict.py predicts a test image input using the best model
data zip folder has the dataset images for train and test

Dataset location: https://drive.google.com/file/d/1X60B-uR3NtqPd4oosdotpbDgy8KOfUdr/view
