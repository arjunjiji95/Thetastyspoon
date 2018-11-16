from datetime import date

from django.db import models
from branchmanager.models import Branchmanager
from stafftype.models import Stafftype


class Employee(models.Model):
    employeename = models.CharField(max_length=20, default='')
    employeehouse = models.CharField(max_length=50, default='')
    employeeplace = models.CharField(max_length=20, default='')
    employeecity = models.CharField(max_length=20, default='')
    employeedistrict = models.CharField(max_length=20, default='')
    employeestate = models.CharField(max_length=20, default='')
    employeepin = models.CharField(max_length=20, default='')
    employeedob = models.DateField(default=date.today)
    employeeage = models.CharField(max_length=20, default='')
    employeedoj = models.DateField(default=date.today)
    employeecontact = models.CharField(max_length=20, default='')
    employeeemail = models.CharField(max_length=50, default='')
    employeeusername = models.CharField(max_length=20, default='')
    employeepassword = models.CharField(max_length=20, default='')
    stafftype_id = models.ForeignKey(Stafftype, on_delete=models.CASCADE)
    branchmanager_id = models.BigIntegerField()

    def __str__(self):
        return self.employeename


