from django.conf.urls import url
from .views import adbranch

app_name = 'adbranch'

urlpatterns = [
    url(r'^$', adbranch, name='adbranch_forms'),

    #url(r'^(?P<pk>\d+)$', booknow, name='booknow_forms'),
]
