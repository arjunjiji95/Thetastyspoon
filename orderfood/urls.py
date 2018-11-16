from django.conf.urls import url
from .views import order

app_name = 'orderfood'

urlpatterns = [
    url(r'^(?P<pk>\d+)$', order, name='orderfood_forms'),
    #url(r'^$', order, name='orderfood_forms')
]
