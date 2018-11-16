from django.conf.urls import url
from .views import foodbook

app_name = 'viewfoodbook'

urlpatterns = [
    url(r'^$', foodbook, name='viewfoodbook_forms'),
    # url(r'^(?P<pk>\d+)$', purchasedetails, name='purchasedetails_forms'),
]
