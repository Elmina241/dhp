from django.http.response import HttpResponse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
import json
from tables.models import Unit
from .models import Default_number, Counterparty, Default_text, Default_var, Property, Property_range, Model_property, Model_unit, Property_var, Model_group, Product_model
from django.core import serializers
from django.utils import timezone
import datetime


def goods_models(request):
    tree = {}
    tree[0] = {"name": "root", "nodes": {}}
    g = Model_group.objects.all().first()
    add_children(g, tree[0])
    model_json = {}
    for m in Product_model.objects.all():
        model_json[str(m.pk)] = {"id": m.pk, "name": m.name, "group": m.group.pk}
    return render(request, "goods_models.html", {"header": "Макеты материальных ценностей", "models": Product_model.objects.all(), "prop_vars": json.dumps(serializers.serialize("json", Property_var.objects.all())), "tree": json.dumps(tree), "model_json": json.dumps(model_json), "props": json.dumps(serializers.serialize("json", Property.objects.all())), "groups": Model_group.objects.exclude(pk = 0), "units": json.dumps(serializers.serialize("json", Unit.objects.all()))})

def goods(request):
    tree = {}
    tree[0] = {"name": "root", "nodes": {}}
    g = Model_group.objects.all().first()
    add_children(g, tree[0])
    models = {}
    for m in Product_model.objects.all():
        models[str(m.pk)] = {"units": {}, "props": {}}
        for u in Model_unit.objects.filter(model = m):
            models[str(m.pk)]["units"][str(u.pk)] = {"name": u.unit.name}
        for p in Model_property.objects.filter(model = m):
            models[str(m.pk)]["props"][str(p.pk)] = {"name": p.prop.name, "type": p.prop.prop_type, "visible": p.visible, "editable": p.editable, "default": "", "choises": None}
            if p.isDefault:
                if p.prop.prop_type == 0:
                    try:
                        models[str(m.pk)]["props"][str(p.pk)]["default"] = p.default_number.number
                    except AttributeError as error:
                        print(error)
                else:
                    if p.prop.prop_type == 1:
                        try:
                            models[str(m.pk)]["props"][str(p.pk)]["default"] = p.default_text.text
                        except AttributeError as error:
                            print(error)
                    else:
                        models[str(m.pk)]["props"][str(p.pk)]["default"] = p.default_var.var.id
                        models[str(m.pk)]["props"][str(p.pk)]["choises"] = {}
                        for v in Property_var.objects.filter(prop = p.prop):
                            models[str(m.pk)]["props"][str(p.pk)]["choises"][str(v.pk)] = v.name
    return render(request, "goods.html", {"header": "Материальные ценности",  "tree": json.dumps(tree), "counters": Counterparty.objects.all(), "models": Product_model.objects.all(), "model_json": json.dumps(models)})


def add_children(obj, node):
    for o in Model_group.objects.filter(parent = obj.id):
        if 'nodes' not in node:
            node['nodes'] = {}
        node['nodes'][o.id] = {"name": o.name, "id": o.id}
        add_children(o, node['nodes'][o.id])

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

def counterparties(request):
    return render(request, "counterparties.html", {"header": "Контрагенты", "counters": Counterparty.objects.all()})

def send_prop(request):
    if request.method == 'POST':
        if 'name' in request.POST:
            t = request.POST['type']
            name = request.POST['name']
            data = json.loads(request.POST['data'])
            if t == '0':
                prop = Property_range(name = name, prop_type = t, inf = data['from'], sup = data['to'])
                prop.save()
            else:
                prop = Property(name=name, prop_type=t)
                prop.save()
                if t == '2':
                    for d in data:
                        p = Property_var(prop = prop, name = d)
                        p.save()
            return HttpResponse('ok')

def send_counter(request):
    if request.method == 'POST':
        if 'name' in request.POST:
            kind = request.POST['kind']
            name = request.POST['name']
            category = request.POST['category']
            c = Counterparty(name = name, kind = kind, category = category)
            c.save()
            return HttpResponse('ok')

def get_model_inf(request):
    if request.method == 'POST':
        if 'id' in request.POST:
            model = Product_model.objects.get(pk = request.POST['id'])
            data = {}
            data['name'] = model.name
            data['group'] = model.group.pk
            units = []
            for u in Model_unit.objects.filter(model = model):
                units.append(u.unit.pk)
            data["units"] = units
            props = {}
            for p in Model_property.objects.filter(model=model):
                props[str(p.pk)] = {"id": p.prop.pk, "visible": p.visible, "editable": p.editable, "isDefault": p.isDefault}
                if p.isDefault:
                    props[str(p.pk)]["default_type"] = p.prop.prop_type
                    if p.prop.prop_type == 0:
                        props[str(p.pk)]["default"] = p.default_number.number
                    else:
                        if p.prop.prop_type == 1:
                            props[str(p.pk)]["default"] = p.default_text.text
                        else:
                            props[str(p.pk)]["default"] = p.default_var.var.id
            data["props"] = props
            return HttpResponse(json.dumps(data))

