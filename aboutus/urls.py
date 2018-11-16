from django.conf.urls import url
from .views import aboutus

app_name = 'aboutus'

urlpatterns = [
    url(r'^$', aboutus, name='aboutus'),
    ]