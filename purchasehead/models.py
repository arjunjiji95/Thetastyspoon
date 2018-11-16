from datetime import date

from django.db import models
from agency.models import Agency


class Purchasehead(models.Model):
    purchaseinvoice = models.CharField(max_length=20, default='')
    purchasedate = models.DateField(default=date.today)
    purchasegrandtotal = models.CharField(max_length=20, default='')
    agency_id = models.ForeignKey(Agency, on_delete=models.CASCADE)
    branchmanager_id=models.BigIntegerField()

    def __str__(self):
        return self.purchaseinvoice



