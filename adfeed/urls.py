from django.conf.urls import url
from .views import adfeed

app_name = 'adfeed'

urlpatterns = [
    #url(r'^$', branchview, name='viewbranch_forms'),
    url(r'^(?P<pk>\d+)$', adfeed, name='adfeed_forms'),
    #url(r'^branchview/(?P<pk>\d+)/$', branchview, name='branchview'),
]
