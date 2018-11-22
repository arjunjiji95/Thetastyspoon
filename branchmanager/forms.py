from django import forms
from . import models


class manager_forms(forms.ModelForm):
    branchmanagername = forms.CharField(
        required=True,
        label='branchmanagername',
        max_length=30,
        widget=forms.TextInput(attrs={'pattern': '[A-Za-z ]+', 'title': 'enter characters only'})
    )
    branchmanagerhouse = forms.CharField(
        required=True,
        label='branchmanagerhouse',
        max_length=30,
        widget=forms.TextInput(attrs={'pattern': '[A-Za-z ]+', 'title': 'enter characters only'})
    )
    branchmanagerplace = forms.CharField(
        required=True,
        label='branchmanagerplace',
        max_length=30,
        widget=forms.TextInput(attrs={'pattern': '[A-Za-z ]+', 'title': 'enter characters only'})
    )
    branchmanagercity = forms.CharField(
        required=True,
        label='branchmanagercity',
        max_length=30,
        widget=forms.TextInput(attrs={'pattern': '[A-Za-z ]+', 'title': 'enter characters only'})
    )
    branchmanagerdistrict = forms.CharField(
        required=True,
        label='branchmanagerdistrict',
        max_length=30,
        widget=forms.TextInput(attrs={'pattern': '[A-Za-z ]+', 'title': 'enter characters only'})
    )
    branchmanagerstate = forms.CharField(
        required=True,
        label='branchmanagerstate',
        max_length=30,
        widget=forms.TextInput(attrs={'pattern': '[A-Za-z ]+', 'title': 'enter characters only'})
    )
    branchmanagerpin = forms.CharField(
        required=True,
        label='branchmanagerpin',
        max_length=6,
        widget=forms.TextInput(attrs={'pattern': '[0-9 ]+', 'title': 'enter digits only'})
    )
    branchmanagerage = forms.CharField(
        required=True,
        label='branchmanagerage',
        max_length=2,
        widget=forms.TextInput(attrs={'pattern': '[0-9 ]+', 'title': 'enter digits only'})
    )
    branchmanagercontact = forms.CharField(
        required=True,
        label='branchmanagercontact',
        max_length=10,
        widget=forms.TextInput(attrs={'pattern': '[0-9 ]+', 'title': 'enter digits only'})
    )
    branchmanagerusername = forms.CharField(
        required=True,
        label='branchmanagerusername',
        max_length=32
    )

    branchmanagerpassword = forms.CharField(
        required=True,
        label='branchmanagerpassword',
        max_length=34,
        widget=forms.PasswordInput()

    )
    branchmanagerstatus = forms.CharField(
        required=True,
        label='branchmanagerstatus',
        max_length=10,
        widget=forms.TextInput(attrs={'pattern': '[0-9 ]+', 'title': 'enter digits only'})
    )
    class Meta:
        model = models.Branchmanager
        fields = ['branchmanagername', 'branchmanagerhouse', 'branchmanagerplace', 'branchmanagercity',
                  'branchmanagerdistrict', 'branchmanagerstate',
                  'branchmanagerpin', 'branchmanagerdob', 'branchmanagerage', 'branchmanagerdoj',
                  'branchmanagercontact', 'branchmanageremail',
                  'branchmanagerusername', 'branchmanagerpassword', 'branchmanagerstatus', 'branch_id']
