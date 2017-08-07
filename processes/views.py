# -*- coding: utf-8 -*-
from django.http.response import HttpResponse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from tables.models import Composition, Compl_comp, Compl_comp_comp, Characteristic_set_var, Comp_char_var, Comp_char_range, Comp_char_number, Set_var, Composition_char, Material, Components, Formula, Formula_component, Reactor, Tank
from .models import Batch_comp, Reactor_content, Tank_content, Model_list, Model_component, Kneading_char_number, Batch, Kneading_char_var, Loading_list, List_component, Kneading, State, State_log, Kneading_char
import json
from django.core import serializers
from django.utils import timezone
import datetime

def loading_lists(request):
    return render(request, "loading_lists.html", {"header": "Загрузочные листы", "location": "/processes/loading_lists/", "lists": Model_list.objects.all})

def storages(request):
    return render(request, "storages.html", {"header": "Хранилища", "location": "/processes/storages/", "reactors": Reactor_content.objects.all, "tanks": Tank_content.objects.all, "reactor": Reactor.objects.all, "tank": Tank.objects.all})

def mixing(request):
    return render(request, "process.html", {"header": "Процессы смешения", "location": "/processes/process/", "kneading": Kneading.objects.all})

def new_tech_comp(request):
    components = serializers.serialize("json", Components.objects.all())
    f_comp = serializers.serialize("json", Formula_component.objects.all())
    c_comps = serializers.serialize("json", Compl_comp.objects.all())
    models = serializers.serialize("json", Model_list.objects.all())
    m_comp = serializers.serialize("json", Model_component.objects.all())
    materials = serializers.serialize("json", Material.objects.all())
    formula = serializers.serialize("json", Formula.objects.filter(composition__isFinal = False))
    reactors = serializers.serialize("json", Reactor.objects.all())
    compl_comp_comps = serializers.serialize("json", Compl_comp_comp.objects.all())
    return render(request, "new_tech_comp.html", {
    "header": "Формирование технологической композиции",
    "location": "/processes/new_tech_comp/",
    "components": json.dumps(components),
    "materials": json.dumps(materials),
    "model_lists": json.dumps(models),
    "model_comps": json.dumps(m_comp),
    "materials2": Material.objects.all,
    "compl_comps": Compl_comp.objects.all,
    "compl_comps2": json.dumps(c_comps),
    "compl_comp_comps": json.dumps(compl_comp_comps),
    "f_c": json.dumps(f_comp),
    "f": json.dumps(formula),
    "reactors": Reactor.objects.all,
    "reactors2": json.dumps(reactors),
    "formulas": Formula.objects.filter(composition__isFinal = False)})

def list_detail(request, list_id):
    components = serializers.serialize("json", Components.objects.all())
    materials = serializers.serialize("json", Material.objects.all())
    f_comp = serializers.serialize("json", Formula_component.objects.all())
    formula = serializers.serialize("json", Formula.objects.all())
    compl_comp_comps = serializers.serialize("json", Compl_comp_comp.objects.all())
    if (list_id == '0'):
        return render(request, "loading_list.html",
            {"list": None,
            "components": json.dumps(components),
            "compositions": Composition.objects.all,
            "materials": json.dumps(materials),
            "materials2": Material.objects.all,
            "compl_comps": Compl_comp.objects.all,
            "compl_comp_comps": json.dumps(compl_comp_comps),
            "f_c": json.dumps(f_comp),
            "f": json.dumps(formula),
            "formulas": Formula.objects.all,
            "location": "/processes/loading_lists/",
            "header": "Загрузочные листы"
            })
    else:
        return render(request, "loading_list.html",
            {"list": get_object_or_404(Model_list, pk=list_id),
            "list_comps": Model_component.objects.filter(list=get_object_or_404(Model_list, pk=list_id)),
            "components": json.dumps(components),
            "materials": json.dumps(materials),
            "materials2": Material.objects.all,
            "compl_comps": Compl_comp.objects.all,
            "compl_comp_comps": json.dumps(compl_comp_comps),
            "formulas": Formula.objects.all,
            "f_c": json.dumps(f_comp),
            "f": json.dumps(formula),
            "compositions": Composition.objects.all,
            "location": "/processes/loading_lists/",
            "header": "Загрузочные листы"
            })

def del_list(request):
    del_var = request.POST.getlist('del_list')
    for d in del_var:
        del_obj = get_object_or_404(Model_list, pk=d)
        del_obj.delete()
    return redirect('loading_lists')


