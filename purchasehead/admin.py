from django.contrib import admin
from .models import Purchasehead


class Purchaseheadadmin(admin.ModelAdmin):
    list_display = ["purchaseinvoice", "purchasedate", "purchasegrandtotal", "agency_id"]


admin.site.register(Purchasehead, Purchaseheadadmin)



