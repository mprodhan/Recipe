'''
    1. Use the UserCreationForm on class SignUpForm
    2. Extend email and display_name on the fields, under class Meta of SignUpForm
    3. Simple Form for class LoginForm.

 '''

from django import forms
from django.contrib.auth.forms import UserCreationForm

from recipe_user.models import RecipeUser

class SignUpForm(UserCreationForm):
    display_name = forms.CharField(max_length=30)

    class Meta:
        model = RecipeUser
        fields = ('email', 'display_name', 'password1', 'password2')

class LoginForm(forms.Form):
    email = forms.EmailField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)


