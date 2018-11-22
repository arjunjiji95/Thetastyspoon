from django import forms
from . import models


class tablebook_forms(forms.ModelForm):

    class Meta:
        model = models.Tablebook
        fields = ['bookingdate', 'bookingtime']