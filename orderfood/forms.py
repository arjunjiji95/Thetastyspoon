from django import forms
from . import models


class orderfood_forms(forms.ModelForm):
    orderfoodquantity = forms.CharField(
        required=True,
        label='orderfoodquantity',
        max_length=10,
        widget=forms.TextInput(attrs={'pattern': '[0-9 ]+', 'title': 'enter digits only'})
    )
    orderfoodbillno = forms.CharField(
        required=True,
        label='orderfoodbillno',
        max_length=5,
        widget=forms.TextInput(attrs={'pattern': '[0-9 ]+', 'title': 'enter digits only'})
    )
    class Meta:
        model = models.Orderfood
        fields = ['orderfooddate', 'orderfoodquantity','orderfoodbillno']

