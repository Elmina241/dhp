from django.contrib import admin
from .models import Currency, Stock, User_group

# Register your models here.

admin.site.register(Currency)
admin.site.register(Stock)
admin.site.register(User_group)
