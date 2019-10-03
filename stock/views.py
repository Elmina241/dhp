from django.http.response import HttpResponse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect, render_to_response
import json
from tables.models import Unit
from django.db.models import Q
from .models import *
from django.core import serializers
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
# from django.contrib import auth
import datetime
from django.contrib.auth.models import User
import timeit


def goods_models(request):
    tree = {}
    tree[0] = {"name": "root", "nodes": {}}
    g = Model_group.objects.all().first()
    add_children(g, tree[0])
    model_json = {}
    for m in Product_model.objects.all():
        model_json[str(m.pk)] = {"id": m.pk, "name": m.name, "group": m.group.pk}
    return render(request, "goods_models.html",
                  {"permissions": json.dumps(User_group.objects.filter(user=request.user)[0].get_permissions()),
                   "user_group": str(User_group.objects.filter(user=request.user)[0].group),
                   "header": "Макеты материальных ценностей", "models": Product_model.objects.all(),
                   "prop_vars": json.dumps(serializers.serialize("json", Property_var.objects.all())),
                   "tree": json.dumps(tree), "model_json": json.dumps(model_json),
                   "props": json.dumps(serializers.serialize("json", Property.objects.all())),
                   "groups": Model_group.objects.exclude(pk=0),
                   "units": json.dumps(serializers.serialize("json", Unit.objects.all()))})


def stocks(request):
    tree = {}
    tree[0] = {"name": "root", "nodes": {}}
    g = Model_group.objects.all().first()
    add_children(g, tree[0])
    goods_json = {}
    for g in Model_group.objects.all():
        if str(g.pk) not in goods_json:
            goods_json[str(g.pk)] = {}
        for s in Stock.objects.all():
            if str(s.pk) not in goods_json[str(g.pk)]:
                goods_json[str(g.pk)][str(s.pk)] = {}
            for r in Stock_good.objects.filter(stock=s, good__model__group=g):
                #goods_json["1"][str(s.pk)][str(r.pk)] = {"code": r.good.get_article(), "name": r.good.get_name(),
                                                         #"amount": r.amount, "unit": str(r.unit), "cost": r.cost}
                goods_json[str(g.pk)][str(s.pk)][str(r.pk)] = {"code": r.good.get_article(), "name": r.good.get_name(),
                                                               "amount": r.amount, "unit": str(r.unit), "cost": r.cost}
    return render(request, "stocks.html",
                  {"permissions": json.dumps(User_group.objects.filter(user=request.user)[0].get_permissions()),
                   "header": "Склад", "tree": json.dumps(tree), "counters": Counterparty.objects.all(),
                   "user_group": str(User_group.objects.filter(user=request.user)[0].group),
                   "models": Product_model.objects.all(), "stocks": Stock.objects.all(),
                   "goods_json": json.dumps(goods_json), "goods": Goods.objects.all()})


def inventory(request):
    tree = {}
    tree[0] = {"name": "root", "nodes": {}}
    g = Model_group.objects.all().first()
    add_children_g(g, tree[0])
    goods_inf_res = get_goods_inf()
    goods = goods_inf_res['goods']
    goods_inf = goods_inf_res['goods_inf']
    inventory_goods = {}
    for i in Inventory.objects.filter(is_finished=False):
        inventory_goods[str(i.pk)] = {'date': i.date.strftime('%d.%m.%Y'), 'stock': str(i.stock),
                                      'stock_id': i.stock.pk}
        for g in Inventory_good.objects.filter(inventory=i):
            if Stock_good.objects.filter(stock=i.stock, good=g.good).count() != 0:
                s_g = Stock_good.objects.filter(stock=i.stock, good=g.good)[0]
                amount = s_g.amount
                if s_g.amount != 0:
                    price = s_g.cost / s_g.amount
                else:
                    price = s_g.cost
            else:
                amount = 0
                price = 0
            inventory_goods[str(i.pk)][str(g.good.pk)] = {'article': g.good.get_article(), 'name': g.good.get_name(),
                                                          'unit': str(g.good.get_unit()), 'price': price,
                                                          'amount': amount}
    return render(request, "inventory.html",
                  {"permissions": json.dumps(User_group.objects.filter(user=request.user)[0].get_permissions()),
                   "header": "Инвентаризация", "tree": json.dumps(tree),
                   'inventories': Inventory.objects.filter(is_finished=False),
                   "user_group": str(User_group.objects.filter(user=request.user)[0].group), "goods": json.dumps(goods),
                   "inventory_goods": json.dumps(inventory_goods), "goods_inf": json.dumps(goods_inf),
                   "stocks": Counter_stock.objects.filter(
                       counter=User_group.objects.filter(user=request.user)[0].group)})


def auth(request):
    users = User.objects.all()
    if request.user.is_authenticated:
        return redirect('main')
    else:
        return render(request, "login.html", {"users": users})


def main(request):
    return render(request, "main-page.html", {"user_group": str(User_group.objects.filter(user=request.user)[0].group),
                                              "permissions": json.dumps(
                                                  User_group.objects.filter(user=request.user)[0].get_permissions()),
                                              "header": "Главная страница"})


def logout(request):
    auth_logout(request)
    return redirect('auth')


def login(request):
    if request.POST:
        username = request.POST['user']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('auth')
        else:
            return render(request, "login.html", {'error': 'Неверный пароль', 'users': User.objects.all()})
    else:
        return redirect("auth")


def goods(request):
    tree = {}
    tree[0] = {"name": "root", "nodes": {}}
    g = Model_group.objects.all().first()
    add_children(g, tree[0])
    goods_json = {}
    for m in Goods.objects.all():
        # names = Good_name.objects.filter(product=m)[0]
        goods_json[str(m.pk)] = {"id": m.pk, "name": m.get_name(), "article": m.get_article(),
                                 "group": m.model.group.pk}
    models = {}
    for m in Product_model.objects.all():
        models[str(m.pk)] = {"units": {}, "props": {}}
        for u in Model_unit.objects.filter(model=m):
            models[str(m.pk)]["units"][str(u.unit.pk)] = {"name": u.unit.name}
        for p in Model_property.objects.filter(model=m):
            models[str(m.pk)]["props"][str(p.prop.pk)] = {"name": p.prop.name, "type": p.prop.prop_type,
                                                          "visible": p.visible, "editable": p.editable, "default": "",
                                                          "choises": {}}
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
            if p.prop.prop_type == 2:
                for v in Property_var.objects.filter(prop=p.prop):
                    models[str(m.pk)]["props"][str(p.prop.pk)]["choises"][str(v.pk)] = v.name
    return render(request, "goods.html",
                  {"permissions": json.dumps(User_group.objects.filter(user=request.user)[0].get_permissions()),
                   "header": "Материальные ценности", "tree": json.dumps(tree), "counters": Counterparty.objects.all(),
                   "user_group": str(User_group.objects.filter(user=request.user)[0].group),
                   "models": Product_model.objects.all(), "model_json": json.dumps(models),
                   "goods_json": json.dumps(goods_json), "goods": Goods.objects.all(),
                   'username': request.user.username})


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
        for m in Product_model.objects.filter(group=o):
            node['nodes'][o.id]['nodes']['m_' + str(m.pk)] = {"name": m.name, "id": 'm_' + str(m.id)}
            node['nodes'][o.id]['nodes']['m_' + str(m.pk)]['nodes'] = {}
            for g in Goods.objects.filter(model=m):
                node['nodes'][o.id]['nodes']['m_' + str(m.pk)]['nodes']['g_' + str(g.pk)] = {"name": g.get_full_name('0'),
                                                                                             "id": 'g_' + str(g.id)}
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
    return render(request, "props.html",
                  {"permissions": json.dumps(User_group.objects.filter(user=request.user)[0].get_permissions()),
                   "header": "Свойства материальных ценностей", "props": Property.objects.all(),
                   "user_group": str(User_group.objects.filter(user=request.user)[0].group),
                   "prop_data": json.dumps(prop_data)})


