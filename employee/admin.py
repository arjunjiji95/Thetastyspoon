from django.contrib import admin
from .models import Employee


class Employeeadmin(admin.ModelAdmin):
    list_display = ["employeename", "employeehouse", "employeeplace", "employeecity", "employeedistrict",
                    "employeestate", "employeepin", "employeedob", "employeeage", "employeedoj", "employeecontact",
                    "employeeemail", "employeeusername", "employeepassword", "stafftype_id", "branchmanager_id"]


admin.site.register(Employee, Employeeadmin)
