from django import forms
from . import models


class table_forms(forms.ModelForm):
    tableno = forms.CharField(
        required=True,
        label='tableno',
        max_length=10,
        widget=forms.TextInput(attrs={'pattern': '[0-9 ]+', 'title': 'enter digits only'})
    )
    seatno = forms.CharField(
        required=True,
        label='seatno',
        max_length=10,
        widget=forms.TextInput(attrs={'pattern': '[0-9 ]+', 'title': 'enter digits only'})
    )
    tablerate = forms.CharField(
        required=True,
        label='tablerate',
        max_length=10,
        widget=forms.TextInput(attrs={'pattern': '[0-9 ]+', 'title': 'enter digits only'})
    )
    tablestatus = forms.CharField(
        required=True,
        label='tablestatus',
        max_length=10,
        widget=forms.TextInput(attrs={'pattern': '[0-9 ]+', 'title': 'enter digits only'})
    )
    class Meta:
        model = models.Table
        fields = ['tableno', 'seatno', 'tablerate', 'tablestatus']