def save_model(request):
    if request.method == 'POST':
        if 'name' in request.POST:
            group = Model_group.objects.get(pk = request.POST['group'])
            name = request.POST['name']
            units = json.loads(request.POST['units'])
            props = json.loads(request.POST['props'])
            model = Product_model(name = name, group = group)
            model.save()
            for u in units:
                unit = Unit.objects.get(pk = u)
                m = Model_unit(model = model, unit = unit)
                m.save()
            for p in props:
                prop = Property.objects.get(pk = int(props[p]["prop"]))
                if props[p]['isDefault']:
                    if prop.prop_type == 0:
                        d = Default_number(model = model, prop = prop, visible = not props[p]['hidden'], editable = not props[p]['uneditable'], isDefault = props[p]['isDefault'], number = props[p]['default'])
                        d.save()
                    else:
                        if prop.prop_type == 1:
                            d = Default_text(model = model, prop = prop, visible = not props[p]['hidden'], editable = not props[p]['uneditable'], isDefault = props[p]['isDefault'], text=props[p]['default'])
                            d.save()
                        else:
                            d = Default_var(model = model, prop = prop, visible = not props[p]['hidden'], editable = not props[p]['uneditable'], isDefault = props[p]['isDefault'], var=Property_var.objects.get(pk = props[p]['default']))
                            d.save()
                else:
                    m = Model_property(model = model, prop = prop, visible = not props[p]['hidden'], editable = not props[p]['uneditable'], isDefault = props[p]['isDefault'])
                    m.save()
            return HttpResponse('ok')

def edit_model(request):
    if request.method == 'POST':
        if 'name' in request.POST:
            group = Model_group.objects.get(pk = request.POST['group'])
            name = request.POST['name']
            units = json.loads(request.POST['units'])
            props = json.loads(request.POST['props'])
            model = Product_model.objects.get(pk = request.POST['id'])
            model.name = name
            model.group = group
            model.save()
            Model_unit.objects.filter(model=model).delete()
            for u in units:
                unit = Unit.objects.get(pk = u)
                m = Model_unit(model=model, unit=unit)
                m.save()
            Model_property.objects.filter(model = model).delete()
            for p in props:
                prop = Property.objects.get(pk = int(props[p]["prop"]))
                if props[p]['isDefault']:
                    if prop.prop_type == 0:
                        d = Default_number(model = model, prop = prop, visible = not props[p]['hidden'], editable = not props[p]['uneditable'], isDefault = props[p]['isDefault'], number = props[p]['default'])
                        d.save()
                    else:
                        if prop.prop_type == 1:
                            d = Default_text(model = model, prop = prop, visible = not props[p]['hidden'], editable = not props[p]['uneditable'], isDefault = props[p]['isDefault'], text=props[p]['default'])
                            d.save()
                        else:
                            d = Default_var(model = model, prop = prop, visible = not props[p]['hidden'], editable = not props[p]['uneditable'], isDefault = props[p]['isDefault'], var=Property_var.objects.get(pk = props[p]['default']))
                            d.save()
                else:
                    m = Model_property(model = model, prop = prop, visible = not props[p]['hidden'], editable = not props[p]['uneditable'], isDefault = props[p]['isDefault'])
                    m.save()
            return HttpResponse('ok')

def save_group(request):
    if request.method == 'POST':
        if 'name' in request.POST:
            if request.POST['id'] != '':
                group = Model_group.objects.get(pk = request.POST['id'])
                group.name = request.POST['name']
            else:
                group = Model_group(name = request.POST['name'], parent = request.POST['parent'])
            group.save()
            return HttpResponse(group.pk)

def del_group(request):
    if request.method == 'POST':
        Model_group.objects.get(pk = request.POST['id']).delete()
        return HttpResponse("ok")

def del_model(request):
    if request.method == 'POST':
        Product_model.objects.get(pk = request.POST['id']).delete()
        return HttpResponse("ok")

def edit_prop(request):
    if request.method == 'POST':
        if 'id' in request.POST:
            prop = Property.objects.get(pk=request.POST['id'])
            name = request.POST['name']
            data = json.loads(request.POST['data'])
            if prop.prop_type == 0:
                prop.name = name
                prop.property_range.inf = data['from']
                prop.property_range.sup = data['to']
                prop.property_range.save()
                prop.save()
            else:
                prop.name = name
                prop.save()
                if prop.prop_type == 2:
                    Property_var.objects.filter(prop = prop).delete()
                    for d in data:
                        p = Property_var(prop = prop, name = d)
                        p.save()
            return HttpResponse('ok')