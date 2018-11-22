from django.conf.urls import url
from .views import branchview

app_name = 'viewbranch'

urlpatterns = [
    #url(r'^$', branchview, name='viewbranch_forms'),
    url(r'^(?P<pk>\d+)$', branchview, name='viewbranch_forms'),
    #url(r'^verify_details/(?P<pk>\d+)/$', verify_details, name='verify_details'),
]
