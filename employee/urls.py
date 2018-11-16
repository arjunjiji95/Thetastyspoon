from django.conf.urls import url
from .views import emp, edit_emp, delete_emp

app_name = 'employee'

urlpatterns = [
    url(r'^$', emp, name='employee_forms'),
    url(r'^edit_emp/(?P<pk>\d+)/$', edit_emp, name='edit_emp'),
    url(r'^delete_emp/(?P<pk>\d+)/$', delete_emp, name='delete_emp'),
]
