from django.conf.urls import url
from . import views
import tables

app_name = 'log'

urlpatterns = [
    url(r'^materials/$', views.materials, name = 'materials'),
]
