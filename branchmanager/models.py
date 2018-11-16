from datetime import date

from django.db import models
from branch.models import Branch



class Branchmanager(models.Model):
    branchmanagername = models.CharField(max_length=50, default='')
    branchmanagerhouse = models.CharField(max_length=50, default='')
    branchmanagerplace = models.CharField(max_length=50, default='')
    branchmanagercity = models.CharField(max_length=50, default='')
    branchmanagerdistrict = models.CharField(max_length=50, default='')
    branchmanagerstate = models.CharField(max_length=50, default='')
    branchmanagerpin = models.BigIntegerField(default='')
    branchmanagerdob = models.DateField(default=date.today)
    branchmanagerage = models.BigIntegerField(default='')
    branchmanagerdoj = models.DateField(default=date.today)
    branchmanagercontact = models.BigIntegerField(default='')
    branchmanageremail = models.CharField(max_length=50, default='')
    branchmanagerusername = models.CharField(max_length=50, default='')
    branchmanagerpassword = models.CharField(max_length=50, default='')
    branchmanagerstatus = models.BigIntegerField(default='')
    branch_id = models.ForeignKey(Branch, on_delete=models.CASCADE)

    def __str__(self):
        return self.branchmanagername


