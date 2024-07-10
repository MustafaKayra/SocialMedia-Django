from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class RegisterForm(UserCreationForm):
    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 != password2:
            raise ValidationError("Password do not match!")
        
        return cleaned_data

    class Meta():
        model = User
        fields = ['username','first_name','password1','password2','email']


class LoginForm(forms.Form):
    username = forms.CharField(label="Username")
    password1 = forms.CharField(label="Password",widget=forms.PasswordInput)

class UpdateUserTestForm(forms.Form):
    password1 = forms.CharField(label="Password",widget=forms.PasswordInput)