def planning(request):
    components = serializers.serialize("json", Components.objects.all())
    f_comp = serializers.serialize("json", Formula_component.objects.all())
    c_comps = serializers.serialize("json", Compl_comp.objects.all())
    models = serializers.serialize("json", Model_list.objects.all())
    m_comp = serializers.serialize("json", Model_component.objects.all())
    materials = serializers.serialize("json", Material.objects.all())
    formula = serializers.serialize("json", Formula.objects.all())
    reactors = serializers.serialize("json", Reactor.objects.all())
    compl_comp_comps = serializers.serialize("json", Compl_comp_comp.objects.all())
    return render(request, "planning.html",
        {"components": json.dumps(components),
        "materials": json.dumps(materials),
        "model_lists": json.dumps(models),
        "model_comps": json.dumps(m_comp),
        "materials2": Material.objects.all,
        "compl_comps": Compl_comp.objects.all,
        "compl_comps2": json.dumps(c_comps),
        "compl_comp_comps": json.dumps(compl_comp_comps),
        "f_c": json.dumps(f_comp),
        "f": json.dumps(formula),
        "reactors": Reactor.objects.all,
        "reactors2": json.dumps(reactors),
        "formulas": Formula.objects.all,
        "location": "/processes/planning/",
        "header": "Планирование"
        })

def save_list(request, list_id):
    list = Model_list()
    #сохранение загрузочного листа
    if 'formula' in request.POST:
        formula = get_object_or_404(Formula, pk=request.POST['formula'])
        list.formula = formula
        list.save()
        if 'json' in request.POST:
            table = request.POST['json']
            data = json.loads(table)
            for d in data:
                if d['Код']!='ВД01':
                    ammount=d['%']
                    if Material.objects.filter(code=d['Код']).count() == 0:
                        mat = Compl_comp.objects.filter(code=d['Код'])[0]
                        cmps = Model_component(list=list, compl=mat, ammount=ammount)
                    else:
                        mat = Material.objects.filter(code=d['Код'])[0]
                        cmps = Model_component(list=list, mat=mat, ammount=ammount)
                    cmps.save()
        return redirect('loading_lists')

def save_load_list(request, kneading_id):
    kneading = get_object_or_404(Kneading, pk=kneading_id)
    list = kneading.list
    if 'ammount' in request.POST:
        ammount = request.POST['ammount']
        list.ammount = ammount
    list.save()
    if 'json' in request.POST:
        List_component.objects.filter(list = list).delete()
        table = request.POST['json']
        data = json.loads(table)
        for d in data:
            if d['Код']!='ВД01':
                ammount=d["Количество, кг"]
                if Material.objects.filter(code=d['Код']).count() == 0:
                    mat = Compl_comp.objects.filter(code=d['Код'])[0]
                    cmps = List_component(list=list, compl=mat, ammount=ammount)
                else:
                    mat = Material.objects.filter(code=d['Код'])[0]
                    cmps = List_component(list=list, mat=mat, ammount=ammount)
                cmps.save()
        return redirect('kneading_detail', kneading_id = kneading_id)

def save_process(request):
    list = Loading_list()
    #сохранение загрузочного листа
    if 'ammount' in request.POST:
        ammount = request.POST['ammount']
        formula = get_object_or_404(Formula, pk=request.POST['formula'])
        list.ammount = ammount
        list.formula = formula
        list.save()
        if 'json' in request.POST:
            table = request.POST['json']
            data = json.loads(table)
            for d in data:
                if d['Код']!='ВД01':
                    ammount=d['%']
                    if Material.objects.filter(code=d['Код']).count() == 0:
                        mat = Compl_comp.objects.filter(code=d['Код'])[0]
                        cmps = List_component(list=list, compl=mat, ammount=ammount)
                    else:
                        mat = Material.objects.filter(code=d['Код'])[0]
                        cmps = List_component(list=list, mat=mat, ammount=ammount)
                    cmps.save()
        #сохранение процесса
        if 'start' in request.POST:
            kneading = Kneading()
            st_date = request.POST['start']
            end_date = request.POST['end']
            reactor = get_object_or_404(Reactor, pk=request.POST['reactor'])
            kneading.start_date = datetime.datetime.strptime(st_date, "%d/%m/%Y").date()
            kneading.finish_date = datetime.datetime.strptime(end_date, "%d/%m/%Y").date()
            kneading.list = list
            kneading.reactor = reactor
            kneading.save()
            st = State_log(kneading = kneading, state = get_object_or_404(State, pk=1))
            st.save()
        return redirect('mixing')

