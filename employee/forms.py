from django import forms
from . import models


class employee_forms(forms.ModelForm):
    class Meta:
        model = models.Employee
        fields = ['employeename', 'employeehouse', 'employeeplace', 'employeecity', 'employeedistrict', 'employeestate',
                  'employeepin', 'employeedob', 'employeeage', 'employeedoj', 'employeecontact', 'employeeemail',
                  'employeeusername', 'employeepassword', 'stafftype_id']
