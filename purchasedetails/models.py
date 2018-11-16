from django.db import models


class Purchasedetails(models.Model):
    itemname = models.CharField(max_length=20, default='')
    itemquantity = models.CharField(max_length=20, default='')
    itembasicrate = models.CharField(max_length=20, default='')
    itemunittotal = models.BigIntegerField()
    purchaseinvoice = models.BigIntegerField()

    def __str__(self):
        return self.itemname
