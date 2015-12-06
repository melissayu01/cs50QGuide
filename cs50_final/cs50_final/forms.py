"""
Django forms for cs50_final project.

Creates fields for each form used on the website.

Melissa Yu, Phillip Yu
"""

from django import forms
from django.forms import ModelForm
from search.models import *
from django.core.exceptions import ValidationError

# creates registration form fields
class NewUser(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=30,
        widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(label='Last Name', max_length=30,
        widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    username = forms.CharField(label='Desired username', max_length=30,
        widget=forms.TextInput(attrs={'placeholder': 'Username'})) # make sure to later check that this is new
    email = forms.EmailField(label='Your e-mail', 
        widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(max_length=32, widget=forms.PasswordInput(render_value=False, attrs={'placeholder': 'Password'}))
    confirm = forms.CharField(max_length=32, widget=forms.PasswordInput(render_value=False, attrs={'placeholder': 'Confirm Password'}))
    
# creates login form fields
class LogIn(forms.Form):
    username = forms.CharField(label='Username', max_length=30, 
        widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(max_length=32, widget=(forms.PasswordInput(render_value=False, attrs={'placeholder': 'Password'})))

# creates rating form fields
class Rate(forms.Form):
    review = forms.CharField(label='Review', max_length=2000, required=False,
        widget=forms.Textarea(attrs={'placeholder': 'Type comments here. (optional)'}))
    rating = forms.ChoiceField(label="Club Rating", choices=(('1', '1'),('2', '2'),('3', '3'),('4', '4'),('5','5')))
