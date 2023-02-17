from .models import *
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']


class BlogForm(ModelForm):

    class Meta:
        model = Blog
        fields = '__all__'


class CommmentForm(ModelForm):

    class Meta:
        model = Comment
        fields = ['comment']
