from django.http.response import HttpResponse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
import json
from django.core import serializers
from django.utils import timezone
import datetime
from .models import  Movement_rec, Operation

from tables.models import Composition, Compl_comp, Compl_comp_comp, Characteristic_set_var, Comp_char_var, Comp_char_range, Comp_char_number, Set_var, Composition_char, Material, Components, Formula, Formula_component, Reactor

def materials(request):
    return render(request, "materials.html", {"header": "Контроль входного сырья", "location": "/log/materials/", "lists": Model_list.objects.all})

def movement(request):
    return render(request, "movement.html", {"header": "Журнал прихода и расхода", "location": "/log/movement/", "movements": Movement_rec.objects.all})
