from django.conf.urls import url
from . import views

app_name = 'log'

urlpatterns = [
    url(r'^materials/$', views.materials, name = 'materials'),
    url(r'^movement/$', views.movement, name = 'movement'),
    url(r'^accepting/$', views.accepting, name = 'accepting'),
    url(r'^accepting/get_act/$', views.get_act, name = 'get_act'),
    url(r'^movement/get_act_by_prod/$', views.get_act_by_prod, name = 'get_act_by_prod'),
    url(r'^movement/get_pass/$', views.get_pass, name = 'get_pass'),
    url(r'^movement/print_pass/$', views.print_pass, name = 'print_pass'),
    url(r'^movement/release/$', views.release, name = 'release'),
    url(r'^movement/add_rows/$', views.add_rows, name = 'add_rows'),
    url(r'^movement/edit_pack/$', views.edit_pack, name = 'edit_pack'),
]
