from django.conf.urls import url
from .views import purchase

app_name = 'purchasehead'

urlpatterns = [
    url(r'^$', purchase, name='purchasehead_forms'),
]
