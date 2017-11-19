from django import forms


class UserLoginForm(forms.Form):
    email = forms.EmailField(max_length = 100)
    password = forms.CharField(max_length = 100)