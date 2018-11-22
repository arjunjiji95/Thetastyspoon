from datetime import date

from django.db import models
from user.models import User
from branch.models import Branch


class Complaint(models.Model):
    complaintcontent = models.CharField(max_length=200, default='')
    complaintdate = models.DateField(default=date.today)
    user_id = models.BigIntegerField()
    branch_id = models.ForeignKey(Branch, on_delete=models.CASCADE)

    def __str__(self):
        return self.complaintcontent
