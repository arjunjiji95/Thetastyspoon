from django.conf.urls import url
from .views import fedd

app_name = 'viewfeedback'

urlpatterns = [
    url(r'^$', fedd, name='viewfeedback_forms'),
    # url(r'^(?P<pk>\d+)$', purchasedetails, name='purchasedetails_forms'),
]
