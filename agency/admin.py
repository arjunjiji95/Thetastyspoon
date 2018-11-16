from django.contrib import admin
from .models import Agency


class Agencyadmin(admin.ModelAdmin):
    list_display = ["agencyname", "agencyplace", "agencycity", "agencydistrict", "agencypin", "agencycontact", "agencyemail", "branchmanager_id"]


admin.site.register(Agency, Agencyadmin)
