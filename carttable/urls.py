from django.conf.urls import url
from .views import carttable,delete_tab

app_name = 'carttable'

urlpatterns = [
    url(r'^$', carttable, name='carttable_forms'),
    url(r'^delete_tab/(?P<pk>\d+)/$', delete_tab, name='delete_tab'),
    ]