from django.db import models
from foodtype.models import Foodtype


class Menu(models.Model):
    menuname = models.CharField(max_length=100, default='')
    menuprice = models.CharField(max_length=20, default='')
    menudescription = models.CharField(max_length=500, default='')
    menupic = models.ImageField(default='')
    foodtype_id = models.ForeignKey(Foodtype, on_delete=models.CASCADE)

    def __str__(self):
        return self.menuname


