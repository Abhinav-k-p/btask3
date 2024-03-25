
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *

class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200)
    user_type = forms.ChoiceField(choices= Users.USER_TYPE_CHOICES, label='Select User Type')
    


    class Meta:
        model = Users
        fields = ('username', 'email', 'password1', 'password2', 'user_type')

