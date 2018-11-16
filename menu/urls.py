from django.conf.urls import url
from .views import menu,edit_menu,delete_menu

app_name = 'menu'

urlpatterns = [
    url(r'^$', menu, name='menu_forms'),
    url(r'^edit_menu/(?P<pk>\d+)/$', edit_menu, name='edit_menu'),
    url(r'^delete_menu/(?P<pk>\d+)/$', delete_menu, name='delete_menu'),
]
