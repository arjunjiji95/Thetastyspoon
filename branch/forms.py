from django import forms
from . import models


class branch_forms(forms.ModelForm):
    branchname = forms.CharField(
        required=True,
        label='branchname',
        max_length=30,
        widget=forms.TextInput(attrs={'pattern': '[A-Za-z ]+', 'title': 'enter characters only'})
    )
    branchplace = forms.CharField(
        required=True,
        label='branchplace',
        max_length=30,
        widget=forms.TextInput(attrs={'pattern': '[A-Za-z ]+', 'title': 'enter characters only'})
    )
    branchcity = forms.CharField(
        required=True,
        label='branchcity',
        max_length=30,
        widget=forms.TextInput(attrs={'pattern': '[A-Za-z ]+', 'title': 'enter characters only'})
    )
    branchdistrict = forms.CharField(
        required=True,
        label='branchdistrict',
        max_length=30,
        widget=forms.TextInput(attrs={'pattern': '[A-Za-z ]+', 'title': 'enter characters only'})
    )
    branchpin = forms.CharField(
        required=True,
        label='branchpin',
        max_length=6,
        widget=forms.TextInput(attrs={'pattern': '[0-9 ]+', 'title': 'enter digits only'})
    )
    branchcontact = forms.CharField(
        required=True,
        label='branchcontact',
        max_length=10,
        widget=forms.TextInput(attrs={'pattern': '[0-9 ]+', 'title': 'enter digits only'})
    )

    class Meta:
        model = models.Branch
        fields = ['branchname', 'branchplace', 'branchcity', 'branchdistrict', 'branchpin', 'branchcontact', 'branchemail']