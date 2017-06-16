from django.conf.urls import url
from . import views
import tables

app_name = 'processes'

urlpatterns = [
    url(r'^loading_lists/$', views.loading_lists, name = 'loading_lists'),
    url(r'^planning/$', views.planning, name = 'planning'),
    url(r'^process/$', views.mixing, name = 'mixing'),
    url(r'^process/get_state/$', views.get_state, name = 'get_state'),
    url(r'^get_processes/$', views.get_processes, name = 'get_processes'),
    url(r'^get_lists/$', views.get_lists, name = 'get_lists'),
    url(r'^process/(?P<kneading_id>[0-9]+)/$', views.kneading_detail, name='kneading_detail'),
    url(r'^process/(?P<kneading_id>[0-9]+)/start_process/$', views.start_kneading, name='start_kneading'),
    url(r'^process/(?P<kneading_id>[0-9]+)/finish_testing/$', views.finish_testing, name='finish_testing'),
    url(r'^process/(?P<kneading_id>[0-9]+)/mixing/$', views.start_mixing, name='start_mixing'),
    url(r'^process/(?P<composition_id>[0-9]+)/get_elems/$', tables.views.get_elems, name='get_elems'),
    url(r'^process/(?P<composition_id>[0-9]+)/get_checked_elems/$', views.get_checked_elems, name='get_checked_elems'),
    url(r'^process/(?P<kneading_id>[0-9]+)/testing/$', views.start_testing, name='start_testing'),
    url(r'^process/(?P<kneading_id>[0-9]+)/add_comp/$', views.add_comp, name='add_comp'),
    url(r'^loading_lists/(?P<list_id>[0-9]+)/save_list/$', views.save_list, name='save_list'),
    url(r'^planning/save_process/$', views.save_process, name = 'save_process'),
    url(r'^loading_lists/(?P<list_id>[0-9]+)/$', views.list_detail, name='list_detail'),
    url(r'^process/(?P<kneading_id>[0-9]+)/save_load_list/$', views.save_load_list, name='save_load_list'),
    url(r'^process/(?P<kneading_id>[0-9]+)/save_kneading_char/$', views.save_kneading_char, name='save_kneading_char'),
]
