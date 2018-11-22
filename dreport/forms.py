from django import forms
from . import models


class dreport_forms(forms.ModelForm):
    tablecount = forms.CharField(
        required=True,
        label='tablecount',
        max_length=20,
        widget=forms.TextInput(attrs={'pattern': '[0-9 ]+', 'title': 'enter digits only'})
    )
    tableamt = forms.CharField(
        required=True,
        label='tableamt',
        max_length=10,
        widget=forms.TextInput(attrs={'pattern': '[0-9 ]+', 'title': 'enter digits only'})
    )
    foodcount = forms.CharField(
        required=True,
        label='foodcount',
        max_length=20,
        widget=forms.TextInput(attrs={'pattern': '[0-9 ]+', 'title': 'enter digits only'})
    )
    foodamt = forms.CharField(
        required=True,
        label='foodamt',
        max_length=10,
        widget=forms.TextInput(attrs={'pattern': '[0-9 ]+', 'title': 'enter digits only'})
    )
    pcount = forms.CharField(
        required=True,
        label='pcount',
        max_length=20,
        widget=forms.TextInput(attrs={'pattern': '[0-9 ]+', 'title': 'enter digits only'})
    )
    pamt = forms.CharField(
        required=True,
        label='pamt',
        max_length=10,
        widget=forms.TextInput(attrs={'pattern': '[0-9 ]+', 'title': 'enter digits only'})
    )

    class Meta:
        model = models.Dreport
        fields = ['reportdate', 'tablecount', 'tableamt', 'foodcount', 'foodamt', 'pcount', 'pamt']