def save_tech_comp(request):
    list = Loading_list()
    #сохранение загрузочного листа
    if 'ammount' in request.POST:
        ammount = request.POST['ammount']
        formula = get_object_or_404(Formula, pk=request.POST['formula'])
        list.ammount = ammount
        list.formula = formula
        list.save()
        comp_amm = 0
        if 'json' in request.POST:
            table = request.POST['json']
            data = json.loads(table)
            for d in data:
                if d['Код']!='ВД01':
                    ammount=d['%']
                    comp_amm = comp_amm + float(ammount)
                    if Material.objects.filter(code=d['Код']).count() == 0:
                        mat = Compl_comp.objects.filter(code=d['Код'])[0]
                        cmps = List_component(list=list, compl=mat, ammount=ammount)
                    else:
                        mat = Material.objects.filter(code=d['Код'])[0]
                        cmps = List_component(list=list, mat=mat, ammount=ammount)
                    cmps.save()
        mat = Material.objects.filter(code="ВД01")[0]
        water_amm = float(list.ammount) - comp_amm
        cmps = List_component(list=list, mat=mat, ammount=water_amm)
        cmps.save()
        #сохранение процесса
        if 'reactor' in request.POST:
            kneading = Kneading()
            reactor = get_object_or_404(Reactor, pk=request.POST['reactor'])
            kneading.start_date = datetime.date.today()
            kneading.finish_date = datetime.date.today()
            kneading.list = list
            kneading.reactor = reactor
            kneading.save()
            st = State_log(kneading = kneading, state = get_object_or_404(State, pk=5))
            st.save()
        #Сохранение партии
        batch = Batch()
        batch.kneading = kneading
        batch.finish_date = datetime.date.today()
        batch.save()
        #Добавление в реактор
        reactor_content = Reactor_content.objects.filter(reactor = kneading.reactor)[0]
        reactor_content.content_type = 1
        reactor_content.amount = kneading.list.ammount
        reactor_content.batch = batch
        reactor_content.save()
        #Получение состава
        components = {}
        for c in Formula_component.objects.filter(formula = kneading.list.formula):
            components[c.mat.id] = {};
            components[c.mat.id]['code'] = c.mat.code
            components[c.mat.id]['name'] = c.mat.name
            components[c.mat.id]['amount'] = 0
            water = List_component.objects.filter(list=kneading.list, mat=get_object_or_404(Material, code='ВД01'))[0]
            components[water.mat.id] = {};
            components[water.mat.id]['code'] = water.mat.code
            components[water.mat.id]['name'] = water.mat.name
            components[water.mat.id]['amount'] = 0
        comp_amm = 0;
        for c in List_component.objects.filter(list = kneading.list):
            if c.compl is None:
                if c.mat.id in components:
                    components[c.mat.id]['amount'] = round(float(components[c.mat.id]['amount']) + c.ammount, 2)
                    comp_amm = comp_amm + c.ammount
            else:
                for c2 in Compl_comp_comp.objects.filter(compl = c.compl):
                    if c2.mat.id in components:
                        components[c2.mat.id]['amount'] = round(float(components[c2.mat.id]['amount']) + (c2.ammount / c.compl.ammount) * c.ammount, 2)
                        comp_amm = comp_amm + round((c2.ammount / c.compl.ammount) * c.ammount, 2)
        components[water.mat.id]['amount'] = round(float(components[water.mat.id]['amount']) + (float(kneading.list.ammount) - comp_amm), 2)
        for c in components:
            comp = Batch_comp(batch = batch, mat = Material.objects.filter(code = components[c]['code'])[0], ammount = components[c]['amount'])
            comp.save()
        return redirect('mixing')

def get_processes(request):
    if request.method == 'GET':
        p = {}
        for k in Kneading.objects.all():
            p[str(k.id)]={'start': k.start_date.strftime('%d.%m.%Y'), 'end': k.finish_date.strftime('%d.%m.%Y'), 'reactor': str(k.reactor), 'formula': k.list.formula.get_name(), 'amount': str(k.list.ammount), 'state': str(get_state_id(k))}
        json_data = json.dumps(p)
        #processes = serializers.serialize("json", p)
        return HttpResponse(json_data)

