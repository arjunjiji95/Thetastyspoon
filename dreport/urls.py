from django.conf.urls import url
from .views import dreport

app_name = 'dreport'

urlpatterns = [
    url(r'^$', dreport, name='dreport_forms'),
    ]
