from django import forms
from branchmanager.models import Branchmanager


class manager_forms(forms.Form):
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
        model = Branchmanager
        fields = ['branchmanagerusername']
