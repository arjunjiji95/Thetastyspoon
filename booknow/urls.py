from django.conf.urls import url
from .views import booknow

app_name = 'booknow'

urlpatterns = [
    url(r'^$', booknow, name='booknow_forms'),

    #url(r'^(?P<pk>\d+)$', booknow, name='booknow_forms'),
]
