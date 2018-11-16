from django.contrib import admin
from .models import Menu


class Menuadmin(admin.ModelAdmin):
    list_display = ["menuname", "menuprice", "menudescription", "menupic", "foodtype_id"]


admin.site.register(Menu, Menuadmin)