def pack(request):
    if request.method == 'POST':
        if request.POST['type'] == 'r':
            storage = get_object_or_404(Reactor_content, pk=request.POST['id'])
        else:
            storage = get_object_or_404(Tank_content, pk=request.POST['id'])
        storage.amount = storage.amount - float(request.POST['amm'])
        if storage.amount == 0:
            storage.content_type = 3
        storage.save()
        return HttpResponse('ok')

def drop(request):
    if request.method == 'POST':
        if request.POST['type'] == 'r':
            storage = get_object_or_404(Reactor_content, pk=request.POST['id'])
        else:
            storage = get_object_or_404(Tank_content, pk=request.POST['id'])
        storage.amount = 0
        storage.content_type = 3
        storage.save()
        return HttpResponse('ok')

def move(request):
    if request.method == 'POST':
        if request.POST['donor'][0] == 'r':
            donor = get_object_or_404(Reactor_content, reactor=request.POST['donor'][2:])
        else:
            donor = get_object_or_404(Tank_content, tank=request.POST['donor'][2:])
        if request.POST['acc'][0] == 'r':
            accepting = get_object_or_404(Reactor_content, reactor=request.POST['acc'][2:])
        else:
            accepting = get_object_or_404(Tank_content, tank=request.POST['acc'][2:])
        amm = float(request.POST['amm'])
        donor.amount = donor.amount - amm
        accepting.content_type = donor.content_type
        accepting.amount = accepting.amount + amm
        if donor.content_type == 1:
            accepting.batch = donor.batch
        else:
            accepting.kneading = donor.kneading
        if donor.amount == 0:
            donor.content_type = 3
        donor.save()
        accepting.save()
        return HttpResponse('ok')

def get_lists(request):
    if request.method == 'GET':
        p = {}
        for l in List_component.objects.all():
            k = Kneading.objects.filter(list = l.list)
            if k.count() != 0:
                m_name = l.mat.name
                m_code = l.mat.code
                p[str(l.id)]={'process': str(k[0].id), 'mat_code': m_code, 'mat_name': m_name, 'amount': str(l.ammount), 'loaded': int(l.loaded)}
        json_data = json.dumps(p)
        #processes = serializers.serialize("json", p)
        return HttpResponse(json_data)

def get_state_id(kneading):
    return State_log.objects.filter(kneading = kneading).last().state.id

def get_state(request):
    if request.method == 'POST':
        if 'id' in request.POST:
            log = State_log.objects.filter(kneading = get_object_or_404(Kneading, pk=request.POST['id'])).last()
            name = log.get_state()
            return HttpResponse(name)

def add_comp(request, kneading_id):
    if request.method == 'POST':
        if 'mat_id' in request.POST:
            if request.POST['type'] == 'compl':
                mat = Compl_comp.objects.filter(pk=request.POST['mat_id'])[0]
                mat.store_amount = mat.store_amount - float(request.POST['amm'])
                comp = List_component.objects.filter(list = get_object_or_404(Kneading, pk=kneading_id).list, compl=mat)[0]
                mat.save()
            else:
                mat = Material.objects.filter(pk=request.POST['mat_id'])[0]
                mat.ammount = mat.ammount - float(request.POST['amm'])
                comp = List_component.objects.filter(list = get_object_or_404(Kneading, pk=kneading_id).list, mat=mat)[0]
                mat.save()
            #comp = List_component.objects.filter(list = get_object_or_404(Kneading, pk=kneading_id).list, mat=get_object_or_404(Material, pk=request.POST['mat_id']))[0]
            comp.ammount = request.POST['amm']
            kneading = get_object_or_404(Kneading, pk=kneading_id)
            reactor_content = Reactor_content.objects.filter(reactor = kneading.reactor)[0]
            reactor_content.amount = kneading.list.ammount
            reactor_content.save()
            comp.loaded = True
            comp.save()
            return HttpResponse("ok")

