from django.contrib import admin
from .models import Table


class Tableadmin(admin.ModelAdmin):
    list_display = ["tableno", "seatno", "tablerate", "tablestatus", "branchmanager_id"]


admin.site.register(Table, Tableadmin)

