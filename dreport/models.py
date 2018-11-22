from datetime import date

from django.db import models
from branch.models import Branch


class Dreport(models.Model):
    reportdate = models.DateField(default=date.today)
    tablecount = models.BigIntegerField()
    tableamt = models.BigIntegerField()
    foodcount = models.BigIntegerField()
    foodamt = models.BigIntegerField()
    pcount = models.BigIntegerField()
    pamt = models.BigIntegerField()
    branchmanager_id=models.BigIntegerField()

    def __str__(self):
        return self.reportdate