def start_kneading(request, kneading_id):
    kneading = get_object_or_404(Kneading, pk=kneading_id)
    st = State_log(kneading = kneading, state = get_object_or_404(State, pk=2))
    st.save()
    components = serializers.serialize("json", Components.objects.all())
    l_comp = serializers.serialize("json", List_component.objects.filter(list = kneading.list))
    materials = serializers.serialize("json", Material.objects.all())
    formula = serializers.serialize("json", Formula.objects.all())
    return redirect('kneading_detail', kneading_id = kneading_id)
    #return render(request, 'started.html', {"components": json.dumps(components),
                                            #"materials": json.dumps(materials),
                                            #"l_c": json.dumps(l_comp),
                                            #"c_id": kneading.list.formula.composition.id,
                                            #"location": "/processes/process/",
                                            #"p": kneading})

def start_mixing(request, kneading_id):
    kneading = get_object_or_404(Kneading, pk=kneading_id)
    if 'water_amm' in request.POST:
         cmps = List_component(list=kneading.list, mat=get_object_or_404(Material, code='ВД01'), ammount=request.POST['water_amm'])
         cmps.save()
    st = State_log(kneading = kneading, state = get_object_or_404(State, pk=3))
    st.save()
    reactor_content = Reactor_content.objects.filter(reactor = kneading.reactor)[0]
    reactor_content.content_type = 2
    reactor_content.kneading = kneading
    reactor_content.save()
    components = serializers.serialize("json", Components.objects.all())
    l_comp = serializers.serialize("json", List_component.objects.filter(list = kneading.list))
    materials = serializers.serialize("json", Material.objects.all())
    formula = serializers.serialize("json", Formula.objects.all())
    return redirect('kneading_detail', kneading_id = kneading_id)


def start_testing(request, kneading_id):
    kneading = get_object_or_404(Kneading, pk=kneading_id)
    if 'list_amm' in request.POST:
         kneading.list.ammount = request.POST['list_amm']
         kneading.list.save()
    st = State_log(kneading = kneading, state = get_object_or_404(State, pk=4))
    st.save()
    return redirect('kneading_detail', kneading_id = kneading_id)

def stop_process(request, kneading_id):
    kneading = get_object_or_404(Kneading, pk=kneading_id)
    st = State_log(kneading = kneading, state = get_object_or_404(State, pk=6))
    st.save()
    return redirect('kneading_detail', kneading_id = kneading_id)


def finish_testing(request, kneading_id):
    kneading = get_object_or_404(Kneading, pk=kneading_id)
    st = State_log(kneading = kneading, state = get_object_or_404(State, pk=5))
    st.save()
    batch = Batch(kneading = kneading)
    batch.save()
    reactor_content = Reactor_content.objects.filter(reactor = kneading.reactor)[0]
    reactor_content.content_type = 1
    reactor_content.amount = kneading.list.ammount
    reactor_content.batch = batch
    reactor_content.save()
    #Получение состава
    components = {}
    for c in Formula_component.objects.filter(formula = kneading.list.formula):
        components[c.mat.id] = {};
        components[c.mat.id]['code'] = c.mat.code
        components[c.mat.id]['name'] = c.mat.name
        components[c.mat.id]['amount'] = 0
        water = List_component.objects.filter(list=kneading.list, mat=get_object_or_404(Material, code='ВД01'))[0]
        components[water.mat.id] = {};
        components[water.mat.id]['code'] = water.mat.code
        components[water.mat.id]['name'] = water.mat.name
        components[water.mat.id]['amount'] = 0
    comp_amm = 0;
    for c in List_component.objects.filter(list = kneading.list):
        if c.compl is None:
            if c.mat.id in components:
                components[c.mat.id]['amount'] = round(float(components[c.mat.id]['amount']) + c.ammount, 2)
                comp_amm = comp_amm + c.ammount
        else:
            for c2 in Compl_comp_comp.objects.filter(compl = c.compl):
                if c2.mat.id in components:
                    components[c2.mat.id]['amount'] = round(float(components[c2.mat.id]['amount']) + (c2.ammount / c.compl.ammount) * c.ammount, 2)
                    comp_amm = comp_amm + round((c2.ammount / c.compl.ammount) * c.ammount, 2)
    components[water.mat.id]['amount'] = round(float(components[water.mat.id]['amount']) + (float(kneading.list.ammount) - comp_amm), 2)
    for c in components:
        comp = Batch_comp(batch = batch, mat = Material.objects.filter(code = components[c]['code'])[0], ammount = components[c]['amount'])
        comp.save()
    return redirect('kneading_detail', kneading_id = kneading_id)

