from django.conf.urls import url
from .views import compp

app_name = 'viewcomplaint'

urlpatterns = [
    url(r'^$', compp, name='viewcomplaint_forms'),
    # url(r'^(?P<pk>\d+)$', purchasedetails, name='purchasedetails_forms'),
]