def counterparties(request):
    counter_data = {}
    for c in Counterparty.objects.all():
        counter_data[str(c.pk)] = {'name': c.name, 'kind': c.kind, 'is_provider': c.is_provider,
                                   'is_consumer': c.is_consumer, 'is_member': c.is_member, 'stocks': {}}
        for s in Counter_stock.objects.filter(counter=c):
            counter_data[str(c.pk)]['stocks'][str(s.stock.pk)] = {'name': s.stock.name}
    return render(request, "counterparties.html",
                  {"user_group": str(User_group.objects.filter(user=request.user)[0].group),
                   "permissions": json.dumps(User_group.objects.filter(user=request.user)[0].get_permissions()),
                   "count_data": json.dumps(counter_data), "header": "Контрагенты",
                   "counters": Counterparty.objects.all(),
                   "stockData": json.dumps(serializers.serialize("json", Stock.objects.all()))})


def storages2(request):
    return render(request, "storages2.html", {"user_group": str(User_group.objects.filter(user=request.user)[0].group),
                                              "permissions": json.dumps(
                                                  User_group.objects.filter(user=request.user)[0].get_permissions()),
                                              "header": "Склады", "stocks": Stock.objects.all()})


def get_goods_inf():
    goods_inf = {}
    goods_inf['goods'] = []
    goods_inf['goods_inf'] = {}
    i = 0
    for g in Goods.objects.all():
        for t in Good_name.AREA_CHOICES:
            full_name = g.get_full_name(t[0])
            if full_name != "":
                goods_inf['goods'].append(full_name)
                goods_inf['goods_inf'][i] = t[0] + '_' + str(g.pk)
                i = i + 1
    return goods_inf


def shipment(request):
    tree = {}
    tree[0] = {"name": "root", "nodes": {}}
    g = Model_group.objects.all().first()
    add_children_g(g, tree[0])
    goods_inf_res = get_goods_inf()
    goods = goods_inf_res['goods']
    goods_inf = goods_inf_res['goods_inf']
    goods_json = {}
    for r in Goods.objects.all():
        goods_json[str(r.pk)] = {"article": r.get_article(), "name": r.get_name(), "unit": str(r.get_unit())}
    units = {}
    causes = {}
    for c in Order.CAUSE_CHOICES:
        causes[c[0]] = {'name': c[1]}
    for u in Goods_unit.objects.all():
        units[str(u.pk)] = {'pk': u.unit.pk, 'product': u.product.pk, 'applicable': u.applicable, 'unit': u.unit.name,
                            'is_base': u.isBase}
    stocks = {}
    for s in Counter_stock.objects.all():
        stocks[str(s.pk)] = {'pk': s.stock.pk, 'counter': s.counter.pk, 'stock': s.stock.name}
    counter = User_group.objects.filter(user=request.user)[0]
    reqs = {}
    for r in Demand.objects.filter(provider=counter.group, matrix__access='4'):
        if Order.objects.filter(matrix=r.matrix, isDonor=True).count() != 0:
            if Order.objects.filter(matrix=r.matrix, isDonor=True)[0].status != '2':
                if r.consumer == counter.group:
                    role = '2'
                else:
                    if r.provider == counter.group:
                        role = '1'
                    else:
                        role = '0'
                reqs[str(r.pk)] = {
                    'id': r.pk,
                    'date': r.date.strftime('%d.%m.%Y'),
                    'consumer': "-" if r.consumer is None else str(r.consumer),
                    'provider': "-" if r.provider is None else str(r.provider),
                    'donor': "" if r.donor is None else str(r.donor),
                    'acceptor': "" if r.acceptor is None else str(r.acceptor),
                    'donor_id': "-" if r.donor is None else r.donor.pk,
                    'acceptor_id': "-" if r.acceptor is None else r.acceptor.pk,
                    'role': role,
                    'vin': r.vin,
                    'cause': Order.objects.filter(matrix=r.matrix, isDonor=True)[0].get_cause_display(),
                    'user': "-" if r.user is None else str(r.user),
                    'release_date': "-" if r.release_date is None else r.release_date.strftime('%d.%m.%Y'),
                    'finish_date': "-" if r.finish_date is None else r.finish_date.strftime('%d.%m.%Y')
                }
    stocks = {}
    for s in Counter_stock.objects.all():
        stocks[str(s.pk)] = {'pk': s.stock.pk, 'counter': s.counter.pk, 'stock': s.stock.name}
    return render(request, "shipment.html", {"user_group": str(User_group.objects.filter(user=request.user)[0].group),
                                             "permissions": json.dumps(
                                                 User_group.objects.filter(user=request.user)[0].get_permissions()),
                                             "header": "Отпуск",
                                             'stocks': Counter_stock.objects.filter(counter=counter.group),
                                             'causes': causes, 'reqs': json.dumps(reqs), "tree": json.dumps(tree),
                                             "goods": json.dumps(goods), "goods_json": json.dumps(goods_json),
                                             "goods_inf": json.dumps(goods_inf), "counter": counter.group,
                                             "units": json.dumps(units), "stockData": json.dumps(stocks),
                                             "counters": Counterparty.objects.all(), "stock_inf": json.dumps(get_stock_inf())})


def get_stock_goods(request):
    if request.method == 'POST':
        if 'id' in request.POST:
            stock = Stock.objects.get(pk=request.POST['id'])
            goods = {}
            for g in Stock_good.objects.filter(stock=stock):
                if g.amount != 0:
                    cost = g.cost / g.amount
                else:
                    cost = 0
                goods[str(g.good.pk)] = {'id': g.good.pk, 'article': g.good.get_article(), 'name': g.good.get_name(),
                                         'unit': str(g.unit), 'amount': g.amount, 'cost': cost}
            return HttpResponse(json.dumps(goods))

