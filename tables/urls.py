from django.conf.urls import url
from . import views

app_name = 'tables'

urlpatterns = [
    url(r'^materials/$', views.index, name = 'index'),
    url(r'^products/$', views.products, name = 'products'),
    url(r'^compositions/$', views.compositions, name = 'compositions'),
    url(r'^packing/$', views.packing, name = 'packing'),
    url(r'^production/$', views.production, name = 'production'),
    url(r'^storage/$', views.storage, name = 'storage'),
    url(r'^caps/$', views.caps, name = 'caps'),
    url(r'^boxing/$', views.boxing, name = 'boxing'),
    url(r'^stickers/$', views.stickers, name = 'stickers'),
    url(r'^products/new_product/$', views.new_product, name = 'new_product'),
    url(r'^compositions/new_composition/$', views.new_composition, name = 'new_composition'),
    url(r'^products/new_product/add_product/$', views.add_product, name = 'add_product'),
    url(r'^compositions/new_composition/add_composition/$', views.add_composition, name = 'add_composition'),
    url(r'^materials/new_material/$', views.new_material, name = 'new_material'),
    url(r'^materials/new_material/add_material/$', views.add_material, name = 'add_material'),
    url(r'^products/del_product/$', views.del_product, name = 'del_product'),
    url(r'^materials/del_material/$', views.del_material, name = 'del_material'),
    url(r'^packing/(?P<container_id>[0-9]+)/$', views.container_detail, name='container_detail'),
    url(r'^caps/(?P<cap_id>[0-9]+)/$', views.cap_detail, name='cap_detail'),
    url(r'^boxing/(?P<box_id>[0-9]+)/$', views.box_detail, name='box_detail'),
    url(r'^stickers/(?P<sticker_id>[0-9]+)/$', views.sticker_detail, name='sticker_detail'),
    url(r'^products/(?P<product_id>[0-9]+)/$', views.pr_detail, name='pr_detail'),
    url(r'^products/get_group/$', views.pr_group, name='pr_group'),
    url(r'^compositions/get_group_comp/$', views.comp_group, name='comp_group'),
    url(r'^materials/(?P<material_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^compositions/(?P<composition_id>[0-9]+)/$', views.comp_detail, name='comp_detail'),
    url(r'^materials/(?P<material_id>[0-9]+)/save_material/$', views.save_material, name='save_material'),
    url(r'^products/(?P<product_id>[0-9]+)/save_product/$', views.save_product, name='save_product'),
    url(r'^caps/(?P<cap_id>[0-9]+)/save_cap/$', views.save_cap, name='save_cap'),
    url(r'^boxing/(?P<box_id>[0-9]+)/save_box/$', views.save_box, name='save_box'),
    url(r'^stickers/(?P<sticker_id>[0-9]+)/save_sticker/$', views.save_sticker, name='save_sticker'),
    url(r'^packing/(?P<container_id>[0-9]+)/save_container/$', views.save_container, name='save_container'),
    url(r'^compositions/(?P<composition_id>[0-9]+)/save_composition/$', views.save_composition, name='save_composition')
]
