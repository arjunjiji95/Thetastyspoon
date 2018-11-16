from django.conf.urls import url
from .views import successfull

app_name = 'successfull'

urlpatterns = [
    url(r'^$', successfull, name='successfull_forms'),
    #url(r'^tablebook/(?P<pk>\d+)/$', tablebook, name='tablebook_forms'),
]
