from django.contrib import admin
from .models import Kneading, State, State_log, Loading_list, List_component, Kneading_char , Reactor_content, Tank_content

admin.site.register(State)
admin.site.register(State_log)
admin.site.register(Loading_list)
admin.site.register(List_component)
admin.site.register(Kneading_char)
admin.site.register(Reactor_content)
admin.site.register(Tank_content)
admin.site.register(Kneading)
