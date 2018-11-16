from django import forms
from user.models import User


class login_forms(forms.Form):
    username = forms.CharField(
        required=True,
        label='username',
        max_length=32
    )

    password = forms.CharField(
        required=True,
        label='password',
        max_length=34,
        widget=forms.PasswordInput()

    )

    class Meta:
        model = User
        fields = ['username']