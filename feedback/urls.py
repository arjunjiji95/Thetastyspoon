from django.conf.urls import url
from .views import fed, edit_feedback, delete_feedback

app_name = 'feedback'

urlpatterns = [
    url(r'^$', fed, name='feedback_forms'),
    url(r'^edit_feedback/(?P<pk>\d+)/$', edit_feedback, name='edit_feedback'),
    url(r'^delete_feedback/(?P<pk>\d+)/$', delete_feedback, name='delete_feedback'),
]
