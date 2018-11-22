from datetime import date

from django.db import models
from user.models import User
from branch.models import Branch


class Feedback(models.Model):
    feedbackcontent = models.CharField(max_length=200, default='')
    feedbackdate = models.DateField(default=date.today)
    user_id = models.BigIntegerField()
    branch_id = models.ForeignKey(Branch, on_delete=models.CASCADE)

    def __str__(self):
        return self.feedbackcontent
