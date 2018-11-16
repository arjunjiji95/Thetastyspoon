from django.conf.urls import url
from .views import tablebook

app_name = 'tablebook'

urlpatterns = [
    url(r'^$', tablebook, name='tablebook_forms1'),
    url(r'^tablebook/(?P<pk>\d+)/$', tablebook, name='tablebook_forms'),
]
