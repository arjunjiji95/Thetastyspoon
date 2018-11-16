from django.conf.urls import url
from .views import branch,edit_branch,delete_branch

app_name = 'branch'

urlpatterns = [
    url(r'^$', branch, name='branch_forms'),
    url(r'^edit_branch/(?P<pk>\d+)/$', edit_branch, name='edit_branch'),
    url(r'^delete_branch/(?P<pk>\d+)/$', delete_branch, name='delete_branch'),
]
