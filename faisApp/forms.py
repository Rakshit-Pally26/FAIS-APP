from django.db import models
from django.forms import ModelForm
from django import forms

class USStateForms(forms.Form):
    name = forms.CharField(max_length=100)
    code = forms.CharField(max_length=2)

class PhotoUploadForm(forms.Form):
    file = forms.ImageField(required=True)