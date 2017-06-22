from django.conf.urls import url
from . import views

app_name = 'tables'

urlpatterns = [
    # таблицы
    url(r'^comp_chars/(?P<composition_id>[0-9]+)/save_comp_char/$', views.save_comp_char, name='save_comp_char'),
    url(r'^materials/$', views.index, name = 'index'),
    url(r'^products/$', views.products, name = 'products'),
    url(r'^compositions/$', views.compositions, name = 'compositions'),
    url(r'^packing/$', views.packing, name = 'packing'),
    url(r'^production/$', views.production, name = 'production'),
    url(r'^storage/$', views.storage, name = 'storage'),
    url(r'^caps/$', views.caps, name = 'caps'),
    url(r'^boxing/$', views.boxing, name = 'boxing'),
    url(r'^stickers/$', views.stickers, name = 'stickers'),
    url(r'^formulas/$', views.formulas, name = 'formulas'),
    url(r'^characteristics/$', views.characteristics, name = 'characteristics'),
    url(r'^comp_chars/$', views.comp_chars, name = 'comp_chars'),
    url(r'^complex_comps/$', views.complex_comps, name = 'complex_comps'),
    # добавление записей
    url(r'^products/new_product/$', views.new_product, name = 'new_product'),
    url(r'^compositions/new_composition/$', views.new_composition, name = 'new_composition'),
    url(r'^products/new_product/add_product/$', views.add_product, name = 'add_product'),
    url(r'^compositions/new_composition/add_composition/$', views.add_composition, name = 'add_composition'),
    url(r'^materials/new_material/$', views.new_material, name = 'new_material'),
    url(r'^materials/new_material/add_material/$', views.add_material, name = 'add_material'),
    url(r'^characteristics/new_characteristic/$', views.new_characteristic, name = 'new_characteristic'),
    url(r'^characteristics/new_characteristic/add_characteristic/$', views.add_characteristic, name = 'add_characteristic'),
    url(r'^storage/0/$', views.storage_detail, name='storage_detail'),
    url(r'^complex_comps/(?P<comp_id>[0-9]+)/$', views.new_comp, name='new_comp'),
    # удаление записей
    url(r'^products/del_product/$', views.del_product, name = 'del_product'),
    url(r'^materials/del_material/$', views.del_material, name = 'del_material'),
    url(r'^boxing/del_box/$', views.del_box, name = 'del_box'),
    url(r'^caps/del_cap/$', views.del_cap, name = 'del_cap'),
    url(r'^characteristics/del_characteristic/$', views.del_characteristic, name = 'del_characteristic'),
    url(r'^complex_comps/del_comp/$', views.del_comp, name = 'del_comp'),
    url(r'^compositions/del_composition/$', views.del_composition, name = 'del_composition'),
    url(r'^packing/del_packing/$', views.del_packing, name = 'del_packing'),
    url(r'^production/del_commodity/$', views.del_commodity, name = 'del_commodity'),
    url(r'^stickers/del_sticker/$', views.del_sticker, name = 'del_sticker'),
    url(r'^storage/del_storage/$', views.del_storage, name = 'del_storage'),
    url(r'^formulas/del_formula/$', views.del_formula, name = 'del_formula'),
    # редактирование записей
    url(r'^packing/(?P<container_id>[0-9]+)/$', views.container_detail, name='container_detail'),
    url(r'^caps/(?P<cap_id>[0-9]+)/$', views.cap_detail, name='cap_detail'),
    url(r'^storage/reactor/(?P<storage_id>[0-9]+)/$', views.reactor_detail, name='reactor_detail'),
    url(r'^storage/tank/(?P<storage_id>[0-9]+)/$', views.tank_detail, name='tank_detail'),
    url(r'^boxing/(?P<box_id>[0-9]+)/$', views.box_detail, name='box_detail'),
    url(r'^stickers/(?P<sticker_id>[0-9]+)/$', views.sticker_detail, name='sticker_detail'),
    url(r'^products/(?P<product_id>[0-9]+)/$', views.pr_detail, name='pr_detail'),
    url(r'^production/(?P<commodity_id>[0-9]+)/$', views.comm_detail, name='comm_detail'),
    url(r'^materials/(?P<material_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^compositions/(?P<composition_id>[0-9]+)/$', views.comp_detail, name='comp_detail'),
    url(r'^formulas/(?P<formula_id>[0-9]+)/$', views.formula_detail, name='formula_detail'),
    url(r'^characteristics/(?P<characteristic_id>[0-9]+)/$', views.characteristic_detail, name='characteristic_detail'),
    url(r'^comp_chars/(?P<composition_id>[0-9]+)/$', views.comp_char_detail, name='comp_char_detail'),
    # фильтры
    url(r'^products/get_group/$', views.pr_group, name='pr_group'),
    url(r'^materials/get_group/$', views.mat_group, name='mat_group'),
    url(r'^compositions/get_group_comp/$', views.comp_group, name='comp_group'),
    # сохранение изменений

    url(r'^materials/(?P<material_id>[0-9]+)/save_material/$', views.save_material, name='save_material'),
    url(r'^products/(?P<product_id>[0-9]+)/save_product/$', views.save_product, name='save_product'),
    url(r'^caps/(?P<cap_id>[0-9]+)/save_cap/$', views.save_cap, name='save_cap'),
    url(r'^boxing/(?P<box_id>[0-9]+)/save_box/$', views.save_box, name='save_box'),
    url(r'^stickers/(?P<sticker_id>[0-9]+)/save_sticker/$', views.save_sticker, name='save_sticker'),
    url(r'^production/(?P<commodity_id>[0-9]+)/save_commodity/$', views.save_commodity, name='save_commodity'),
    url(r'^packing/(?P<container_id>[0-9]+)/save_container/$', views.save_container, name='save_container'),
    url(r'^storage/(reactor/|tank/|)(?P<storage_id>[0-9]+)/save_storage/$', views.save_storage, name='save_storage'),
    url(r'^compositions/(?P<composition_id>[0-9]+)/save_composition/$', views.save_composition, name='save_composition'),
    url(r'^formulas/(?P<formula_id>[0-9]+)/save_formula/$', views.save_formula, name='save_formula'),
    url(r'^complex_comps/0/save_comp/$', views.save_comp, name='save_comp'),
    # Запросы
    url(r'^complex_comps/get_comps/$', views.get_comps, name='get_comps'),
    url(r'^comp_chars/(?P<composition_id>[0-9]+)/get_char/$', views.get_char, name='get_char'),
    url(r'^comp_chars/(?P<composition_id>[0-9]+)/get_elems/$', views.get_elems, name='get_elems')
]
