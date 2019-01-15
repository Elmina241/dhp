from django.http.response import HttpResponse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
import json
from tables.models import Material
from .models import Property
from django.core import serializers
from django.utils import timezone
import datetime


def goods_models(request):
    tree = {
        0: {
            'id': 0,
            'name': "null",
            'nodes': {
                1: {
                    'id': 1,
                    'name': "Главный",
                    'nodes': {
                        2: {
                            'id': 2,
                            'name': "Пункт 1"
                        },
                        3: {
                            'id': 3,
                            'name': "Пункт 2"
                        }
                    }
                }
            }
        }
    }
    return render(request, "goods_models.html", {"header": "Макеты материальных ценностей", "tree": json.dumps(tree)})

def props(request):
    return render(request, "props.html", {"header": "Свойства материальных ценностей", "props": Property.objects.all()})

def send_prop(request):
    if request.method == 'POST':
        if 'name' in request.POST:
            t = request.POST['type']
            name = request.POST['name']
            data = json.loads(request.POST['data'])
            if t == 0:
                prop = Property_range(name = name, prop_type = t, inf = data['from'], sup = data['to'])
                prop.save()
            else:
                prop = Property(name=name, prop_type=t)
                prop.save()
                if t == 2:
                    for d in data:
                        p = Property_var(prop = prop, name = d)
                        p.save()
            return HttpResponse('ok')