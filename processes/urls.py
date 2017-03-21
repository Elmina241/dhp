from django.conf.urls import url
from . import views

app_name = 'processes'

urlpatterns = [
    url(r'^loading_lists/$', views.loading_lists, name = 'loading_lists'),
    url(r'^planning/$', views.planning, name = 'planning'),
    url(r'^process/$', views.mixing, name = 'mixing'),
    url(r'^process/get_state/$', views.get_state, name = 'get_state'),
    url(r'^process/(?P<kneading_id>[0-9]+)/$', views.kneading_detail, name='kneading_detail'),
    url(r'^process/(?P<kneading_id>[0-9]+)/start_process/$', views.start_kneading, name='start_kneading'),
    url(r'^process/(?P<kneading_id>[0-9]+)/mixing/$', views.start_mixing, name='start_mixing'),
    url(r'^process/(?P<kneading_id>[0-9]+)/save_process/$', views.save_list, name='save_list'),
    url(r'^planning/save_process/$', views.save_process, name = 'save_process'),
    url(r'^loading_lists/(?P<list_id>[0-9]+)/$', views.list_detail, name='list_detail'),
    url(r'^loading_lists/(?P<list_id>[0-9]+)/save_list/$', views.save_list, name='save_list'),
]
