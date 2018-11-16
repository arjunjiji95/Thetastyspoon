from django import forms
from . import models


class dailyreport_forms(forms.ModelForm):

    class Meta:
        model = models.Dailyreport
        fields = ['reportdate']