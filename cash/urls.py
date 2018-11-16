from django.conf.urls import url
from .views import cash

app_name = 'cash'

urlpatterns = [
    url(r'^$', cash, name='cash'),
    ]