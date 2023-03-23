# forms.py
from django import forms
from .models import *

class EmotionDetForm(forms.ModelForm):

	class Meta:
		model = EmotionDet
		fields = ['emotion_det_img']
