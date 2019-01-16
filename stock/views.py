from django.http.response import HttpResponse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
import json
from tables.models import Unit
from .models import Property, Property_range, Property_var
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
    return render(request, "goods_models.html", {"header": "Макеты материальных ценностей", "tree": json.dumps(tree), "props": json.dumps(serializers.serialize("json", Property.objects.all())), "units": json.dumps(serializers.serialize("json", Unit.objects.all()))})

def props(request):
    prop_data = {}
    for p in Property.objects.all():
        if p.prop_type == 0:
            prop_data[str(p.id)] = {'name': p.name, 'type': 0, 'from': p.property_range.inf, 'to': p.property_range.sup}
        else:
            if p.prop_type == 1:
                prop_data[str(p.id)] = {'name': p.name, 'type': 1}
            else:
                vals = []
                for v in Property_var.objects.filter(prop = p):
                    vals.append(v.name)
                prop_data[str(p.id)] = {'name': p.name, 'type': 2, 'vals': vals}
    return render(request, "props.html", {"header": "Свойства материальных ценностей", "props": Property.objects.all(), "prop_data": json.dumps(prop_data)})

def send_prop(request):
    if request.method == 'POST':
        if 'name' in request.POST:
            t = request.POST['type']
            name = request.POST['name']
            data = json.loads(request.POST['data'])
            if t == '0':
                prop = Property_range(name = name, prop_type = t, inf = data['from'], sup = data['to'])
                print(data['from'])
                prop.save()
            else:
                prop = Property(name=name, prop_type=t)
                prop.save()
                if t == '2':
                    for d in data:
                        print(data)
                        p = Property_var(prop = prop, name = d)
                        p.save()
            return HttpResponse('ok')