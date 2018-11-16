from django.db import models


class User(models.Model):
    username = models.CharField(max_length=20, default='')
    userhouse = models.CharField(max_length=20, default='')
    userplace = models.CharField(max_length=20, default='')
    usercity = models.CharField(max_length=20, default='')
    userdistrict = models.CharField(max_length=20, default='')
    userstate = models.CharField(max_length=20, default='')
    userpin = models.BigIntegerField(default='')
    usercontact = models.BigIntegerField(default='')
    useremail = models.CharField(max_length=20, default='')
    userusername = models.CharField(max_length=20, default='')
    userpassword = models.CharField(max_length=20, default='')

    def __str__(self):
        return self.username