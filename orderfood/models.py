from datetime import date
from django.db import models
from branch.models import Branch
from menu.models import Menu



class Orderfood(models.Model):
    orderfooddate = models.DateField(default=date.today)
    orderfoodquantity = models.BigIntegerField()
    orderitemname = models.CharField(max_length=20, default='')
    orderfoodtotalamount = models.BigIntegerField()
    orderfoodbillno = models.CharField(max_length=20, default='')
    orderfoodstatus = models.CharField(max_length=20, default=0)
    menu_id = models.BigIntegerField()
    user_id = models.BigIntegerField()

    def __str__(self):
        return self.orderfoodbillno
