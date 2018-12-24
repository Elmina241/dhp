from django.conf.urls import url
from . import views

app_name = 'stock'

urlpatterns = [
    url(r'^goods_models/$', views.goods_models, name='goods_models'),
]
