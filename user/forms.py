from django import forms
from . import models


class user_forms(forms.ModelForm):

    class Meta:
        model = models.User
        fields = ['username', 'userhouse', 'userplace', 'usercity', 'userdistrict', 'userstate', 'userpin', 'usercontact', 'useremail', 'userusername', 'userpassword']