def get_stock_inf():
    data = {}
    for s in Stock.objects.all():
        data[str(s.pk)] = {}
        for r in Stock_good.objects.filter(stock=s):
            data[str(s.pk)][str(r.good.pk)] = r.amount
    return data

def supplies(request):
    tree = {}
    tree[0] = {"name": "root", "nodes": {}}
    g = Model_group.objects.all().first()
    add_children_g(g, tree[0])
    goods_inf_res = get_goods_inf()
    goods = goods_inf_res['goods']
    goods_inf = goods_inf_res['goods_inf']
    goods_json = {}
    for r in Goods.objects.all():
        goods_json[str(r.pk)] = {"article": r.get_article(), "name": r.get_name(), "unit": str(r.get_unit())}
    causes = {}
    for c in Order.CAUSE_CHOICES:
        causes[c[0]] = {'name': c[1]}
    units = {}
    for u in Goods_unit.objects.all():
        units[str(u.pk)] = {'pk': u.unit.pk, 'product': u.product.pk, 'applicable': u.applicable, 'unit': u.unit.name,
                            'is_base': u.isBase}
    stocks = {}
    for s in Counter_stock.objects.all():
        stocks[str(s.pk)] = {'pk': s.stock.pk, 'counter': s.counter.pk, 'stock': s.stock.name}
    counter = User_group.objects.filter(user=request.user)[0]
    reqs = {}
    for r in Demand.objects.filter(consumer=counter.group, matrix__access='4'):
        if Order.objects.filter(matrix=r.matrix, isDonor=False).count() != 0:
            if Order.objects.filter(matrix=r.matrix, isDonor=False)[0].status != '2':
                if r.consumer == counter.group:
                    role = '2'
                else:
                    if r.provider == counter.group:
                        role = '1'
                    else:
                        role = '0'
                reqs[str(r.pk)] = {
                    'id': r.pk,
                    'date': r.date.strftime('%d.%m.%Y'),
                    'consumer': "-" if r.consumer is None else str(r.consumer),
                    'provider': "-" if r.provider is None else str(r.provider),
                    'donor': "" if r.donor is None else str(r.donor),
                    'acceptor': "" if r.acceptor is None else str(r.acceptor),
                    'donor_id': "-" if r.donor is None else r.donor.pk,
                    'acceptor_id': "-" if r.acceptor is None else r.acceptor.pk,
                    'role': role,
                    'vin': r.vin,
                    'cause': Order.objects.filter(matrix=r.matrix, isDonor=False)[0].get_cause_display(),
                    'user': "-" if r.user is None else str(r.user),
                    'release_date': "-" if r.release_date is None else r.release_date.strftime('%d.%m.%Y'),
                    'finish_date': "-" if r.finish_date is None else r.finish_date.strftime('%d.%m.%Y')
                }
    stocks = {}
    for s in Counter_stock.objects.all():
        stocks[str(s.pk)] = {'pk': s.stock.pk, 'counter': s.counter.pk, 'stock': s.stock.name}
    return render(request, "supplies.html", {"user_group": str(User_group.objects.filter(user=request.user)[0].group),
                                             "permissions": json.dumps(
                                                 User_group.objects.filter(user=request.user)[0].get_permissions()),
                                             'causes': causes, "header": "Поступления",
                                             'stocks': Counter_stock.objects.filter(counter=counter.group),
                                             'reqs': json.dumps(reqs), "tree": json.dumps(tree),
                                             "goods": json.dumps(goods), "goods_json": json.dumps(goods_json),
                                             "goods_inf": json.dumps(goods_inf), "counter": counter.group,
                                             "units": json.dumps(units), "stockData": json.dumps(stocks),
                                             "counters": Counterparty.objects.all(), "stock_inf": json.dumps(get_stock_inf())})


def offers(request):
    counter = User_group.objects.filter(user=request.user)[0]
    reqs = {}
    for r in Demand.objects.filter(Q(consumer=counter.group) | Q(provider=counter.group)).filter(is_closed=False,
                                                                                                 is_demand=False).exclude(
            matrix__access='4'):
        if r.consumer == counter.group:
            role = '2'
        else:
            if r.provider == counter.group:
                role = '1'
            else:
                role = '0'
        reqs[str(r.pk)] = {
            'id': r.pk,
            'date': r.date.strftime('%d.%m.%Y'),
            'release_date': "-" if r.release_date is None else r.release_date.strftime('%d.%m.%Y'),
            'finish_date': "-" if r.finish_date is None else r.finish_date.strftime('%d.%m.%Y'),
            'consumer': str(r.consumer),
            'provider': str(r.provider),
            'donor': "-" if r.donor is None else str(r.donor),
            'acceptor': "-" if r.acceptor is None else str(r.acceptor),
            'donor_id': "-" if r.donor is None else r.donor.pk,
            'acceptor_id': "-" if r.acceptor is None else r.acceptor.pk,
            'access': r.matrix.access,
            'role': role,
            'user': "-" if r.user is None else str(r.user),
            'isEdited': r.is_edited,
            'vin': r.vin
        }
    tree = {}
    tree[0] = {"name": "root", "nodes": {}}
    g = Model_group.objects.all().first()
    add_children_g(g, tree[0])
    goods_inf_res = get_goods_inf()
    goods = goods_inf_res['goods']
    goods_inf = goods_inf_res['goods_inf']
    units = {}
    for u in Goods_unit.objects.all():
        units[str(u.pk)] = {'pk': u.unit.pk, 'product': u.product.pk, 'applicable': u.applicable, 'unit': u.unit.name,
                            'is_base': u.isBase}
    stocks = {}
    for s in Counter_stock.objects.all():
        stocks[str(s.pk)] = {'pk': s.stock.pk, 'counter': s.counter.pk, 'stock': s.stock.name}
    return render(request, "offers.html", {"user_group_pk": User_group.objects.filter(user=request.user)[0].group.pk,
                                           "user_group": str(User_group.objects.filter(user=request.user)[0].group),
                                           "permissions": json.dumps(
                                               User_group.objects.filter(user=request.user)[0].get_permissions()),
                                           "header": "Предложения", "reqs": json.dumps(reqs), "counter": counter.group,
                                           "tree": json.dumps(tree),
                                           'stocks': Counter_stock.objects.filter(counter=counter.group),
                                           "goods": json.dumps(goods), "goods_inf": json.dumps(goods_inf),
                                           "units": json.dumps(units), "stockData": json.dumps(stocks),
                                           "counters": Counterparty.objects.all(), "stock_inf": json.dumps(get_stock_inf())})


