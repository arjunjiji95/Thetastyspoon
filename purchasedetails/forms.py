from django import forms
from . import models

class purchasedetails_forms(forms.ModelForm):

   class Meta:
    model = models.Purchasedetails
    fields = ['itemname', 'itemquantity', 'itembasicrate']

