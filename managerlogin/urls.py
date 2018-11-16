from django.conf.urls import url
from .views import login, managerhome

app_name = 'managerlogin'

urlpatterns = [
    url(r'^$', login, name='manager_forms'),
    url(r'^managerhome', managerhome, name='managerhome'),
]