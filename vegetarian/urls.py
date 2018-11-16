from django.conf.urls import url
from .views import vegetarian

app_name = 'vegetarian'

urlpatterns = [
    url(r'^$', vegetarian, name='vegetarian_forms'),
    # url(r'^(?P<pk>\d+)$', purchasedetails, name='purchasedetails_forms'),
]
