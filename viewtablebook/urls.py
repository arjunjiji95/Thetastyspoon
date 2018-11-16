from django.conf.urls import url
from .views import tablebook

app_name = 'viewtablebook'

urlpatterns = [
    url(r'^$', tablebook, name='viewtablebook_forms'),
    # url(r'^(?P<pk>\d+)$', purchasedetails, name='purchasedetails_forms'),
]
