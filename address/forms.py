from django import forms
from . import models


class address_forms(forms.ModelForm):
    address = forms.CharField(
        required=True,
        label='address',
        max_length=500,
        widget=forms.TextInput(attrs={'pattern': '[A-Za-z0-9 ]+', 'title': 'enter addressy'})
    )
    phone = forms.CharField(
        required=True,
        label='phone',
        max_length=10,
        widget=forms.TextInput(attrs={'pattern': '[0-9 ]+', 'title': 'enter digits only'})
    )
    class Meta:
        model = models.Address
        fields = ['address', 'phone']

