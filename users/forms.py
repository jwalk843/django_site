from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm): # inherits from user creation form
    email = forms.EmailField()

    class Meta:
        model = User # the model this form will interact with
        fields = ['username', 'email', 'password1', 'password2'] 