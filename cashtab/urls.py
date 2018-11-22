from django.conf.urls import url
from .views import cashtab

app_name = 'cashtab'

urlpatterns = [
    url(r'^$', cashtab, name='cashtab'),
    ]