def requirements(request):
    counter = User_group.objects.filter(user=request.user)[0]
    reqs = {}
    for r in Demand.objects.filter(Q(consumer=counter.group) | Q(provider=counter.group)).filter(
            is_closed=False).filter(is_demand=True).exclude(matrix__access='4').order_by('-pk'):
        if r.consumer == counter.group:
            role = '2'
        else:
            if r.provider == counter.group:
                role = '1'
            else:
                role = '0'
        reqs[str(r.pk)] = {
            'id': r.pk,
            'date': r.date.strftime('%d.%m.%Y'),
            'release_date': "-" if r.release_date is None else r.release_date.strftime('%d.%m.%Y'),
            'finish_date': "-" if r.finish_date is None else r.finish_date.strftime('%d.%m.%Y'),
            'consumer': str(r.consumer),
            'provider': str(r.provider),
            'donor': "-" if r.donor is None else str(r.donor),
            'acceptor': str(r.acceptor),
            'donor_id': "-" if r.donor is None else r.donor.pk,
            'acceptor_id': "-" if r.acceptor is None else r.acceptor.pk,
            'access': r.matrix.access,
            'role': role,
            'user': "-" if r.user is None else str(r.user),
            'isEdited': r.is_edited,
            'vin': r.vin
        }
    tree = {}
    tree[0] = {"name": "root", "nodes": {}}
    g = Model_group.objects.all().first()
    add_children_g(g, tree[0])
    goods_inf_res = get_goods_inf()
    goods = goods_inf_res['goods']
    goods_inf = goods_inf_res['goods_inf']
    units = {}
    for u in Goods_unit.objects.all():
        units[str(u.pk)] = {'pk': u.unit.pk, 'product': u.product.pk, 'applicable': u.applicable, 'unit': u.unit.name,
                            'is_base': u.isBase}
    stocks = {}
    for s in Counter_stock.objects.all():
        stocks[str(s.pk)] = {'pk': s.stock.pk, 'counter': s.counter.pk, 'stock': s.stock.name}
    return render(request, "requirements.html",
                  {"user_group_pk": User_group.objects.filter(user=request.user)[0].group.pk,
                   "user_group": str(User_group.objects.filter(user=request.user)[0].group),
                   "permissions": json.dumps(User_group.objects.filter(user=request.user)[0].get_permissions()),
                   "header": "Заказы", "reqs": json.dumps(reqs), "tree": json.dumps(tree),
                   'stocks': Counter_stock.objects.filter(counter=counter.group), "goods": json.dumps(goods),
                   "goods_inf": json.dumps(goods_inf), "units": json.dumps(units), "counter": counter.group,
                   "stockData": json.dumps(stocks), "counters": Counterparty.objects.all(), "stock_inf": json.dumps(get_stock_inf())})


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


def send_stock(request):
    if request.method == 'POST':
        if 'name' in request.POST:
            name = request.POST['name']
            stock = Stock(name=name)
            stock.save()
            return HttpResponse('ok')


def save_changed_stock(request):
    if request.method == 'POST':
        if 'id' in request.POST:
            req = Demand.objects.get(pk=request.POST['id'])
            stock = Stock.objects.get(pk=request.POST['stock'])
            if request.POST['is_donor'] == 'true':
                req.donor = stock
            else:
                req.acceptor = stock
            req.save()
            return HttpResponse('ok')


def save_stock(request):
    if request.method == 'POST':
        if 'id' in request.POST:
            stock = Stock.objects.get(pk=request.POST['id'])
            name = request.POST['name']
            stock.name = name
            stock.save()
            return HttpResponse('ok')


def get_prod_info(request):
    if request.method == 'POST':
        if 'id' in request.POST:
            stock = Stock.objects.get(pk=request.POST['stock'])
            good = Stock_good.objects.get(pk=request.POST['id']).good
            data = {}
            names = {}
            units = {}
            for n in Good_name.objects.filter(product=good):
                names[str(n.pk)] = {'type': n.get_name_type_display(), 'area': n.get_area_display(), 'name': n.name}
            s_g = Stock_good.objects.get(pk=request.POST['id'])
            base_amm = s_g.amount / Goods_unit.objects.filter(product=good, unit=s_g.unit)[0].coeff
            for g in Goods_unit.objects.filter(product=good):
                coeff = Goods_unit.objects.filter(product=good, unit=g.unit)[0].coeff
                units[str(g)] = {'amount': base_amm * coeff, "unit": str(g.unit)}
            data['names'] = names
            data['units'] = units
            expecting = {}
            for d in Demand_good.objects.filter(good=good, matrix__access='4'):
                if (
                        d.get_demand().donor == stock or d.get_demand().acceptor == stock) and d.get_demand().is_closed == False and d.balance != 0:
                    operation = 'Отгрузка' if d.get_demand().donor == stock else 'Поставка'
                    if Order.objects.filter(matrix=d.matrix, isDonor=(operation == 'Отгрузка')).count() != 0:
                        if Order.objects.filter(matrix=d.matrix, isDonor=(operation == 'Отгрузка'))[0].status != '2':
                            expecting[str(d.pk)] = {'vin': d.get_demand().vin,
                                                    'date': d.get_demand().finish_date.strftime('%d.%m.%Y'),
                                                    'amount': d.balance, 'operation': operation}
            data['expecting'] = expecting
            history = {}
            for o in Stock_operation.objects.filter(good=good, package__stock=stock).exclude(operation='2'):
                history[str(o.pk)] = {'vin': o.package.vin, 'date': o.package.date.strftime('%d.%m.%Y'),
                                      'operation': o.get_operation_display(), 'amount': o.amount, 'unit': str(o.unit)}
            data['history'] = history
            return HttpResponse(json.dumps(data))


def send_counter(request):
    if request.method == 'POST':
        if 'name' in request.POST:
            kind = request.POST['kind']
            name = request.POST['name']
            c = Counterparty(name=name, kind=kind, is_provider=json.loads(request.POST['isProv']),
                             is_consumer=json.loads(request.POST['isCons']),
                             is_member=json.loads(request.POST['isMember']))
            c.save()
            data = json.loads(request.POST['stocks'])
            for d in data:
                p = Counter_stock(counter=c, stock=Stock.objects.get(pk=d))
                p.save()
            return HttpResponse('ok')


def edit_counter(request):
    if request.method == 'POST':
        if 'id' in request.POST:
            counter = Counterparty.objects.get(pk=request.POST['id'])
            counter.name = request.POST['name']
            counter.kind = request.POST['kind']
            counter.is_provider = json.loads(request.POST['isProv'])
            counter.is_consumer = json.loads(request.POST['isCons'])
            counter.is_member = json.loads(request.POST['isMember'])
            counter.save()
            Counter_stock.objects.filter(counter=counter).delete()
            data = json.loads(request.POST['stocks'])
            for d in data:
                p = Counter_stock(counter=counter, stock=Stock.objects.get(pk=d))
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


