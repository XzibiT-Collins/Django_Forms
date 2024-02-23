from django import forms
from user_app.models import userProfileInfo
from django.contrib.auth.models import User


class userInfo(forms.ModelForm):
    password = forms.PasswordInput
    class Meta():
        model = User
        fields = ('username','email','password')


class userProfileInfoForm(forms.ModelForm):
    class Meta():
        model = userProfileInfo
        fields = ('profile_pic','profile_link')