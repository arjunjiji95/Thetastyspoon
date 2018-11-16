from django.conf.urls import url
from .views import dailyreport

app_name = 'dailyreport'

urlpatterns = [
    url(r'^$', dailyreport, name='dailyreport_forms'),

    #url(r'^(?P<pk>\d+)$', booknow, name='booknow_forms'),
]
