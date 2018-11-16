from django.contrib import admin
from .models import Foodtype


class Foodtypeadmin(admin.ModelAdmin):
    list_display = ["foodname"]


admin.site.register(Foodtype, Foodtypeadmin)