from django.contrib import admin
from .models import Material_group, Prefix, Unit, Material, Product_group, Product_form, Product_use, Product_mark, Product_option, Product_detail, Product

admin.site.register(Material_group)
admin.site.register(Prefix)
admin.site.register(Unit)
admin.site.register(Material)
admin.site.register(Product_group)
admin.site.register(Product_use)
admin.site.register(Product_form)
admin.site.register(Product_option)
admin.site.register(Product_detail)
admin.site.register(Product_mark)
admin.site.register(Product)

# Register your models here.
