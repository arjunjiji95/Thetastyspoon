from django.conf.urls import url
from .views import nonveg

app_name = 'nonveg'

urlpatterns = [
    url(r'^$', nonveg, name='nonveg_forms'),
    # url(r'^(?P<pk>\d+)$', purchasedetails, name='purchasedetails_forms'),
]
