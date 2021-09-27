from django import forms
from django.contrib.auth.models import User

class RegisterForm(forms.ModelForm):
    username=forms.CharField(label="Username")
    password = forms.CharField(label="Password", widget=forms.PasswordInput())
    email = forms.EmailField(label="E-mail", required=True)
    confirm_password = forms.CharField(label="Password-Confirm", widget=forms.PasswordInput())
    class Meta:
        model=User
        fields=["email", "username","password"]

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs = {"class": "form-control"}

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        confirm_password = self.cleaned_data.get("confirm_password")
        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match!")
        values = {
            "username" : username,
            "password" : password
        }
        return values

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 8:
            raise forms.ValidationError("your password cannot be less than 8 characters.")
        return password

    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username = username)
        if qs.exists():
            raise forms.ValidationError("This username is registered!Try another username")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email exists")
        return email

class LoginForm(forms.Form):
    username=forms.CharField(label="Username")
    password=forms.CharField(label="Password", widget=forms.PasswordInput())
    class Meta:
        model=User
        fields=["username","password"]
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs = {"class": "form-control"}
