from django.conf.urls import url
from .views import snacks

app_name = 'snacks'

urlpatterns = [
    url(r'^$', snacks, name='snacks_forms'),
    # url(r'^(?P<pk>\d+)$', purchasedetails, name='purchasedetails_forms'),
]
