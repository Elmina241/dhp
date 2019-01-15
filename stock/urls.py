from django.conf.urls import url
from . import views

app_name = 'stock'

urlpatterns = [
    url(r'^goods_models/$', views.goods_models, name='goods_models'),
    url(r'^props/$', views.props, name='props'),
    url(r'^props/send_prop/$', views.send_prop, name='send_prop'),
]
