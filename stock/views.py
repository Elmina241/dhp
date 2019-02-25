from django.http.response import HttpResponse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
import json
from tables.models import Unit
from .models import Default_number, Counter_stock, Goods, Stock, Good_name, Goods_property, Goods_unit, Property_num, Goods_string, Goods_var, \
    Counterparty, Default_text, Default_var, Property, Property_range, Model_property, Model_unit, Property_var, \
    Model_group, Product_model
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
    return render(request, "goods_models.html",
                  {"header": "Макеты материальных ценностей", "models": Product_model.objects.all(),
                   "prop_vars": json.dumps(serializers.serialize("json", Property_var.objects.all())),
                   "tree": json.dumps(tree), "model_json": json.dumps(model_json),
                   "props": json.dumps(serializers.serialize("json", Property.objects.all())),
                   "groups": Model_group.objects.exclude(pk=0),
                   "units": json.dumps(serializers.serialize("json", Unit.objects.all()))})


def goods(request):
    tree = {}
    tree[0] = {"name": "root", "nodes": {}}
    g = Model_group.objects.all().first()
    add_children(g, tree[0])
    goods_json = {}
    for m in Goods.objects.all():
        names = Good_name.objects.filter(product=m)[0]
        goods_json[str(m.pk)] = {"id": m.pk, "name": names.name, "article": names.article, "group": m.model.group.pk}
    models = {}
    for m in Product_model.objects.all():
        models[str(m.pk)] = {"units": {}, "props": {}}
        for u in Model_unit.objects.filter(model=m):
            models[str(m.pk)]["units"][str(u.unit.pk)] = {"name": u.unit.name}
        for p in Model_property.objects.filter(model=m):
            models[str(m.pk)]["props"][str(p.prop.pk)] = {"name": p.prop.name, "type": p.prop.prop_type,
                                                          "visible": p.visible, "editable": p.editable, "default": "",
                                                          "choises": None}
            if p.isDefault:
                if p.prop.prop_type == 0:
                    try:
                        models[str(m.pk)]["props"][str(p.prop.pk)]["default"] = p.default_number.number
                    except AttributeError as error:
                        print(error)
                else:
                    if p.prop.prop_type == 1:
                        try:
                            models[str(m.pk)]["props"][str(p.prop.pk)]["default"] = p.default_text.text
                        except AttributeError as error:
                            print(error)
                    else:
                        models[str(m.pk)]["props"][str(p.prop.pk)]["default"] = p.default_var.var.id
                        models[str(m.pk)]["props"][str(p.prop.pk)]["choises"] = {}
                        for v in Property_var.objects.filter(prop=p.prop):
                            models[str(m.pk)]["props"][str(p.prop.pk)]["choises"][str(v.pk)] = v.name
    return render(request, "goods.html",
                  {"header": "Материальные ценности", "tree": json.dumps(tree), "counters": Counterparty.objects.all(),
                   "models": Product_model.objects.all(), "model_json": json.dumps(models),
                   "goods_json": json.dumps(goods_json), "goods": Goods.objects.all()})


def add_children(obj, node):
    for o in Model_group.objects.filter(parent=obj.id):
        if 'nodes' not in node:
            node['nodes'] = {}
        node['nodes'][o.id] = {"name": o.name, "id": o.id}
        add_children(o, node['nodes'][o.id])

def add_children_g(obj, node):
    for o in Model_group.objects.filter(parent=obj.id):
        if 'nodes' not in node:
            node['nodes'] = {}
        node['nodes'][o.id] = {"name": o.name, "id": o.id}
        node['nodes'][o.id]['nodes'] = {}
        for m in Product_model.objects.filter(group = o):
            node['nodes'][o.id]['nodes']['m_' + str(m.pk)] = {"name": m.name, "id": 'm_' + str(m.id)}
            node['nodes'][o.id]['nodes']['m_' + str(m.pk)]['nodes'] = {}
            for g in Goods.objects.filter(model = m):
                node['nodes'][o.id]['nodes']['m_' + str(m.pk)]['nodes']['g_' + str(g.pk)] = {"name": g.get_name(), "id": 'g_' + str(g.id)}
        add_children_g(o, node['nodes'][o.id])


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
                for v in Property_var.objects.filter(prop=p):
                    vals.append(v.name)
                prop_data[str(p.id)] = {'name': p.name, 'type': 2, 'vals': vals}
    return render(request, "props.html", {"header": "Свойства материальных ценностей", "props": Property.objects.all(),
                                          "prop_data": json.dumps(prop_data)})


