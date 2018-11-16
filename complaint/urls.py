from django.conf.urls import url
from .views import comp, edit_complaint, delete_complaint

app_name = 'complaint'

urlpatterns = [
    url(r'^$', comp, name='complaint_forms'),
    url(r'^edit_complaint/(?P<pk>\d+)/$', edit_complaint, name='edit_complaint'),
    url(r'^delete_complaint/(?P<pk>\d+)/$', delete_complaint, name='delete_complaint'),
]
