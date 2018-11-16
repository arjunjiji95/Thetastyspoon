from django.conf.urls import url
from .views import agency, edit_agency, delete_agency

app_name = 'agency'

urlpatterns = [
    url(r'^$', agency, name='agency_forms'),
    url(r'^edit_agency/(?P<pk>\d+)/$', edit_agency, name='edit_agency'),
    url(r'^delete_agency/(?P<pk>\d+)/$', delete_agency, name='delete_agency'),
]
