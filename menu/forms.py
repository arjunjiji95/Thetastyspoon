from django import forms
from . import models


class menu_forms(forms.ModelForm):
    menuname = forms.CharField(
        required=True,
        label='menuname',
        max_length=30,
        widget=forms.TextInput(attrs={'pattern': '[A-Za-z0-9 ]+', 'title': 'enter character only'})
    )
    menuprice = forms.CharField(
        required=True,
        label='menuprice',
        max_length=30,
        widget=forms.TextInput(attrs={'pattern': '[0-9 ]+', 'title': 'enter digits only'})
    )
    menudescription = forms.CharField(
        required=True,
        label='menudescription',
        max_length=30,
        widget=forms.TextInput(attrs={'pattern': '[A-Za-z0-9 ]+', 'title': 'enter description'})
    )

    class Meta:
        model = models.Menu
        fields = ['menuname', 'menuprice', 'menudescription', 'foodtype_id', 'menupic']