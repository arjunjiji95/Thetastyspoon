from django.conf.urls import url
from .views import creditt

app_name = 'creditt'

urlpatterns = [
    url(r'^$', creditt, name='creditt'),
    ]