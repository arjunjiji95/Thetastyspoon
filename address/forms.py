from django import forms
from . import models


class address_forms(forms.ModelForm):
    class Meta:
        model = models.Address
        fields = ['address', 'phone']