def get_demand_goods(request):
    if request.method == 'POST':
        if 'id' in request.POST:
            demand = Demand.objects.get(pk=request.POST['id'])
            data = {}
            if request.POST['t'] == 's':
                if Order.objects.filter(matrix=demand.matrix, isDonor=True).count() == 0:
                    data['is_finished'] = True
                else:
                    ord = Order.objects.filter(matrix=demand.matrix, isDonor=True)[0]
                    data['is_finished'] = ord.status is '2'
            for d in Demand_good.objects.filter(matrix=demand.matrix):
                b_amount = Goods_unit.objects.filter(product=d.good, unit=d.unit)[0].coeff * d.amount
                data[str(d.pk)] = {'article': d.article, 'name': d.name, 'amount': d.amount, 'unit': str(d.unit)}
                if request.POST['t'] == 's':
                    data[str(d.pk)]['balance'] = d.balance
            return HttpResponse(json.dumps(data))


def save_req_goods(request):
    if request.method == 'POST':
        if 'goods' in request.POST:
            goods = json.loads(request.POST['goods'])
            for g in goods:
                d = Demand_good.objects.get(pk=g)
                d.amount = goods[g]
                d.balance = goods[g]
                matrix = d.matrix
                d.save()
            dem = Demand.objects.filter(matrix=matrix)[0]
            dem.is_edited = True
            dem.save()
            return HttpResponse('ok')


def save_date(request):
    if request.method == 'POST':
        if 'id' in request.POST:
            d = Demand.objects.get(pk=request.POST['id'])
            if request.POST['t'] == '0':
                d.release_date = datetime.datetime.strptime(request.POST['date'], "%Y-%m-%d").date()
                date = d.release_date
            else:
                d.finish_date = datetime.datetime.strptime(request.POST['date'], "%Y-%m-%d").date()
                date = d.finish_date
            d.save()
            return HttpResponse(date.strftime('%d.%m.%Y'))


def save_stock_operation(request):
    if request.method == 'POST':
        if 'id' in request.POST:
            demand = Demand.objects.get(pk=request.POST['id'])
            goods = json.loads(request.POST['goods'])
            m = Matrix(access='0', cause=request.POST['cause'], cause_id=request.POST['id'])
            m.save()
            if json.loads(request.POST['isDonor']) == True:
                stock = demand.donor
            else:
                stock = demand.acceptor
            if request.POST['operation'] == '0':
                p = Package(matrix=m, vin=demand.acceptor.cur_vin, stock=stock, date=datetime.datetime.now())
                p.save()
                demand.acceptor.cur_vin = demand.acceptor.cur_vin + 1
                demand.acceptor.save()
            if request.POST['operation'] == '1':
                p = Package(matrix=m, vin=demand.donor.cur_vin, stock=stock, date=datetime.datetime.now())
                p.save()
                demand.donor.cur_vin = demand.donor.cur_vin + 1
                demand.donor.save()
            balance = 0
            for g in goods:
                amount = float(goods[g]['amount'].replace(',', '.'))
                good_d = Demand_good.objects.get(pk=goods[g]['id'])
                s = Stock_operation(
                    package=p,
                    good=good_d.good,
                    operation=request.POST['operation'],
                    unit=good_d.unit,
                    amount=amount
                )
                s.save()
                good_d.balance = good_d.balance - amount
                good_d.save()
                balance = balance + good_d.balance
                # добавление информации в склад
                if json.loads(request.POST['isDonor']) != True:
                    amount = Goods_unit.objects.filter(product=good_d.good, unit=good_d.unit)[0].coeff * amount
                    if Stock_good.objects.filter(stock=demand.acceptor, good=good_d.good).count() == 0:
                        rec = Stock_good(stock=demand.acceptor, good=good_d.good,
                                         unit=Goods_unit.objects.filter(product=good_d.good, isBase=True)[0].unit,
                                         amount=amount)
                        rec.save()
                    else:
                        rec = Stock_good.objects.filter(stock=demand.acceptor, good=good_d.good)[0]
                        if rec.amount != 0:
                            cost = (rec.cost / rec.amount) * amount
                        else:
                            cost = 0
                        rec.amount = rec.amount + amount
                        rec.cost = float(rec.cost + cost)
                        rec.save()
                else:
                    if Stock_good.objects.filter(stock=demand.donor, good=good_d.good).count() != 0:
                        amount = Goods_unit.objects.filter(product=good_d.good, unit=good_d.unit)[0].coeff * amount
                        rec = Stock_good.objects.filter(stock=demand.donor, good=good_d.good)[0]
                        if rec.amount != 0:
                            cost = (rec.cost / rec.amount) * amount
                        else:
                            cost = 0
                        rec.amount = rec.amount - amount
                        rec.cost = float(rec.cost - cost)
                        rec.save()
                if balance == 0:
                    if json.loads(request.POST['isDonor']):
                        for g in goods:
                            good_d = Demand_good.objects.get(pk=goods[g]['id'])
                            good_d.balance = good_d.amount
                            good_d.save()
                    ord = Order.objects.filter(matrix=demand.matrix, isDonor=json.loads(request.POST['isDonor']))[0]
                    ord.status = '2'
                    ord.save()
            return HttpResponse('ok')


