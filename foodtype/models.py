from django.db import models


class Foodtype(models.Model):
    foodname = models.CharField(max_length=50, default='')

    def __str__(self):
        return self.foodname
