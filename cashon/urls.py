from django.conf.urls import url
from .views import cashon

app_name = 'cashon'

urlpatterns = [
    url(r'^$', cashon, name='cashon'),
    ]