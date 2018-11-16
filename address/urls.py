from django.conf.urls import url
from .views import address,delete_food

app_name = 'address'

urlpatterns = [
    url(r'^$', address, name='address_forms'),
    url(r'^delete_food/(?P<pk>\d+)/$', delete_food, name='delete_food'),
    ]