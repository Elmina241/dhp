from django.conf.urls import url
from . import views

app_name = 'tables'

urlpatterns = [
    url(r'^materials/$', views.index, name = 'index'),
    url(r'^products/$', views.products, name = 'products'),
    url(r'^products/new_product/$', views.new_product, name = 'new_product'),
    url(r'^products/new_product/add_product/$', views.add_product, name = 'add_product'),
    url(r'^materials/new_material/$', views.new_material, name = 'new_material'),
    url(r'^materials/new_material/add_material/$', views.add_material, name = 'add_material'),
    url(r'^products/(?P<product_id>[0-9]+)/$', views.pr_detail, name='pr_detail'),
    url(r'^materials/(?P<material_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^materials/(?P<material_id>[0-9]+)/save_material/$', views.save_material, name='save_material'),
    url(r'^products/(?P<product_id>[0-9]+)/save_product/$', views.save_product, name='save_product')
]
