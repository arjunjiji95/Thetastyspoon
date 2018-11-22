from django.db import models


class Table(models.Model):
    tableno = models.BigIntegerField()
    seatno = models.BigIntegerField()
    tablerate = models.BigIntegerField()
    tablestatus = models.CharField(max_length=50, default='')
    branchmanager_id = models.BigIntegerField()

    def __str__(self):
        return self.tableno

