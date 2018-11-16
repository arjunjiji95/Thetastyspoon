from django import forms
from . import models


class agency_forms(forms.ModelForm):
    agencyname = forms.CharField(
        required=True,
        label='agencyname',
        max_length=30,
        widget=forms.TextInput(attrs={'pattern': '[A-Za-z ]+', 'title': 'enter characters only'})
    )
    agencyplace = forms.CharField(
        required=True,
        label='agencyplace',
        max_length=30,
        widget=forms.TextInput(attrs={'pattern': '[A-Za-z ]+', 'title': 'enter characters only'})
    )
    agencycity = forms.CharField(
        required=True,
        label='agencycity',
        max_length=30,
        widget=forms.TextInput(attrs={'pattern': '[A-Za-z ]+', 'title': 'enter characters only'})
    )
    agencydistrict = forms.CharField(
        required=True,
        label='agencydistrict',
        max_length=30,
        widget=forms.TextInput(attrs={'pattern': '[A-Za-z ]+', 'title': 'enter characters only'})
    )
    agencypin = forms.CharField(
        required=True,
        label='agencypin',
        max_length=6,
        widget=forms.TextInput(attrs={'pattern': '[0-9 ]+', 'title': 'enter digits only'})
    )
    agencycontact = forms.CharField(
        required=True,
        label='agencycontact',
        max_length=6,
        widget=forms.TextInput(attrs={'pattern': '[0-9 ]+', 'title': 'enter digits only'})
    )
    class Meta:
        model = models.Agency
        fields = ['agencyname', 'agencyplace', 'agencycity', 'agencydistrict', 'agencypin', 'agencycontact',
                  'agencyemail']
