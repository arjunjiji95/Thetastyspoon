from django.conf.urls import url
from .views import tabledetails, edit_tabledetails, delete_tabledetails

app_name = 'tabledetails'

urlpatterns = [
    url(r'^$', tabledetails, name='table_forms'),
    url(r'^edit_tabledetails/(?P<pk>\d+)/$', edit_tabledetails, name='edit_tabledetails'),
    url(r'^delete_tabledetails/(?P<pk>\d+)/$', delete_tabledetails, name='delete_tabledetails'),
]
