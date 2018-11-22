from django.conf.urls import url
from .views import casht

app_name = 'casht'

urlpatterns = [
    url(r'^$', casht, name='casht'),
    ]