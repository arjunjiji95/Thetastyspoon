from django import forms
from . import models


class orderfood_forms(forms.ModelForm):
    class Meta:
        model = models.Orderfood
        fields = ['orderfooddate', 'orderfoodquantity','orderfoodbillno']

