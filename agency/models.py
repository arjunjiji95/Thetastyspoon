from django.db import models


class Agency(models.Model):
    agencyname = models.CharField(max_length=20, default='')
    agencyplace = models.CharField(max_length=20, default='')
    agencycity = models.CharField(max_length=20, default='')
    agencydistrict = models.CharField(max_length=20, default='')
    agencypin = models.CharField(max_length=20, default='')
    agencycontact = models.CharField(max_length=20, default='')
    agencyemail = models.EmailField()
    branchmanager_id = models.BigIntegerField(default='')

    def __str__(self):
        return self.agencyname

