from django.conf.urls import url
from . import views
import tables

app_name = 'log'

urlpatterns = [
    url(r'^materials/$', views.materials, name = 'materials'),
    url(r'^movement/$', views.movement, name = 'movement'),
    url(r'^accepting/$', views.accepting, name = 'accepting'),
    url(r'^accepting/get_act/$', views.get_act, name = 'get_act'),
    url(r'^movement/get_act_by_prod/$', views.get_act_by_prod, name = 'get_act_by_prod'),
    url(r'^movement/release/$', views.release, name = 'release'),
]
