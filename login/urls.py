from django.conf.urls import url
from .views import login, userhome

app_name = 'login'

urlpatterns = [
    url(r'^$', login, name='login_forms'),
    url(r'^userhome$', userhome, name='userhome'),
]