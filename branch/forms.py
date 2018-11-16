from django import forms
from . import models


class branch_forms(forms.ModelForm):

    class Meta:
        model = models.Branch
        fields = ['branchname', 'branchplace', 'branchcity', 'branchdistrict', 'branchpin', 'branchcontact', 'branchemail']