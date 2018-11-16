from django.conf.urls import url
from .views import net

app_name = 'net'

urlpatterns = [
    url(r'^$', net, name='net'),
    ]