from django.conf.urls import url
from .views import pay

app_name = 'pay'

urlpatterns = [
    url(r'^$', pay, name='pay'),
    #url(r'^$', card, name='card'),

    ]