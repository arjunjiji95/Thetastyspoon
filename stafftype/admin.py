from django.contrib import admin
from .models import Stafftype


class Stafftypeadmin(admin.ModelAdmin):
    list_display = ["staffname"]


admin.site.register(Stafftype, Stafftypeadmin)