def kneading_detail(request, kneading_id):
    kneading = get_object_or_404(Kneading, pk=kneading_id)
    state_id = State_log.objects.filter(kneading = kneading).last().state.pk
    components = serializers.serialize("json", Components.objects.all())
    l_comp = serializers.serialize("json", List_component.objects.filter(list = kneading.list))
    materials = serializers.serialize("json", Material.objects.all())
    formula = serializers.serialize("json", Formula.objects.all())
    l_comp2 = List_component.objects.filter(list = kneading.list)
    #Добавить минимум максимум
    comps = {}
    for c in l_comp2:
        if c.compl is None:
            if Components.objects.filter(comp = c.list.formula.composition, mat = c.mat).count() == 0:
                min = 0 #костыль!!! добавить проверку на наличие всех компонентов в рецепте
                max = 0
            else:
                min = Components.objects.filter(comp = c.list.formula.composition, mat = c.mat)[0].min
                max = Components.objects.filter(comp = c.list.formula.composition, mat = c.mat)[0].max
            comps[str(c.id)]={'mat_code': c.mat.code, 'mat_name': c.mat.name, 'amount': str(c.ammount), 'loaded': int(c.loaded), 'min': min, 'max': max}
        else:
            comps[str(c.id)]={'mat_code': c.compl.code, 'mat_name': c.compl.name, 'amount': str(c.ammount), 'loaded': int(c.loaded), 'min': '-', 'max': '-'}
    load_list = json.dumps(comps)
    if state_id == 1:
        return render(request, 'waiting.html', {"components": json.dumps(components),
                                                "materials": json.dumps(materials),
                                                "l_c": json.dumps(l_comp),
                                                "c_id": kneading.list.formula.composition.id,
                                                "load_list": load_list,
                                                "location": "/processes/process/",
                                                "p": kneading})
    if state_id == 2:
        return render(request, 'started.html', {"components": json.dumps(components),
                                                "materials": json.dumps(materials),
                                                "l_c": json.dumps(l_comp),
                                                "c_id": kneading.list.formula.composition.id,
                                                "load_list": load_list,
                                                "location": "/processes/process/",
                                                "p": kneading})
    if state_id == 3:
        return render(request, 'mixing.html', {"components": json.dumps(components),
                                                "materials": json.dumps(materials),
                                                "comp": List_component.objects.filter(list=kneading.list),
                                                "l_c": json.dumps(l_comp),
                                                "load_list": load_list,
                                                "c_id": kneading.list.formula.composition.id,
                                                "location": "/processes/process/",
                                                "p": kneading})
    if state_id == 6:
        return render(request, 'stoped.html', {"components": json.dumps(components),
                                                "materials": json.dumps(materials),
                                                "comp": List_component.objects.filter(list=kneading.list),
                                                "l_c": json.dumps(l_comp),
                                                "load_list": load_list,
                                                "c_id": kneading.list.formula.composition.id,
                                                "location": "/processes/process/",
                                                "p": kneading})
    if state_id == 4:
        isTested = (Kneading_char.objects.filter(kneading = kneading).count() != 0)
        if isTested:
            chars = Kneading_char.objects.filter(kneading = kneading)
        else:
            chars = Composition_char.objects.filter(comp = kneading.list.formula.composition)
        return render(request, 'testing.html', {
                                                "chars": chars,
                                                "isTested": isTested,
                                                "isValid": kneading.isValid,
                                                "kneading_chars": Kneading_char.objects.filter(kneading = kneading),
                                                "location": "/processes/process/",
                                                "p": kneading})
    if state_id == 5:
        batch = Batch.objects.filter(kneading = kneading)[0]
        #Получение состава
        components = {}
        for c in Formula_component.objects.filter(formula = kneading.list.formula):
            components[c.mat.id] = {};
            components[c.mat.id]['code'] = c.mat.code
            components[c.mat.id]['name'] = c.mat.name
            components[c.mat.id]['amount'] = 0
            water = List_component.objects.filter(list=kneading.list, mat=get_object_or_404(Material, code='ВД01'))[0]
            components[water.mat.id] = {};
            components[water.mat.id]['code'] = water.mat.code
            components[water.mat.id]['name'] = water.mat.name
            components[water.mat.id]['amount'] = 0
        comp_amm = 0;
        for c in List_component.objects.filter(list = kneading.list):
            if c.compl is None:
                if c.mat.id in components:
                    components[c.mat.id]['amount'] = round(components[c.mat.id]['amount'] + c.ammount, 2)
                    comp_amm = comp_amm + c.ammount
            else:
                for c2 in Compl_comp_comp.objects.filter(compl = c.compl):
                    if c2.mat.id in components:
                        components[c2.mat.id]['amount'] = round(components[c2.mat.id]['amount'] + (c2.ammount / c.compl.ammount) * c.ammount, 2)
                        comp_amm = comp_amm + round((c2.ammount / c.compl.ammount) * c.ammount, 2)
        components[water.mat.id]['amount'] = round(components[water.mat.id]['amount'] + (kneading.list.ammount - comp_amm), 2)
        #Получение значений характеристик контроля качества
        chars = {}
        temp_chars = Kneading_char.objects.filter(kneading = kneading)
        i = 0
        for c in temp_chars:
            if c.characteristic.char_type.id != 3:
                try:
                    chars[i] = {'group' : c.characteristic.group.name, 'name': c.characteristic.name, 'value': c.kneading_char_number.number}
                except Kneading_char_number.DoesNotExist:
                    chars[i] = {}
            else:
                val = Kneading_char_var.objects.filter(kneading_char = c)[0].char_var.name
                chars[i] = {'group' : c.characteristic.group.name, 'name': c.characteristic.name, 'value': val}
            i = i+1
        return render(request, 'finished.html', {"comps": List_component.objects.filter(list = kneading.list),
                                                "chars": chars,
                                                "components": components,
                                                "location": "/processes/process/",
                                                "p": batch})

