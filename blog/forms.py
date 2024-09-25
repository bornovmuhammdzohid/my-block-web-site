from django import forms
from .models import *

from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class CreateUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"]


# class CreateUserForm(UserCreationForm):

#     class Meta:
#         model = get_user_model()
#         fields = ["email", "username", "password1", "password2"]


# class UserLoginForm(AuthenticationForm):

#     class Meta:
#         model = get_user_model()
#         fields = ["username", "password"]

# class DateInput(forms.DateInput):
#     input_type = 'date'

# class UserUpdateForm(forms.ModelForm):
    
#     class Meta:
#         model = get_user_model()
#         fields = ["username", "email"]

# class ProfileUpdateForm(forms.ModelForm):

#     class Meta:
#         model = Profile
#         fields = ['bio', 'phone_number', 'professional', 'avatar', 'about_me', 'age']