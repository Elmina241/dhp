from django.conf.urls import url
from . import views

app_name = 'stock'

urlpatterns = [
    url(r'^goods_models/$', views.goods_models, name='goods_models'),
    url(r'^goods/$', views.goods, name='goods'),
    url(r'^goods/save_good/$', views.save_good, name='save_good'),
    url(r'^goods/edit_good/$', views.edit_good, name='edit_good'),
    url(r'^goods_models/save_group/$', views.save_group, name='save_group$'),
    url(r'^goods_models/del_group/$', views.del_group, name='del_group'),
    url(r'^goods_models/save_model/$', views.save_model, name='save_model'),
    url(r'^goods_models/edit_model/$', views.edit_model, name='edit_model'),
    url(r'^goods_models/del_model/$', views.del_model, name='del_model'),
    url(r'^goods_models/get_model_inf/$', views.get_model_inf, name='get_model_inf'),
    url(r'^goods/get_good_inf/$', views.get_good_inf, name='get_good_inf'),
    url(r'^props/$', views.props, name='props'),
    url(r'^requirements/$', views.requirements, name='requirements'),
    url(r'^counterparties/$', views.counterparties, name='counterparties'),
    url(r'^counterparties/send_counter/$', views.send_counter, name='send_counter'),
    url(r'^props/send_prop/$', views.send_prop, name='send_prop'),
    url(r'^props/edit_prop/$', views.edit_prop, name='edit_prop'),
]
