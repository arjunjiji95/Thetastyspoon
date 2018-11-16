from django.conf.urls import url
from .views import viewfood

app_name = 'food'

urlpatterns = [
    url(r'^$', viewfood, name='food_forms'),
    #url(r'^(?P<pk>\d+)$', viewfood, name='food_forms'),

    #url(r'^(?P<pk>\d+)$', booknow, name='booknow_forms'),
]
