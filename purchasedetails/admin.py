from django.contrib import admin
from .models import Purchasedetails

class Purchasedetailsadmin(admin.ModelAdmin):
    list_display = ["itemname", "itemquantity", "itembasicrate", "itemunittotal", "purchaseinvoice"]


admin.site.register(Purchasedetails, Purchasedetailsadmin)

