from django.db import models
import os

# Create your models here.

class EmotionDet(models.Model):
    emotion_det_img = models.ImageField(upload_to='emotion_detection/images/%Y/%m/%d')