from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class UserLoginForm(forms.Form):
    email = forms.EmailField(max_length = 100)
    password = forms.CharField(max_length = 100)


class UserSignupForm(UserCreationForm):
    class Meta:
        fields = ("username", "email", "first_name", "last_name", "password1", "password2")
        model = get_user_model()


class UpdateForm(UserChangeForm):
    class Meta:
        fields = ("username", "email", "first_name", "last_name")
        exclude = ("password1","password2")
        model = get_user_model()