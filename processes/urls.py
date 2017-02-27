from django.conf.urls import url
from . import views

app_name = 'processes'

urlpatterns = [
    url(r'^loading_lists/$', views.loading_lists, name = 'loading_lists'),
    url(r'^loading_lists/(?P<list_id>[0-9]+)/$', views.list_detail, name='list_detail'),
    url(r'^loading_lists/(?P<list_id>[0-9]+)/save_list/$', views.save_list, name='save_list'),
]
