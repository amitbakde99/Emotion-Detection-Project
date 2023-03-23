from django.shortcuts import render, redirect
from .forms import *
from django.http import StreamingHttpResponse
from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.core.files.storage import FileSystemStorage
from .opencv_dlib import opencv_dlib
from .camera import VideoCamera
import numpy as np
import urllib
import json
import cv2
import os



# Create your views here.
def home(request):
	form = EmotionDetForm(request.POST, request.FILES) 
	if request.method == 'POST':
		if form.is_valid():
			post = form.save(commit=False)
			post.save()

			imageURL = settings.MEDIA_URL + form.instance.emotion_det_img.name
			print(imageURL)
			opencv_dlib(settings.MEDIA_ROOT_URL + imageURL)

			return render(request, 'emotion_detection.html', {'form': form, 'post': post, 'imageURL': imageURL})
	else:
		form = EmotionDetForm()
	return render(request,'emotion_detection.html', {'form' : form})  

def gen(camera):
	while True:
		frame = camera.get_frame()
		yield (b'--frame\r\n'
				b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

		
def facecam_feed(request):
	global x
	x = VideoCamera()
	return StreamingHttpResponse(gen(x),
					content_type='multipart/x-mixed-replace; boundary=frame')

def stopcam_feed(request):
	global x
	del x