def stock_operations(request):
    user = request.user
    counter = User_group.objects.filter(user=user)[0].group
    tree = {}
    tree[0] = {"name": "root", "nodes": {}}
    g = Model_group.objects.all().first()
    add_children_g(g, tree[0])
    goods_inf_res = get_goods_inf()
    goods = goods_inf_res['goods']
    goods_inf = goods_inf_res['goods_inf']
    goods_json = {}
    for r in Goods.objects.all():
        goods_json[str(r.pk)] = {"article": r.get_article(), "name": r.get_name(), "unit": str(r.get_unit())}
    units = {}
    for u in Goods_unit.objects.all():
        units[str(u.pk)] = {'pk': u.unit.pk, 'product': u.product.pk, 'applicable': u.applicable, 'unit': u.unit.name,
                            'is_base': u.isBase}
    stocks = {}
    for s in Counter_stock.objects.all():
        stocks[str(s.pk)] = {'pk': s.stock.pk, 'counter': s.counter.pk, 'stock': s.stock.name}
    operations = {}
    stock_operations_res = Stock_operation.objects.none()
    for stock in Counter_stock.objects.filter(counter=counter):
        stock_operations_res = stock_operations_res | Stock_operation.objects.filter(package__stock=stock.stock)
    stock_operations_res = stock_operations_res.order_by('-date')
    for s in stock_operations_res:
        id = s.package.pk
        demands = Demand.objects.filter(pk=s.package.matrix.cause_id)
        if s.package.matrix.cause_id is None or demands.count() == 0:
            cause = 'Инвентаризация'
        else:
            demand = demands[0]
            cause = Order.objects.filter(matrix=demand.matrix)[0].get_cause_display()
        if id not in operations:
            operations[id] = {"date": s.package.date.strftime('%d.%m.%Y'), "operation": s.get_operation_display(),
                              "vin": s.package.vin, "stock": str(s.package.stock), "cause": cause,
                              "stock_id": s.package.stock.pk}
        operations[id][str(s.good.pk)] = {"article": s.good.get_article(), "name": s.good.get_name(),
                                          "unit": str(s.unit), "amount": s.amount, "cost": s.cost}
        if s.operation == '2':
            operations[id][str(s.good.pk)]['diffr'] = s.amount - float(s.last_value)
    return render(request, "stock_operations.html",
                  {"user_group": str(User_group.objects.filter(user=request.user)[0].group),
                   "permissions": json.dumps(User_group.objects.filter(user=request.user)[0].get_permissions()),
                   "header": "Журнал приходов/расходов", "operations": operations,
                   "operations_json": json.dumps(operations), "tree": json.dumps(tree), "goods": json.dumps(goods),
                   "goods_json": json.dumps(goods_json), "goods_inf": json.dumps(goods_inf), "counter": counter,
                   "units": json.dumps(units), 'stocks': Counter_stock.objects.filter(counter=counter),
                   "stockData": json.dumps(stocks), "counters": Counterparty.objects.all()})


def get_good_inf(request):
    if request.method == 'POST':
        if 'id' in request.POST:
            good = Goods.objects.get(pk=request.POST['id'])
            data = {}
            data['names'] = {}
            for n in Good_name.objects.filter(product=good):
                data['names'][str(n.pk)] = {'type': n.name_type, 'area': n.area, 'name': n.name}
            data['counter'] = good.producer.pk
            units = {}
            for u in Goods_unit.objects.filter(product=good):
                if u.applicable:
                    units[str(u.pk)] = {"name": u.unit.name, "value": u.coeff, "isBase": u.isBase}
            data["units"] = units
            data["model"] = good.model.pk
            props = {}
            for p in Goods_property.objects.filter(product=good):
                if p.applicable and p.visible:
                    props[str(p.pk)] = {"name": p.property.name, "type": p.property.prop_type, "editable": p.editable,
                                        "value": "", "choises": None}
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
        if 'model' in request.POST:
            model = Product_model.objects.get(pk=request.POST['model'])
            counter = Counterparty.objects.get(pk=request.POST['counter'])
            names = json.loads(request.POST['names'])
            units = json.loads(request.POST['units'])
            props = json.loads(request.POST['props'])
            good = Goods(model=model, producer=counter)
            good.save()
            for n in names:
                name = Good_name(product=good, name=names[n]['name'], area=names[n]['area'], name_type=names[n]['type'])
                name.save()
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


def save_demand(request):
    if request.method == 'POST':
        if 'date' in request.POST:
            group = User_group.objects.filter(user=request.user)[0].group
            consumer = Counterparty.objects.get(pk=request.POST['consumer'])
            provider = Counterparty.objects.get(pk=request.POST['provider'])
            if consumer == group:
                access = '1'
            else:
                if provider == group:
                    access = '2'
                else:
                    access = '0'
            donor = None
            acceptor = None
            vin = group.cur_vin
            if request.POST['donor'] != '' and request.POST['donor'] != '-1':
                donor = Stock.objects.get(pk=request.POST['donor'])
            if request.POST['acceptor'] != '' and request.POST['acceptor'] != '-1':
                acceptor = Stock.objects.get(pk=request.POST['acceptor'])
            date = datetime.datetime.strptime(request.POST['date'], "%Y-%m-%d").date()
            goods = json.loads(request.POST['goods'])
            matrix = Matrix(access=access, cause='0')
            matrix.save()
            demand = Demand(consumer=consumer, is_demand=json.loads(request.POST['is_demand']), vin=vin, matrix=matrix,
                            provider=provider, donor=donor, acceptor=acceptor, finish_date=date, user=request.user)
            demand.save()
            group.cur_vin = group.cur_vin + 1
            group.save()
            matrix.cause_id = demand.pk
            matrix.save()
            for g in goods:
                amount = float(goods[g]['num'].replace(',', '.'))
                t = goods[g]['product'][0]
                id = goods[g]['product'][2:]
                good = Goods.objects.get(pk=id)
                d = Demand_good(matrix=matrix, good=good, unit=Unit.objects.get(pk=goods[g]['unit']),
                                amount=amount, balance=amount, name=good.get_name(t),
                                article=good.get_article(t))
                d.save()
            if consumer == provider:
                status = '4'
                if demand.donor is not None:
                    ord_donor = Order(stock=demand.donor, matrix=demand.matrix, isDonor=True, status='0')
                    ord_donor.save()
                if demand.acceptor is not None:
                    ord_acceptor = Order(stock=demand.acceptor, matrix=demand.matrix, isDonor=False, status='0')
                    ord_acceptor.save()
                demand.matrix.access = status
                demand.matrix.save()
            return HttpResponse('ok')


def save_supply(request):
    if request.method == 'POST':
        if 'date' in request.POST:
            matrix = Matrix(access='0', cause='1')
            matrix.save()
            consumer = Counterparty.objects.get(pk=request.POST['consumer'])
            acceptor = Stock.objects.get(pk=request.POST['acceptor'])
            date = datetime.datetime.strptime(request.POST['date'], "%Y-%m-%d").date()
            p = Package(stock=acceptor, vin=acceptor.cur_vin, matrix=matrix, date=date)
            p.save()
            acceptor.cur_vin = acceptor.cur_vin + 1
            acceptor.save()
            ord = Order(stock=acceptor, matrix=matrix, isDonor=(request.POST['operation'] == '1'), status='2')
            ord.save()
            goods = json.loads(request.POST['goods'])
            for g in goods:
                amount = float(goods[g]['num'].replace(',', '.'))
                t = goods[g]['product'][0]
                id = goods[g]['product'][2:]
                good = Goods.objects.get(pk=id)
                s = Stock_operation(
                    package=p,
                    good=good,
                    operation=request.POST['operation'],
                    unit=Unit.objects.get(pk=goods[g]['unit']),
                    amount=amount
                )
                s.save()
                if request.POST['operation'] == '0':
                    if Stock_good.objects.filter(stock=acceptor, good=good).count() == 0:
                        rec = Stock_good(stock=acceptor, good=good,
                                         unit=Goods_unit.objects.filter(product=good, isBase=True)[0].unit, amount=
                                         Goods_unit.objects.filter(product=good,
                                                                   unit=Unit.objects.get(pk=goods[g]['unit']))[
                                             0].coeff * amount)
                        rec.save()
                    else:
                        rec = Stock_good.objects.filter(stock=acceptor, good=good)[0]
                        rec.amount = rec.amount + Goods_unit.objects.filter(product=good,
                                                                            unit=Unit.objects.get(pk=goods[g]['unit']))[
                            0].coeff * amount
                        rec.save()
                else:
                    if Stock_good.objects.filter(stock=acceptor, good=good).count() != 0:
                        rec = Stock_good.objects.filter(stock=acceptor, good=good)[0]
                        rec.amount = rec.amount - Goods_unit.objects.filter(product=good,
                                                                            unit=Unit.objects.get(pk=goods[g]['unit']))[
                            0].coeff * amount
                        rec.save()
            return HttpResponse('ok')


