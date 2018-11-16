from django.db import models


class Table(models.Model):
    tableno = models.CharField(max_length=50, default='')
    seatno = models.CharField(max_length=10, default='')
    tablerate = models.CharField(max_length=50, default='')
    tablestatus = models.CharField(max_length=50, default='')
    branchmanager_id = models.BigIntegerField()

    def __str__(self):
        return self.tableno

