from django import forms

class RegForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(max_length=20, widget=forms.PasswordInput())
    conf_password = forms.CharField(max_length=20, widget=forms.PasswordInput())
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    emailid = forms.EmailField()
    mobileno = forms.IntegerField()

class LoginForm(forms.Form):
        username = forms.CharField(max_length=20)
        password = forms.CharField(max_length=20, widget=forms.PasswordInput())