from django.conf.urls import url
from . import views

app_name = 'stock'

urlpatterns = [
    url(r'^goods_models/$', views.goods_models, name='goods_models'),
    url(r'^goods_models/save_group/$', views.save_group, name='save_group$'),
    url(r'^goods_models/del_group/$', views.del_group, name='del_group'),
    url(r'^goods_models/save_model/$', views.save_model, name='save_model'),
    url(r'^goods_models/del_model/$', views.del_model, name='del_model'),
    url(r'^goods_models/get_model_inf/$', views.get_model_inf, name='get_model_inf'),
    url(r'^props/$', views.props, name='props'),
    url(r'^props/send_prop/$', views.send_prop, name='send_prop'),
    url(r'^props/edit_prop/$', views.edit_prop, name='edit_prop'),
]
