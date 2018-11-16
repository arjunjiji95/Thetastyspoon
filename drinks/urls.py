from django.conf.urls import url
from .views import drinks

app_name = 'drinks'

urlpatterns = [
    url(r'^$', drinks, name='drinks_forms'),
    # url(r'^(?P<pk>\d+)$', purchasedetails, name='purchasedetails_forms'),
]
