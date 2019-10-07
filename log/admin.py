from django.contrib import admin

from .models import Operation, Movement_rec, Packing_char

admin.site.register(Operation)
admin.site.register(Movement_rec)
admin.site.register(Packing_char)

# Register your models here.
