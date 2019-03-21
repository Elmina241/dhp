from django.conf.urls import url
from . import views

app_name = 'stock'

urlpatterns = [
    url(r'^goods_models/$', views.goods_models, name='goods_models'),
    url(r'^goods/$', views.goods, name='goods'),
    url(r'^stocks/$', views.stocks, name='stocks'),
    url(r'^stock_operations/$', views.stock_operations, name='stock_operations'),
    url(r'^stock_operations/save_supply/$', views.save_supply, name='save_supply'),
    url(r'^goods/save_good/$', views.save_good, name='save_good'),
    url(r'^goods/edit_good/$', views.edit_good, name='edit_good'),
    url(r'^goods_models/save_group/$', views.save_group, name='save_group$'),
    url(r'^goods_models/del_group/$', views.del_group, name='del_group'),
    url(r'^goods_models/save_model/$', views.save_model, name='save_model'),
    url(r'^goods_models/edit_model/$', views.edit_model, name='edit_model'),
    url(r'^goods_models/del_model/$', views.del_model, name='del_model'),
    url(r'^goods/del_good/$', views.del_good, name='del_good'),
    url(r'^goods_models/get_model_inf/$', views.get_model_inf, name='get_model_inf'),
    url(r'^goods/get_good_inf/$', views.get_good_inf, name='get_good_inf'),
    url(r'^stocks/get_prod_info/$', views.get_prod_info, name='get_prod_info'),
    url(r'^props/$', views.props, name='props'),
    url(r'^requirements/$', views.requirements, name='requirements'),
    url(r'^requirements/save_demand/$', views.save_demand, name='save_demand'),
    url(r'^requirements/save_stock_operation/$', views.save_stock_operation, name='save_stock_operation'),
    url(r'^requirements/get_demand_goods/$', views.get_demand_goods, name='get_demand_goods'),
    url(r'^counterparties/$', views.counterparties, name='counterparties'),
    url(r'^counterparties/send_counter/$', views.send_counter, name='send_counter'),
    url(r'^counterparties/del_counter/$', views.del_counter, name='del_counter'),
    url(r'^props/send_prop/$', views.send_prop, name='send_prop'),
    url(r'^props/edit_prop/$', views.edit_prop, name='edit_prop'),
    url(r'^props/del_prop/$', views.del_prop, name='del_prop'),
    url(r'^requirements/save_status/$', views.save_status, name='save_status'),
]