def counterparties(request):
    return render(request, "counterparties.html", {"header": "Контрагенты", "counters": Counterparty.objects.all(), "stockData": json.dumps(serializers.serialize("json", Stock.objects.all()))})

def requirements(request):
    tree = {}
    tree[0] = {"name": "root", "nodes": {}}
    g = Model_group.objects.all().first()
    add_children_g(g, tree[0])
    goods = []
    goods_inf = {}
    i = 0
    for g in Good_name.objects.all():
        goods.append(g.article + ' ' + g.name)
        goods_inf[i] = g.product.pk
        i = i + 1
    return render(request, "requirements.html", {"header": "Требования", "tree": json.dumps(tree), "goods": json.dumps(goods), "goods_inf": json.dumps(goods_inf), "counters": Counterparty.objects.all()})


def send_prop(request):
    if request.method == 'POST':
        if 'name' in request.POST:
            t = request.POST['type']
            name = request.POST['name']
            data = json.loads(request.POST['data'])
            if t == '0':
                prop = Property_range(name=name, prop_type=t, inf=data['from'], sup=data['to'])
                prop.save()
            else:
                prop = Property(name=name, prop_type=t)
                prop.save()
                if t == '2':
                    for d in data:
                        p = Property_var(prop=prop, name=d)
                        p.save()
            return HttpResponse('ok')


def send_counter(request):
    if request.method == 'POST':
        if 'name' in request.POST:
            kind = request.POST['kind']
            name = request.POST['name']
            c = Counterparty(name=name, kind=kind, is_provider = json.loads(request.POST['isProv']), is_consumer = json.loads(request.POST['isCons']), is_member = json.loads(request.POST['isMember']))
            c.save()
            data = json.loads(request.POST['stocks'])
            for d in data:
                p = Counter_stock(counter=c, stock=Stock.objects.get(pk = d))
                p.save()
            return HttpResponse('ok')


def get_model_inf(request):
    if request.method == 'POST':
        if 'id' in request.POST:
            model = Product_model.objects.get(pk=request.POST['id'])
            data = {}
            data['name'] = model.name
            data['group'] = model.group.pk
            units = []
            for u in Model_unit.objects.filter(model=model):
                units.append(u.unit.pk)
            data["units"] = units
            props = {}
            for p in Model_property.objects.filter(model=model):
                props[str(p.pk)] = {"id": p.prop.pk, "visible": p.visible, "editable": p.editable,
                                    "isDefault": p.isDefault}
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


def get_good_inf(request):
    if request.method == 'POST':
        if 'id' in request.POST:
            good = Goods.objects.get(pk=request.POST['id'])
            data = {}
            names = Good_name.objects.filter(product=good)[0]
            data['name'] = names.name
            data['article'] = names.article
            data['barcode'] = names.barcode
            data['original'] = names.original
            data['local'] = names.local
            data['transit'] = names.transit
            data['model'] = good.model.pk
            data['counter'] = good.producer.pk
            units = {}
            for u in Goods_unit.objects.filter(product=good):
                if u.applicable:
                    units[str(u.pk)] = {"name": u.unit.name,"value": u.coeff, "isBase": u.isBase}
            data["units"] = units
            props = {}
            for p in Goods_property.objects.filter(product=good):
                if p.applicable and p.visible:
                    props[str(p.pk)] = {"name": p.property.name, "type": p.property.prop_type, "editable": p.editable , "value": "", "choises": None}
                    if p.property.prop_type == 0:
                        try:
                            props[str(p.pk)]["value"] = p.property_num.number
                        except AttributeError as error:
                            print(error)
                    else:
                        if p.property.prop_type == 1:
                            try:
                                props[str(p.pk)]["value"] = p.goods_string.text
                            except AttributeError as error:
                                print(error)
                        else:
                            props[str(p.pk)]["value"] = p.goods_var.var.id
                            props[str(p.pk)]["choises"] = {}
                            for v in Property_var.objects.filter(prop=p.property):
                                props[str(p.pk)]["choises"][str(v.pk)] = v.name
            data["props"] = props
            return HttpResponse(json.dumps(data))


