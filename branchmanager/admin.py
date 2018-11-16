from django.contrib import admin
from .models import Branchmanager


class Branchmanageradmin(admin.ModelAdmin):
    list_display = ["branchmanagername", "branchmanagerhouse", "branchmanagerplace", "branchmanagercity", "branchmanagerdistrict", "branchmanagerstate", "branchmanagerpin", "branchmanagerdob", "branchmanagerage", "branchmanagerdoj", "branchmanagercontact", "branchmanageremail", "branchmanagerusername", "branchmanagerpassword", "branchmanagerstatus", "branch_id"]


admin.site.register(Branchmanager, Branchmanageradmin)

