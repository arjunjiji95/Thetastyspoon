from django.db import models


class Branch(models.Model):

    branchname = models.CharField(max_length=30, default='')
    branchplace = models.CharField(max_length=20, default='')
    branchcity = models.CharField(max_length=20, default='')
    branchdistrict = models.CharField(max_length=20, default='')
    branchpin = models.CharField(max_length=20, default='')
    branchcontact = models.CharField(max_length=10, default='')
    branchemail = models.CharField(max_length=20, default='')

    def __str__(self):
        return self.branchname

