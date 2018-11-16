from django import forms
from . import models


class table_forms(forms.ModelForm):
    class Meta:
        model = models.Table
        fields = ['tableno', 'seatno', 'tablerate', 'tablestatus']
