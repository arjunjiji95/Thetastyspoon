from django.conf.urls import url
from .views import card

app_name = 'card'

urlpatterns = [
    url(r'^$', card, name='card'),
    ]