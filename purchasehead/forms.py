from django import forms
from . import models


class purchasehead_forms(forms.ModelForm):

    class Meta:
        model = models.Purchasehead
        fields = ['purchaseinvoice', 'purchasedate', 'agency_id']



