from django.conf.urls import url
from .views import payment, card

app_name = 'payment'

urlpatterns = [
    url(r'^$', payment, name='payment'),
    url(r'^$', card, name='card'),

    ]