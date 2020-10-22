from .models import Profile
from django import forms

class NewProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['username']

class NewImageForm(forms.ModelForm):
    class Meta:
        model = Friend_Images
        exclude = ['usersubmitter','profile','comments','likes']