def save_model(request):
    if request.method == 'POST':
        if 'name' in request.POST:
            group = Model_group.objects.get(pk=request.POST['group'])
            name = request.POST['name']
            units = json.loads(request.POST['units'])
            props = json.loads(request.POST['props'])
            model = Product_model(name=name, group=group)
            model.save()
            for u in units:
                unit = Unit.objects.get(pk=u)
                m = Model_unit(model=model, unit=unit)
                m.save()
            for p in props:
                prop = Property.objects.get(pk=int(props[p]["prop"]))
                if props[p]['isDefault']:
                    if prop.prop_type == 0:
                        d = Default_number(model=model, prop=prop, visible=not props[p]['hidden'],
                                           editable=not props[p]['uneditable'], isDefault=props[p]['isDefault'],
                                           number=props[p]['default'])
                        d.save()
                    else:
                        if prop.prop_type == 1:
                            d = Default_text(model=model, prop=prop, visible=not props[p]['hidden'],
                                             editable=not props[p]['uneditable'], isDefault=props[p]['isDefault'],
                                             text=props[p]['default'])
                            d.save()
                        else:
                            d = Default_var(model=model, prop=prop, visible=not props[p]['hidden'],
                                            editable=not props[p]['uneditable'], isDefault=props[p]['isDefault'],
                                            var=Property_var.objects.get(pk=props[p]['default']))
                            d.save()
                else:
                    m = Model_property(model=model, prop=prop, visible=not props[p]['hidden'],
                                       editable=not props[p]['uneditable'], isDefault=props[p]['isDefault'])
                    m.save()
            return HttpResponse('ok')


def save_good(request):
    if request.method == 'POST':
        if 'name' in request.POST:
            model = Product_model.objects.get(pk=request.POST['model'])
            counter = Counterparty.objects.get(pk=request.POST['counter'])
            name = request.POST['name']
            article = request.POST['article']
            barcode = request.POST['barcode']
            original = request.POST['original']
            local = request.POST['local']
            transit = request.POST['transit']
            units = json.loads(request.POST['units'])
            props = json.loads(request.POST['props'])
            good = Goods(model=model, producer=counter)
            good.save()
            names = Good_name(product=good, name=name, article=article, barcode=barcode, original=original, local=local,
                              transit=transit)
            names.save()
            for u in units:
                unit = Unit.objects.get(pk=u)
                m = Goods_unit(product=good, unit=unit, applicable=units[u]['applicable'], isBase=units[u]['isBase'],
                               coeff=units[u]['coeff'])
                m.save()
            for p in props:
                prop = Property.objects.get(pk=p)
                if prop.prop_type == 0:
                    d = Property_num(product=good, property=prop, applicable=props[p]['applicable'],
                                     visible=props[p]['visible'], editable=props[p]['editable'],
                                     number=props[p]['value'])
                    d.save()
                else:
                    if prop.prop_type == 1:
                        d = Goods_string(product=good, property=prop, applicable=props[p]['applicable'],
                                         visible=props[p]['visible'], editable=props[p]['editable'],
                                         text=props[p]['value'])
                        d.save()
                    else:
                        d = Goods_var(product=good, property=prop, applicable=props[p]['applicable'],
                                      visible=props[p]['visible'], editable=props[p]['editable'],
                                      var=Property_var.objects.get(pk=props[p]['value']))
                        d.save()
            return HttpResponse('ok')

