# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 14:55:21 2018

@author: johny
"""

#from django.forms import ModelForm
from django import forms
#from efile.models import Efile_Upload

class UploadForm(forms.Form):
    #user_name = forms.CharField()
    #title_name = forms.CharField()
    #created_time = forms.DateTimeField()  # auto_now_add: admin also can't change the create time
    #update_time = forms.DateTimeField()  # auto_now: admin also can't change the update time
    file_url = forms.FileField()