def get_checked_elems(request, composition_id):
    if request.method == 'POST':
        if 'char_id' in request.POST:
            char = get_object_or_404(Kneading_char, pk=request.POST['char_id'])
            data = {}
            vars = {}
            checked = {}
            all_var = Characteristic_set_var.objects.filter(char_set = char.characteristic)
            length = Characteristic_set_var.objects.filter(char_set = char.characteristic).count()
            for i in range(0, length):
                vars[str(all_var[i].char_var.id)] = all_var[i].char_var.name
            checked_var = Kneading_char_var.objects.filter(kneading_char = char)
            #length = Comp_char_var.objects.filter(comp_char = char).count()
            #for i in range(0, length):
            checked[str(checked_var[0].char_var.id)] = checked_var[0].char_var.name
            data['vars'] =  vars
            data['checked'] = checked
            json_data = json.dumps(data)
            return HttpResponse(json_data)

def save_kneading_char(request, kneading_id):
    kneading = get_object_or_404(Kneading, pk=kneading_id)
    Kneading_char.objects.filter(kneading = kneading).delete()
    chars = Composition_char.objects.filter(comp = kneading.list.formula.composition)
    isValid = True
    for char in chars:
        if (char.characteristic.char_type.id != 3):
            if str(char.characteristic.id) in request.POST:
                kneading_char = Kneading_char_number(kneading = kneading, characteristic = char.characteristic, number = request.POST[str(char.characteristic.id)])
                kneading_char.save()
                #Проверка на соответсвие показателям
                comp_char = Composition_char.objects.filter(comp = kneading.list.formula.composition, characteristic = char.characteristic)[0]
                if (char.characteristic.char_type.id == 1):
                    range = Comp_char_range.objects.filter(comp = kneading.list.formula.composition, characteristic = char.characteristic)[0]
                    isValid = isValid & ((float(kneading_char.number) <= float(range.sup)) & (float(kneading_char.number) >= float(range.inf)))
                if (char.characteristic.char_type.id == 2):
                    isValid = isValid & (kneading_char.number == comp_char.сomp_char_number.number)
        else:
            if (str(char.characteristic.id) + "'checked'") in request.POST:
                char_var = request.POST[str(char.characteristic.id) + "'checked'"]
                kneading_char = Kneading_char(kneading = kneading, characteristic = char.characteristic)
                kneading_char.save()
                set_var = get_object_or_404(Set_var, pk=char_var)
                kneading_char_var = Kneading_char_var(kneading_char = kneading_char, char_var = set_var)
                kneading_char_var.save()
                #Проверка на соответсвие показателям
                comp_char = Composition_char.objects.filter(comp = kneading.list.formula.composition, characteristic = char.characteristic)[0]
                isValid = isValid & (Comp_char_var.objects.filter(comp_char = comp_char, char_var = set_var).count() != 0)
    kneading.isTested = True
    kneading.isValid = isValid
    kneading.save()
    return redirect('kneading_detail', kneading_id = kneading_id)
