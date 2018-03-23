from django import forms


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=20, required=True)
    password1 = forms.CharField(min_length=6, required=True)
    password2 = forms.CharField(min_length=6, required=True)
    email = forms.EmailField(max_length=30, required=True)

class LoginForm(forms.Form):
    username = forms.CharField(max_length=20, required=True)
    password = forms.CharField(required=True, min_length=5)
