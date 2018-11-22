from django.conf.urls import url
from .views import repbranch

app_name = 'repbranch'

urlpatterns = [
    url(r'^$', repbranch, name='repbranch_forms'),

    #url(r'^(?P<pk>\d+)$', booknow, name='booknow_forms'),
]