def edit_good(request):
    if request.method == 'POST':
        if 'name' in request.POST:
            good = Goods.objects.get(pk=request.POST['id'])
            counter = Counterparty.objects.get(pk=request.POST['counter'])
            name = request.POST['name']
            article = request.POST['article']
            barcode = request.POST['barcode']
            original = request.POST['original']
            local = request.POST['local']
            transit = request.POST['transit']
            units = json.loads(request.POST['units'])
            props = json.loads(request.POST['props'])
            good.producer = counter
            good.save()
            names = Good_name.objects.filter(product = good)[0]
            names.name=name
            names.article=article
            names.barcode=barcode
            names.original=original
            names.local=local
            names.transit=transit
            names.save()
            for u in units:
                unit = Goods_unit.objects.get(pk=u)
                unit.isBase = units[u]['isBase']
                unit.coeff = units[u]['coeff']
                unit.save()
            for p in props:
                prop = Goods_property.objects.get(pk=p)
                if prop.property.prop_type == 0:
                    prop.number = props[p]['value']
                    prop.save()
                else:
                    if prop.property.prop_type == 1:
                        prop.text = props[p]['value']
                        prop.save()
                    else:
                        prop.var = Property_var.objects.get(pk=props[p]['value'])
                        prop.save()
            return HttpResponse('ok')

def edit_model(request):
    if request.method == 'POST':
        if 'name' in request.POST:
            group = Model_group.objects.get(pk=request.POST['group'])
            name = request.POST['name']
            units = json.loads(request.POST['units'])
            props = json.loads(request.POST['props'])
            model = Product_model.objects.get(pk=request.POST['id'])
            model.name = name
            model.group = group
            model.save()
            Model_unit.objects.filter(model=model).delete()
            for u in units:
                unit = Unit.objects.get(pk=u)
                m = Model_unit(model=model, unit=unit)
                m.save()
            Model_property.objects.filter(model=model).delete()
            for p in props:
                prop = Property.objects.get(pk=int(props[p]["prop"]))
                if props[p]['isDefault']:
                    if prop.prop_type == 0:
                        d = Default_number(model=model, prop=prop, visible=not props[p]['hidden'],
                                           editable=not props[p]['uneditable'], isDefault=props[p]['isDefault'],
                                           number=props[p]['default'])
                        d.save()
                    else:
                        if prop.prop_type == 1:
                            d = Default_text(model=model, prop=prop, visible=not props[p]['hidden'],
                                             editable=not props[p]['uneditable'], isDefault=props[p]['isDefault'],
                                             text=props[p]['default'])
                            d.save()
                        else:
                            d = Default_var(model=model, prop=prop, visible=not props[p]['hidden'],
                                            editable=not props[p]['uneditable'], isDefault=props[p]['isDefault'],
                                            var=Property_var.objects.get(pk=props[p]['default']))
                            d.save()
                else:
                    m = Model_property(model=model, prop=prop, visible=not props[p]['hidden'],
                                       editable=not props[p]['uneditable'], isDefault=props[p]['isDefault'])
                    m.save()
            return HttpResponse('ok')


def save_group(request):
    if request.method == 'POST':
        if 'name' in request.POST:
            if request.POST['id'] != '':
                group = Model_group.objects.get(pk=request.POST['id'])
                group.name = request.POST['name']
            else:
                group = Model_group(name=request.POST['name'], parent=request.POST['parent'])
            group.save()
            return HttpResponse(group.pk)


def del_group(request):
    if request.method == 'POST':
        Model_group.objects.get(pk=request.POST['id']).delete()
        return HttpResponse("ok")


def del_model(request):
    if request.method == 'POST':
        Product_model.objects.get(pk=request.POST['id']).delete()
        return HttpResponse("ok")

def del_good(request):
    if request.method == 'POST':
        Goods.objects.get(pk=request.POST['id']).delete()
        return HttpResponse("ok")

def del_counter(request):
    if request.method == 'POST':
        Counterparty.objects.get(pk=request.POST['id']).delete()
        return HttpResponse("ok")

def del_prop(request):
    if request.method == 'POST':
        Property.objects.get(pk=request.POST['id']).delete()
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
                    Property_var.objects.filter(prop=prop).delete()
                    for d in data:
                        p = Property_var(prop=prop, name=d)
                        p.save()
            return HttpResponse('ok')
