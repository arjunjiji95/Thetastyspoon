from django.conf.urls import url
from .views import foodtype,edit_foodtype,delete_foodtype

app_name = 'foodtype'

urlpatterns = [
    url(r'^$', foodtype, name='foodtype_forms'),
    url(r'^edit_foodtype/(?P<pk>\d+)/$', edit_foodtype, name='edit_foodtype'),
    url(r'^delete_foodtype/(?P<pk>\d+)/$', delete_foodtype, name='delete_foodtype'),
]
