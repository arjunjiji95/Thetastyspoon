from django.contrib import admin
from .models import Complaint


class Complaintadmin(admin.ModelAdmin):
    list_display = ["complaintcontent", "complaintdate", "user_id", "branch_id"]


admin.site.register(Complaint, Complaintadmin)
