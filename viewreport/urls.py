from django.conf.urls import url
from .views import viewreport

app_name = 'viewreport'

urlpatterns = [
    #url(r'^$', viewreport, name='viewreport_forms'),
    url(r'^(?P<pk>\d+)$', viewreport, name='viewreport_forms'),
    #url(r'^viewreport/(?P<pk>\d+)/$', viewreport, name='viewreport_forms'),
     #url(r'^viewreport/(?P<pk>\d+)/$', viewreport, name='viewreport'),
]
