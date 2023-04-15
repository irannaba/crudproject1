from django.core import validators
from django import forms
from .models import Usertable
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class StudentRegistration(forms.ModelForm):
 class Meta:
  model = Usertable
  fields = ['name', 'task']
  widgets = {
   'name': forms.TextInput(attrs={'class':'form-control'}),
  #  'email': forms.EmailInput(attrs={'class':'form-control'}),
   'task': forms.TextInput(attrs={'class':'form-control'}),
  #  'password': forms.PasswordInput(render_value=True, attrs={'class':'form-control'}),
  }
  


class SignUpForm(UserCreationForm):
 password2 = forms.CharField(label='Confirm Password (again)', widget=forms.PasswordInput)
 class Meta:
  model = User
  fields = ['username', 'first_name', 'last_name', 'email']
  labels = {'email': 'Email'}