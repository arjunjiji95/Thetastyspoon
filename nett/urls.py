from django.conf.urls import url
from .views import nett

app_name = 'nett'

urlpatterns = [
    url(r'^$', nett, name='nett'),
    ]