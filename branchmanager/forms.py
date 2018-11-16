from django import forms
from . import models


class manager_forms(forms.ModelForm):
    class Meta:
        model = models.Branchmanager
        fields = ['branchmanagername', 'branchmanagerhouse', 'branchmanagerplace', 'branchmanagercity',
                  'branchmanagerdistrict', 'branchmanagerstate',
                  'branchmanagerpin', 'branchmanagerdob', 'branchmanagerage', 'branchmanagerdoj',
                  'branchmanagercontact', 'branchmanageremail',
                  'branchmanagerusername', 'branchmanagerpassword', 'branchmanagerstatus', 'branch_id']
