from django.contrib import admin
from .models import Currency, Stock, User_group, Section, User_permission, Stock_operation

# Register your models here.

admin.site.register(Currency)
admin.site.register(Stock)
admin.site.register(User_group)
admin.site.register(Section)
admin.site.register(User_permission)
admin.site.register(Stock_operation)
