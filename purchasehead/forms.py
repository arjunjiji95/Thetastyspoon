from django import forms
from . import models


class purchasehead_forms(forms.ModelForm):
    purchaseinvoice = forms.CharField(
        required=True,
        label='purchaseinvoice',
        max_length=5,
        widget=forms.TextInput(attrs={'pattern': '[0-9 ]+', 'title': 'enter digits only'})
    )

    class Meta:
        model = models.Purchasehead
        fields = ['purchaseinvoice', 'purchasedate', 'agency_id']



