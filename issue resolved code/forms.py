from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,forms
from .models import *

class SignupForm(UserCreationForm):
    class Meta():
        model = User
        fields = ['username','first_name','last_name','email',]



#########################################################CHANGE

class AdminLoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

#########################################################CHANGE

class BlogForm(forms.ModelForm):
    class Meta():
        model = Blog
        fields = ['topic','image','blog','post_date',]
        exclude=['user']

