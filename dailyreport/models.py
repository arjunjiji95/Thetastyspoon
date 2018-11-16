from datetime import date

from django.db import models


class Dailyreport(models.Model):
    reportdate = models.DateField(default=date.today)

    def __str__(self):
        return self.reportdate