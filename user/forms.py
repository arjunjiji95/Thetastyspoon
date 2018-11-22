from django import forms
from . import models


class user_forms(forms.ModelForm):
    username = forms.CharField(
        required=True,
        label='username',
        max_length=30,
        widget=forms.TextInput(attrs={'pattern': '[A-Za-z ]+', 'title': 'enter characters only'})
    )
    userhouse = forms.CharField(
        required=True,
        label='userhouse',
        max_length=30,
        widget=forms.TextInput(attrs={'pattern': '[A-Za-z ]+', 'title': 'enter characters only'})
    )
    userplace = forms.CharField(
        required=True,
        label='userplace',
        max_length=30,
        widget=forms.TextInput(attrs={'pattern': '[A-Za-z ]+', 'title': 'enter characters only'})
    )
    usercity = forms.CharField(
        required=True,
        label='usercity',
        max_length=30,
        widget=forms.TextInput(attrs={'pattern': '[A-Za-z ]+', 'title': 'enter characters only'})
    )
    userdistrict = forms.CharField(
        required=True,
        label='userdistrict',
        max_length=30,
        widget=forms.TextInput(attrs={'pattern': '[A-Za-z ]+', 'title': 'enter characters only'})
    )
    userstate = forms.CharField(
        required=True,
        label='userstate',
        max_length=30,
        widget=forms.TextInput(attrs={'pattern': '[A-Za-z ]+', 'title': 'enter characters only'})
    )
    userpin = forms.CharField(
        required=True,
        label='userpin',
        max_length=6,
        widget=forms.TextInput(attrs={'pattern': '[0-9 ]+', 'title': 'enter digits only'})
    )
    usercontact = forms.CharField(
        required=True,
        label='usercontact',
        max_length=10,
        widget=forms.TextInput(attrs={'pattern': '[0-9 ]+', 'title': 'enter digits only'})
    )
    userusername = forms.CharField(
        required=True,
        label='userusername',
        max_length=32
    )

    userpassword = forms.CharField(
        required=True,
        label='userpassword',
        max_length=34,
        widget=forms.PasswordInput()

    )

    class Meta:
        model = models.User
        fields = ['username', 'userhouse', 'userplace', 'usercity', 'userdistrict', 'userstate', 'userpin', 'usercontact', 'useremail', 'userusername', 'userpassword']