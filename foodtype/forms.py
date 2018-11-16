from django import forms
from . import models


class foodtype_forms(forms.ModelForm):
    foodname = forms.CharField(
        required=True,
        label='foodname',
        max_length=30,
        widget=forms.TextInput(attrs={'pattern': '[A-Za-z ]+', 'title': 'enter character only'})
    )

    class Meta:
        model = models.Foodtype
        fields = ['foodname']