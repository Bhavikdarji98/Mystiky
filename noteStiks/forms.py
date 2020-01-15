from django import forms

class Login(forms.Form):
    Email = forms.EmailField(widget=forms.EmailInput)
    Pass = forms.CharField(max_length=12, widget=forms.PasswordInput)

class NewRegister(forms.Form):
    FullName = forms.CharField(max_length=20)
    Email = forms.EmailField(widget=forms.EmailInput)
    Pass = forms.CharField(max_length=12, widget=forms.PasswordInput)