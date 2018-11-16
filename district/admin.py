from django.contrib import admin
from .models import District


class Districtadmin(admin.ModelAdmin):
    list_display = ["name"]


admin.site.register(District, Districtadmin)