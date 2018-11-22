from datetime import date

from django.db import models
from branch.models import Branch
from tabledetails.models import Table




class Tablebook(models.Model):
    bookingdate = models.DateField(default=date.today)
    bookingtime = models.CharField(max_length=20, default='')
    #bookingrate = models.CharField(max_length=20, default='')
    #bookingstatus = models.CharField(max_length=20, default='')
    tablerate = models.BigIntegerField()
    tableno = models.BigIntegerField()
    seatno = models.BigIntegerField()
    branch_id = models.BigIntegerField()
    table_id = models.BigIntegerField()
    user_id = models.BigIntegerField()


    def __str__(self):
        return self.bookingrate

