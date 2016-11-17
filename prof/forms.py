from django import forms
from django.forms import ModelForm
from .models import RegisterProfile, RegisterCourse 
from django.db import models
from django.contrib.auth.models import User


class Register(forms.ModelForm):
    class Meta:
        model = RegisterProfile
        fields = '__all__'

class RegisterCourse(forms.ModelForm):
    class Meta:
        model = RegisterCourse
        fields = '__all__'

class ApplyJobs(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=50)
    cv_file = forms.FileField()
    mobile = forms.CharField(max_length=20)
    message = forms.CharField(widget=forms.Textarea)
