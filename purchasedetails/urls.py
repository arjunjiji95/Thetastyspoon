from django.conf.urls import url
from .views import purchasedetails

app_name = 'purchasedetails'

urlpatterns = [
    url(r'^$', purchasedetails, name='purchasedetails_forms'),
    # url(r'^(?P<pk>\d+)$', purchasedetails, name='purchasedetails_forms'),
]
