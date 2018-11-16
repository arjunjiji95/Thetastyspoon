from django.contrib import admin
from .models import Feedback


class Feedbackadmin(admin.ModelAdmin):
    list_display = ["feedbackcontent", "feedbackdate", "user_id", "branch_id"]


admin.site.register(Feedback, Feedbackadmin)
