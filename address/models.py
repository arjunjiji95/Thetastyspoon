from django.db import models

class Address(models.Model):
    billno = models.CharField(max_length=20, default='')
    total = models.BigIntegerField()
    address = models.CharField(max_length=200, default='')
    phone=models.BigIntegerField()
    user_id=models.BigIntegerField()



    def __str__(self):
        return self.username