def save_planned_supply(request):
    if request.method == 'POST':
        if 'date' in request.POST:
            matrix = Matrix(access='4', cause='1')
            matrix.save()
            date = datetime.datetime.strptime(request.POST['date'], "%Y-%m-%d").date()
            group = User_group.objects.filter(user=request.user)[0].group
            vin = group.cur_vin
            group.cur_vin = group.cur_vin + 1
            group.save()
            if request.POST['operation'] == '0':
                consumer = Counterparty.objects.get(pk=request.POST['consumer'])
                provider = None
                acceptor = Stock.objects.get(pk=request.POST['acceptor'])
                donor = None
                is_demand = True
                release_date = None
                finish_date = date
            else:
                provider = Counterparty.objects.get(pk=request.POST['consumer'])
                consumer = None
                donor = Stock.objects.get(pk=request.POST['acceptor'])
                acceptor = None
                is_demand = False
                release_date = date
                finish_date = None
            new_demand = Demand(
                matrix=matrix,
                consumer=consumer,
                provider=provider,
                donor=donor,
                acceptor=acceptor,
                is_closed=False,
                release_date=release_date,
                finish_date=finish_date,
                is_edited=False,
                vin=vin,
                is_demand=is_demand,
                user=request.user
            )
            if 'cause' in request.POST:
                cause = request.POST['cause']
            else:
                cause = '0'
            new_demand.save()
            if new_demand.donor is not None:
                ord_donor = Order(stock=new_demand.donor, matrix=new_demand.matrix, cause=cause, isDonor=True,
                                  status='0')
                ord_donor.save()
            if new_demand.acceptor is not None:
                ord_acceptor = Order(stock=new_demand.acceptor, matrix=new_demand.matrix, cause=cause, isDonor=False,
                                     status='0')
                ord_acceptor.save()
            consumer = Counterparty.objects.get(pk=request.POST['consumer'])
            acceptor = Stock.objects.get(pk=request.POST['acceptor'])
            p = Package(stock=acceptor, vin=acceptor.cur_vin, matrix=matrix, date=date)
            p.save()
            acceptor.cur_vin = acceptor.cur_vin + 1
            acceptor.save()
            # ord = Order(stock=acceptor, matrix=matrix, isDonor=(request.POST['operation']=='1'), status='2')
            # ord.save()
            goods = json.loads(request.POST['goods'])
            for g in goods:
                amount = float(goods[g]['num'].replace(',', '.'))
                t = goods[g]['product'][0]
                id = goods[g]['product'][2:]
                g_m = Goods.objects.get(pk=id)
                good = Demand_good(matrix=matrix, good=g_m, article=g_m.get_article(t), name=g_m.get_name(t),
                                   unit=Unit.objects.get(pk=goods[g]['unit']), amount=amount,
                                   balance=amount)
                good.save()
            return HttpResponse('ok')


def send_inventory(request):
    if request.method == 'POST':
        if 'stock' in request.POST:
            stock = Stock.objects.get(pk=request.POST['stock'])
            goods = json.loads(request.POST['inventory_goods'])
            date = datetime.datetime.strptime(request.POST['date'], "%Y-%m-%d")
            inv = Inventory(stock=stock, date=date, is_finished=False)
            inv.save()
            for g in goods:
                t = g[0]
                id = g[2:]
                if t == 'g':
                    good = Goods.objects.get(pk=id)
                    if Inventory_good.objects.filter(inventory=inv, good=good).count() == 0:
                        i_g = Inventory_good(good=good, inventory=inv, amount=0)
                        i_g.save()
                elif t == 'm':
                    model = Product_model.objects.get(pk=id)
                    for good in Goods.objects.filter(model=model):
                        if Inventory_good.objects.filter(inventory=inv, good=good).count() == 0:
                            i_g = Inventory_good(good=good, inventory=inv, amount=0)
                            i_g.save()
                else:
                    save_group_inventory(id, inv)
            return HttpResponse('ok')


def save_group_inventory(group, inventory):
    for model in Product_model.objects.filter(group__pk=group):
        for good in Goods.objects.filter(model=model):
            if Inventory_good.objects.filter(inventory=inventory, good=good).count() == 0:
                i_g = Inventory_good(good=good, inventory=inventory, amount=0)
                i_g.save()
    for child_group in Model_group.objects.filter(parent=group):
        save_group_inventory(child_group.pk, inventory)


def save_inventory(request):
    if request.method == 'POST':
        if 'stock' in request.POST:
            stock = Stock.objects.get(pk=request.POST['stock'])
            goods = json.loads(request.POST['inventory_goods'])
            matrix = Matrix(access='0', cause='2')
            matrix.save()
            if 'type' in request.POST:
                date = datetime.datetime.strptime(request.POST['date'] + " " + request.POST['time'], "%d.%m.%Y %H:%M")
                inv = Inventory.objects.get(pk=request.POST['inventory'])
                inv.is_finished = True
                inv.save()
            else:
                date = datetime.datetime.strptime(request.POST['date'] + " " + request.POST['time'], "%Y-%m-%d %H:%M")
            p = Package(stock=stock, vin=stock.cur_vin, matrix=matrix, date=date)
            p.save()
            stock.cur_vin = stock.cur_vin + 1
            stock.save()
            for g in goods:
                cost = float(goods[g]['cost'].replace(',', '.'))
                amount = float(goods[g]['amount'].replace(',', '.'))
                good = Goods.objects.get(pk=g)
                last_value = 0
                if goods[g]['amount'] == '0':
                    if Stock_good.objects.filter(stock=stock, good=good).count() != 0:
                        last_value = Stock_good.objects.filter(stock=stock, good=good)[0].amount
                        Stock_good.objects.filter(stock=stock, good=good).delete()
                else:
                    if Stock_good.objects.filter(stock=stock, good=good).count() == 0:
                        s_g = Stock_good(stock=stock, good=good, unit=good.get_unit(), amount=amount,
                                         cost=cost * amount)
                        last_value = 0
                        s_g.save()
                    else:
                        s_g = Stock_good.objects.filter(stock=stock, good=good)[0]
                        last_value = s_g.amount
                        for h in Stock_operation.objects.filter(good=good, package__stock=stock, package__date__gte=date):
                            if h.operation == '0':
                                last_value = last_value - good.get_base_amount(h.amount, h.unit)
                                amount = amount + good.get_base_amount(h.amount, h.unit)
                            else:
                                if h.operation == '1':
                                    last_value = last_value + good.get_base_amount(h.amount, h.unit)
                                    amount = amount - good.get_base_amount(h.amount, h.unit)
                        s_g.amount = amount
                        s_g.cost = cost * amount
                        s_g.save()
                s = Stock_operation(
                    package=p,
                    good=good,
                    operation='2',
                    unit=good.get_unit(),
                    amount=amount,
                    cost=cost,
                    last_value=last_value
                )
                s.save()
            return HttpResponse('ok')


