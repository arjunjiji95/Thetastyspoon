from django.contrib import admin
from .models import Branch


class Branchadmin(admin.ModelAdmin):
    list_display = ["branchname", "branchplace", "branchcity", "branchdistrict", "branchpin", "branchcontact", "branchemail"]


admin.site.register(Branch, Branchadmin)

