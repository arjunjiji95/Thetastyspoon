from django.conf.urls import url
from .views import front

app_name = 'front'

urlpatterns = [
    url(r'^$', front, name='front_forms'),
    #url(r'^(?P<pk>\d+)$', viewfood, name='food_forms'),

    #url(r'^(?P<pk>\d+)$', booknow, name='booknow_forms'),
]
