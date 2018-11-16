from django.contrib import admin
from .models import User


class Useradmin(admin.ModelAdmin):
    list_display = ["username", "userhouse", "userplace", "usercity", "userdistrict", "userstate", "userpin", "usercontact", "useremail", "userusername", "userpassword"]


admin.site.register(User, Useradmin)