def edit_good(request):
    if request.method == 'POST':
        if 'id' in request.POST:
            good = Goods.objects.get(pk=request.POST['id'])
            counter = Counterparty.objects.get(pk=request.POST['counter'])
            names = json.loads(request.POST['names'])
            units = json.loads(request.POST['units'])
            properties = json.loads(request.POST['props'])
            good.producer = counter
            good.save()
            Good_name.objects.filter(product=good).delete()
            for n in names:
                name = Good_name(product=good, name=names[n]['name'], area=names[n]['area'], name_type=names[n]['type'])
                name.save()
            for u in units:
                unit = Goods_unit.objects.get(pk=u)
                unit.isBase = units[u]['isBase']
                unit.coeff = units[u]['coeff']
                unit.save()
            for p in properties:
                prop = Goods_property.objects.get(pk=p)
                if prop.property.prop_type == 0:
                    prop.property_num.number = properties[p]['value']
                    prop.property_num.save()
                else:
                    if prop.property.prop_type == 1:
                        prop.goods_string.text = properties[p]['value']
                        prop.goods_string.save()
                    else:
                        prop.goods_var.var = Property_var.objects.get(pk=properties[p]['value'])
                        prop.goods_var.save()
            return HttpResponse('ok')


def finish_shipment(request):
    if request.method == 'POST':
        if 'id' in request.POST:
            demand = Demand.objects.get(pk=request.POST['id'])
            ord = Order.objects.filter(matrix=demand.matrix, isDonor=True)[0]
            ord.status = '2'
            ord.save()
            goods = []
            m = Matrix(access='4', cause='0')
            m.save()
            for g in Demand_good.objects.filter(matrix=demand.matrix):
                if g.balance != 0:
                    good = Demand_good(matrix=m, good=g.good, name=g.name, unit=g.unit, amount=g.balance,
                                       balance=g.balance)
                    good.save()
                    goods.append(good)
                    g.amount = g.amount - g.balance
                    g.save()
                g.balance = g.amount
                g.save()
            if len(goods) == 0:
                m.delete()
            else:
                group = User_group.objects.filter(user=request.user)[0].group
                vin = group.cur_vin
                group.cur_vin = group.cur_vin + 1
                group.save()
                new_demand = Demand(
                    matrix=m,
                    consumer=demand.consumer,
                    provider=demand.provider,
                    donor=demand.donor,
                    acceptor=demand.acceptor,
                    is_closed=False,
                    finish_date=demand.finish_date,
                    is_edited=False,
                    vin=vin,
                    is_demand=demand.is_demand,
                    user=request.user
                )
                new_demand.save()
                if new_demand.donor is not None:
                    ord_donor = Order(stock=new_demand.donor, matrix=new_demand.matrix, isDonor=True, status='0')
                    ord_donor.save()
                if new_demand.acceptor is not None:
                    ord_acceptor = Order(stock=new_demand.acceptor, matrix=new_demand.matrix, isDonor=False, status='0')
                    ord_acceptor.save()
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
                    d = Model_property(model=model, prop=prop, visible=not props[p]['hidden'],
                                       editable=not props[p]['uneditable'], isDefault=props[p]['isDefault'])
                    d.save()
                for g_p in Goods_property.objects.filter(product__model=model, property=prop):
                    g_p.visible = d.visible
                    g_p.editable = d.editable
                    g_p.save()
                for g in Goods.objects.filter(model=model):
                    if Goods_property.objects.filter(product=g, property=prop).count() == 0:
                        if prop.prop_type == 0:
                            d = Property_num(product=g, property=prop, applicable=True,
                                             visible=not props[p]['hidden'], editable=not props[p]['uneditable'],
                                             number=0)
                            d.save()
                        else:
                            if prop.prop_type == 1:
                                d = Goods_string(product=g, property=prop, applicable=True,
                                                 visible=not props[p]['hidden'], editable=not props[p]['uneditable'],
                                                 text="")
                                d.save()
                            else:
                                var = Property_var.objects.filter(prop=prop).first()
                                d = Goods_var(product=g, property=prop, applicable=True,
                                              visible=not props[p]['hidden'], editable=not props[p]['uneditable'],
                                              var=var)
                                d.save()
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


def del_inventory(request):
    if request.method == 'POST':
        Inventory.objects.get(pk=request.POST['id']).delete()
        return HttpResponse("ok")


def del_stock(request):
    if request.method == 'POST':
        Stock.objects.get(pk=request.POST['id']).delete()
        return HttpResponse("ok")

def del_operation(request):
    if request.method == 'POST':
        d = Demand.objects.get(pk=request.POST['id'])
        ord = Order.objects.filter(matrix=d.matrix)[0]
        ord.status = '2'
        ord.save()
        return HttpResponse("ok")

def save_status(request):
    if request.method == 'POST':
        if 'id' in request.POST:
            d = Demand.objects.get(pk=request.POST['id'])
            status = request.POST['status']
            if status == '1':
                status = '4'
                if d.donor is not None:
                    ord_donor = Order(stock=d.donor, matrix=d.matrix, isDonor=True, status='0')
                    ord_donor.save()
                if d.acceptor is not None:
                    ord_acceptor = Order(stock=d.acceptor, matrix=d.matrix, isDonor=False, status='0')
                    ord_acceptor.save()
            else:
                if status == '2':
                    status = '3'
                else:
                    if status == '3':
                        d.is_closed = True
                        d.save()
            d.matrix.access = status
            d.matrix.save()
            return HttpResponse('ok')


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
