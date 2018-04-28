# -*- coding: utf-8 -*-
from django.http.response import HttpResponse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from tables.models import Product, Composition, Comp_prop_var, Compl_comp, Compl_comp_comp, Characteristic_set_var, Comp_char_var, Comp_char_range, Comp_char_number, Set_var, Composition_char, Material, Components, Formula, Formula_component, Reactor, Tank
from .models import Month_plan, Batch_comp, Reactor_content, Tank_content, Model_list, Model_component, Kneading_char_number, Batch, Kneading_char_var, Loading_list, List_component, Kneading, State, State_log, Kneading_char
from log.models import Movement_rec, Operation, Packing_divergence
import json
import math
from django.core import serializers
from django.utils import timezone
import datetime

def loading_lists(request):
    return render(request, "loading_lists.html", {"header": "Загрузочные листы", "location": "/processes/loading_lists/", "lists": Model_list.objects.all})

def storages(request):
    prods = {}
    for p in Product.objects.all():
        prods[str(p.pk)] = {'name': p.code + " " + p.get_name_for_table(), 'composition': p.production.composition.id, 'amount': p.production.get_boxing_amm()}
    return render(request, "storages.html", {"header": "Хранилища", "location": "/processes/storages/", "reactors": Reactor_content.objects.all, "tanks": Tank_content.objects.all, "reactor": Reactor.objects.all, "tank": Tank.objects.all, "products": json.dumps(prods)})

def mixing(request, kneading_id = -1):
    if kneading_id != -1:
        kneading = get_object_or_404(Kneading, pk=kneading_id)
    else:
        kneading = None
    batches = {}
    for k in Kneading.objects.filter(isFinished = False):
        log = State_log.objects.filter(kneading = k).last().state.pk
        if  log != 7 and log!=6:
            name = "П-" + str(int(k.batch_num)) + " " + str(k.list.formula)
            if name not in batches:
                batches[name] = name
    return render(request, "process.html", {"header": "Процессы смешения", "states": State.objects.all(), "location": "/processes/process/", "kneading": Kneading.objects.filter(isFinished = False), "new_kneading": kneading, "batches": batches})

def archive(request):
    kneadings = []
    for k in Kneading.objects.filter(isFinished = True, list__formula__composition__isFinal = True):
        log = State_log.objects.filter(kneading = k).last().state.pk
        if  log == 7:
            kneadings.append(k)
    return render(request, "archive.html", {"header": "Архив", "states": State.objects.all(), "location": "/processes/archive/", "kneading": kneadings})

def plan(request):
    return render(request, "plan.html", {"header": "План на месяц", "location": "/processes/plan/", "products": Product.objects.all(), "plans": json.dumps(serializers.serialize("json", Month_plan.objects.all()))})

def save_month_plan(request):
    Month_plan.objects.filter(month = request.POST["month"]).delete()
    for p in Product.objects.all():
        if str(p.pk) in request.POST and request.POST[str(p.pk)]!='':
            if (Month_plan.objects.filter(month = request.POST["month"], prod = p).count()==0):
                plan_obj= Month_plan(month = request.POST["month"], prod = p, num = request.POST[str(p.pk)])
                plan_obj.save()
            else:
                plan_obj = Month_plan.objects.filter(month = request.POST["month"], prod = p)[0]
                plan_obj.num = request.POST[str(p.pk)]
                plan_obj.save()
    if len(request.POST["month"]) == 7:
        return redirect('plan')
    else:
        return redirect('task')

def task(request):
    return render(request, "week_plan.html", {"header": "Задание на неделю", "location": "/processes/task/", "products": Product.objects.all(), "plans": json.dumps(serializers.serialize("json", Month_plan.objects.all()))})

def new_tech_comp(request):
    components = serializers.serialize("json", Components.objects.all())
    f_comp = serializers.serialize("json", Formula_component.objects.all())
    c_comps = serializers.serialize("json", Compl_comp.objects.all())
    models = serializers.serialize("json", Model_list.objects.all())
    m_comp = serializers.serialize("json", Model_component.objects.all())
    materials = serializers.serialize("json", Material.objects.all())
    batch_comps = serializers.serialize("json", Batch_comp.objects.all())
    formula = serializers.serialize("json", Formula.objects.filter(composition__isFinal = False))
    reactors = serializers.serialize("json", Reactor.objects.all())
    compl_comp_comps = serializers.serialize("json", Compl_comp_comp.objects.all())
    formula_names = {}
    for f in Formula.objects.all():
        formula_names[str(f.pk)] = str(f)
    batches = {}
    i=0
    for r in Reactor_content.objects.filter(content_type = "1"):
        batches[str(i)] = {"id": r.pk, "formula": str(r.batch.kneading.list.formula.pk), "name": ("Партия №" + str(r.batch.pk) + " " + str(r.reactor)), "type": "1", "amount": (r.amount - r.reserved)}
        i=i+1
    for t in Tank_content.objects.filter(content_type = "1"):
        batches[str(i)] = {"id": t.pk, "formula": str(t.batch.kneading.list.formula.pk), "name": ("Партия №" + str(t.batch.pk) + " " + str(t.tank)), "type": "2", "amount": (t.amount - t.reserved)}
        i=i+1
    for c in Compl_comp.objects.all():
        batches[str(i)] = {"id": c.pk, "formula": str(c.formula.pk), "name": c.name, "type": "3", "amount": (c.store_amount - c.reserved)}
        i=i+1
    return render(request, "new_tech_comp.html", {
    "header": "Формирование технологической композиции",
    "location": "/processes/new_tech_comp/",
    "components": json.dumps(components),
    "materials": json.dumps(materials),
    "model_lists": json.dumps(models),
    "model_comps": json.dumps(m_comp),
    "materials2": Material.objects.all,
    "compl_comps": Compl_comp.objects.all,
    "formula_names": json.dumps(formula_names),
    "compl_comps2": json.dumps(c_comps),
    "compl_comp_comps": json.dumps(compl_comp_comps),
    "f_c": json.dumps(f_comp),
    "f": json.dumps(formula),
    "reactors": Reactor.objects.all,
    "reactors2": json.dumps(reactors),
    "batches": json.dumps(batches),
    "formulas": Formula.objects.filter(composition__isFinal = False),
    "batch_comps": json.dumps(batch_comps)})

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
            "compl_comps": Formula.objects.filter(composition__isFinal = False),
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
            "compl_comps": Formula.objects.filter(composition__isFinal = False),
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

def print_month_plan(request, month):
    text_month = month[1:8]
    return render(request, "print_month_plan.html", {"products": Product.objects.all(), "plans": json.dumps(serializers.serialize("json", Month_plan.objects.all())), "plans2": Month_plan.objects.filter(month = text_month), "date": text_month})

def print_week_plan(request, month):
    text_month = month[1:11]
    return render(request, "print_week_plan.html", {"products": Product.objects.all(), "plans": json.dumps(serializers.serialize("json", Month_plan.objects.all())), "plans2": Month_plan.objects.filter(month = text_month), "date": text_month})

def print_lists(request, lists, kneading_id = None):
    list_ids = json.loads(lists)
    data = {}
    list_comps = {}
    for l in list_ids:
        amm = 0
        k = get_object_or_404(Kneading, pk=l)
        data[str(k.pk)] = {"id": k.pk, "batch_num": k.batch_num, "name": str(k), "start_date": k.start_date, "finish_date": k.finish_date, "reactor": k.reactor.pk, "amount": k.list.ammount, "list": k.list.pk, "code": str(k.list.formula.code), "isFinal": k.list.formula.composition.isFinal}
        for c in List_component.objects.filter(list = k.list):
            amm = amm + c.ammount
            if c.compl is None:
                if c.r_cont is None and c.t_cont is None and c.formula is None:
                    list_comps[str(c.pk)] = {"list": c.list.pk, "name": str(c.mat), "ammount": c.ammount, "min": c.min, "max": c.max}
                else:
                    if c.t_cont is not None:
                        list_comps[str(c.pk)] = {"list": c.list.pk, "name": str(c.t_cont.batch.kneading.list.formula), "ammount": c.ammount, "min": c.min, "max": c.max}
                    else:
                        if c.r_cont is not None:
                            list_comps[str(c.pk)] = {"list": c.list.pk, "name": str(c.r_cont.batch.kneading.list.formula), "ammount": c.ammount, "min": c.min, "max": c.max}
                        else:
                            list_comps[str(c.pk)] = {"list": c.list.pk, "name": str(c.formula), "ammount": c.ammount, "min": c.min, "max": c.max}
            else:
                list_comps[str(c.pk)] = {"list": c.list.pk, "name": str(c.compl.formula), "ammount": c.ammount, "min": c.min, "max": c.max}
        water = Material.objects.filter(code = "ВД01")[0]
        if round(k.list.ammount - amm, 2)!=0:
            list_comps[str(water.pk) + str(k.id)] = {"list": c.list.pk, "name": str(water), "ammount": math.fabs(k.list.ammount - amm), "min": None, "max": None}

    return render(request, "print_lists.html", {"kneading": data, "comps": list_comps})

def del_process(request, kneading_id = None):
    del_var = request.POST.getlist('del_list')
    for d in del_var:
        del_obj = get_object_or_404(Kneading, pk=d)
        for r in Reactor_content.objects.filter(kneading = del_obj):
            r.kneading = None
            r.save()
        for t in Tank_content.objects.filter(kneading = del_obj):
            t.kneading = None
            t.save()
        del_obj.isFinished = True
        del_obj.save()
    return redirect('mixing')


def planning(request):
    components = serializers.serialize("json", Components.objects.all())
    f_comp = serializers.serialize("json", Formula_component.objects.all())
    c_comps = serializers.serialize("json", Compl_comp.objects.all())
    models = serializers.serialize("json", Model_list.objects.all())
    m_comp = serializers.serialize("json", Model_component.objects.all())
    materials = serializers.serialize("json", Material.objects.all())
    formula = serializers.serialize("json", Formula.objects.all())
    reactors = serializers.serialize("json", Reactor.objects.all())
    batch_comps = serializers.serialize("json", Batch_comp.objects.all())
    formula_names = {}
    for f in Formula.objects.all():
        formula_names[str(f.pk)] = str(f)
    batches = {}
    i=0
    for r in Reactor_content.objects.filter(content_type = "1"):
        batches[str(i)] = {"id": r.pk, "formula": str(r.batch.kneading.list.formula.pk), "batch": r.batch.pk, "name": ("Партия №" + str(r.batch.pk) + " " + str(r.reactor)), "type": "1", "amount": (r.amount - r.reserved)}
        i=i+1
    for t in Tank_content.objects.filter(content_type = "1"):
        batches[str(i)] = {"id": t.pk, "formula": str(t.batch.kneading.list.formula.pk), "batch": t.batch.pk, "name": ("Партия №" + str(t.batch.pk) + " " + str(t.tank)), "type": "2", "amount": (t.amount - t.reserved)}
        i=i+1
    for c in Compl_comp.objects.all():
        batches[str(i)] = {"id": c.pk, "formula": str(c.formula.pk), "name": c.name, "type": "3", "amount": (c.store_amount - c.reserved)}
        i=i+1

    compl_comp_comps = serializers.serialize("json", Compl_comp_comp.objects.all())
    return render(request, "planning.html",
        {"components": json.dumps(components),
        "materials": json.dumps(materials),
        "model_lists": json.dumps(models),
        "model_comps": json.dumps(m_comp),
        "materials2": Material.objects.all,
        "compl_comps": Formula.objects.filter(composition__isFinal = False),
        "compl_comps2": json.dumps(c_comps),
        "compl_comp_comps": json.dumps(compl_comp_comps),
        "f_c": json.dumps(f_comp),
        "f": json.dumps(formula),
        "formula_names": json.dumps(formula_names),
        "reactors": Reactor.objects.all,
        "reactors2": json.dumps(reactors),
        "formulas": Formula.objects.all,
        "location": "/processes/planning/",
        "header": "Планирование",
        "batches": json.dumps(batches),
        "batch_comps": json.dumps(batch_comps)
        })

def new_associated_process(request):
    components = serializers.serialize("json", Components.objects.all())
    f_comp = serializers.serialize("json", Formula_component.objects.all())
    c_comps = serializers.serialize("json", Compl_comp.objects.all())
    models = serializers.serialize("json", Model_list.objects.all())
    m_comp = serializers.serialize("json", Model_component.objects.all())
    materials = serializers.serialize("json", Material.objects.all())
    formula = serializers.serialize("json", Formula.objects.all())
    reactors = serializers.serialize("json", Reactor.objects.all())
    list_comps = {}
    processes = {}
    for k in Kneading.objects.filter(isFinished = False).order_by("-pk"):
        log = State_log.objects.filter(kneading = k).last().state.pk
        if  log == 1 or log == 2:
            name = "П-" + str(int(k.batch_num)) + " " + str(k.list.formula)
            if name not in processes:
                processes[name] = {"id": k.pk, "batch_num": k.batch_num, "name": str(k), "start_date": str(k.start_date), "finish_date": str(k.finish_date), "reactor": k.reactor.pk, "amount": k.list.ammount, "formula": k.list.formula.pk, "list": k.list.pk}
                for c in List_component.objects.filter(list = k.list):
                    if c.compl is None:
                        if c.r_cont is None and c.t_cont is None and c.formula is None:
                            list_comps[str(c.pk)] = {"list": c.list.pk, "mat": c.mat.pk, "ammount": c.ammount}
                        else:
                            if c.t_cont is not None:
                                list_comps[str(c.pk)] = {"list": c.list.pk, "formula": c.t_cont.batch.kneading.list.formula.pk, "ammount": c.ammount}
                            else:
                                if c.r_cont is None:
                                    list_comps[str(c.pk)] = {"list": c.list.pk, "formula": c.formula.pk, "ammount": c.ammount}
                                else:
                                    r_id = c.pk
                                    list_comps[str(c.pk)] = {"list": c.list.pk, "formula": c.r_cont.batch.kneading.list.formula.pk, "ammount": c.ammount}
                    else:
                        list_comps[str(c.pk)] = {"list": c.list.pk, "formula": c.compl.formula.pk, "ammount": c.ammount}
    batch_comps = serializers.serialize("json", Batch_comp.objects.all())
    formula_names = {}
    for f in Formula.objects.all():
        formula_names[str(f.pk)] = str(f)
    batches = {}
    i=0
    for r in Reactor_content.objects.filter(content_type = "1"):
        batches[str(i)] = {"id": r.pk, "formula": str(r.batch.kneading.list.formula.pk), "batch": r.batch.pk, "name": ("Партия №" + str(r.batch.pk) + " " + str(r.reactor)), "type": "1", "amount": (r.amount - r.reserved)}
        i=i+1
    for t in Tank_content.objects.filter(content_type = "1"):
        batches[str(i)] = {"id": t.pk, "formula": str(t.batch.kneading.list.formula.pk), "batch": t.batch.pk, "name": ("Партия №" + str(t.batch.pk) + " " + str(t.tank)), "type": "2", "amount": (t.amount - t.reserved)}
        i=i+1
    for c in Compl_comp.objects.all():
        batches[str(i)] = {"id": c.pk, "formula": str(c.formula.pk), "name": c.name, "type": "3", "amount": (c.store_amount - c.reserved)}
        i=i+1
    compl_comp_comps = serializers.serialize("json", Compl_comp_comp.objects.all())
    return render(request, "associated_process.html",
        {"components": json.dumps(components),
        "materials": json.dumps(materials),
        "model_lists": json.dumps(models),
        "model_comps": json.dumps(m_comp),
        "materials2": Material.objects.all,
        "compl_comps": Formula.objects.filter(composition__isFinal = False),
        "compl_comps2": json.dumps(c_comps),
        "compl_comp_comps": json.dumps(compl_comp_comps),
        "f_c": json.dumps(f_comp),
        "f": json.dumps(formula),
        "formula_names": json.dumps(formula_names),
        "processes": processes,
        "processes2": json.dumps(processes),
        "reactors": Reactor.objects.all,
        "reactors2": json.dumps(reactors),
        "formulas": Formula.objects.all,
        "list_comps": json.dumps(list_comps),
        "location": "/processes/new_associated_process/",
        "header": "Планирование",
        "batches": json.dumps(batches),
        "batch_comps": json.dumps(batch_comps)
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
                    id = ammount.split("_")[0]
                    ammount = ammount.split("_")[1]
                    if Material.objects.filter(code=d['Код']).count() == 0:
                        mat = Formula.objects.filter(id=id)[0]
                        cmps = Model_component(list=list, formula=mat, ammount=ammount)
                    else:
                        mat = Material.objects.filter(id=id)[0]
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
        for c in List_component.objects.filter(list = list):
            if c.compl is None:
                if c.r_cont is None and c.t_cont is None and c.formula is None:
                    c.mat.reserved = c.mat.reserved - c.ammount
                else:
                    if c.r_cont is None and c.formula is None:
                        c.t_cont.reserved = c.t_cont.reserved - c.ammount
                    else:
                        if c.formula is None:
                            c.r_cont.reserved = c.r_cont.reserved - c.ammount
            else:
                c.compl.reserved = c.compl.reserved - c.ammount
        List_component.objects.filter(list = list).delete()
        table = request.POST['json']
        data = json.loads(table)
        for d in data:
            if d['Код']!='ВД01':
                ammount=d['%']
                t = ammount[0]
                id = ammount.split("_")[1]
                min = ammount.split("_")[3]
                max = ammount.split("_")[4]
                ammount = ammount.split("_")[2]
                if min == "":
                    min = None
                else:
                    min = float(min)
                if max == "":
                    max = None
                else:
                    max = float(max)
                if t == "1":
                    mat = Reactor_content.objects.filter(id = id)[0]
                    mat.reserved = mat.reserved + float(ammount)
                    mat.save()
                    cmps = List_component(list=list, r_cont=mat, min = min, max = max, ammount=ammount)
                    cmps.save()
                if t == "2":
                    mat = Tank_content.objects.filter(id = id)[0]
                    mat.reserved = mat.reserved + float(ammount)
                    mat.save()
                    cmps = List_component(list=list, t_cont=mat, min = min, max = max, ammount=ammount)
                    cmps.save()
                if t == "3":
                    mat = Compl_comp.objects.filter(id = id)[0]
                    mat.reserved = mat.reserved + float(ammount)
                    mat.save()
                    cmps = List_component(list=list, compl=mat, min = min, max = max, ammount=ammount)
                    cmps.save()
                if t == "4":
                    mat = Material.objects.filter(id = id)[0]
                    mat.reserved = mat.reserved + float(ammount)
                    mat.save()
                    cmps = List_component(list=list, mat=mat, min = min, max = max, ammount=ammount)
                    cmps.save()
                if t == "5":
                    mat = Formula.objects.filter(id = id)[0]
                    cmps = List_component(list=list, formula=mat, min = min, max = max, ammount=ammount)
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
                        t = ammount[0]
                        id = ammount.split("_")[1]
                        ammount = ammount.split("_")[2]
                        if t == "1":
                            mat = get_object_or_404(Reactor_content, pk = id)
                            mat.reserved = mat.reserved + float(ammount)
                            mat.save()
                            cmps = List_component(list=list, r_cont=mat, ammount=ammount)
                        else:
                            if t == "2":
                                mat = get_object_or_404(Tank_content, pk = id)
                                mat.reserved = mat.reserved + float(ammount)
                                mat.save()
                                cmps = List_component(list=list, t_cont=mat, ammount=ammount)
                            else:
                                if t == "3":
                                    mat = get_object_or_404(Compl_comp, pk = id)
                                    mat.reserved = mat.reserved + float(ammount)
                                    mat.save()
                                    cmps = List_component(list=list, compl=mat, ammount=ammount)
                                else:
                                    mat = get_object_or_404(Formula, pk = id)
                                    cmps = List_component(list=list, formula=mat, ammount=ammount)
                    else:
                        mat = Material.objects.filter(code=d['Код'])[0]
                        mat.reserved = mat.reserved + float(ammount)
                        mat.save()
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
            if 'kneading' in request.POST:
                k = get_object_or_404(Kneading, pk=request.POST['kneading'])
                kneading.batch_num = k.batch_num
            else:
                kneading.batch_num = formula.composition.cur_batch
                formula.composition.cur_batch = formula.composition.cur_batch + 1
                formula.composition.save()
            kneading.reactor = reactor
            kneading.save()
            st = State_log(kneading = kneading, state = get_object_or_404(State, pk=1))
            st.save()
        return redirect('mixing', kneading_id = kneading.id)

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
                        mat.store_amount = mat.store_amount - float(ammount)
                        mat.save()
                        cmps = List_component(list=list, compl=mat, ammount=ammount)
                    else:
                        mat = Material.objects.filter(code=d['Код'])[0]
                        mat.ammount = mat.ammount - float(ammount)
                        mat.save()
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
            kneading.batch_num = formula.composition.cur_batch
            formula.composition.cur_batch = formula.composition.cur_batch + 1
            formula.composition.save()
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
            comp = Batch_comp(batch = batch, mat = Material.objects.filter(code = components[c]['code'])[0], ammount = ((components[c]['amount']/float(list.ammount))*100))
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
        div = Packing_divergence()
        if request.POST['type'] == 'r':
            storage = get_object_or_404(Reactor_content, pk=request.POST['id'])
            div.reactor = storage.reactor
        else:
            storage = get_object_or_404(Tank_content, pk=request.POST['id'])
            div.tank = storage.tank
        div.prod_num = request.POST['num']
        div.start_amm = storage.amount
        div.pack_amm = request.POST['amm']
        storage.amount = storage.amount - float(request.POST['amm'])
        prod = get_object_or_404(Product, pk=request.POST['pr_id'])
        div.product = prod
        div.batch = storage.batch
        rec = Movement_rec(batch = storage.batch, product = prod, amount = float(request.POST['num']), operation = Operation.objects.filter(id = 1)[0])
        rec.save()
        div.save()
        if storage.amount == 0:
            storage.content_type = 3
            storage.batch = None
            storage.kneading = None
        storage.save()
        return HttpResponse('ok')

def drop(request):
    if request.method == 'POST':
        if request.POST['type'] == 'r':
            storage = get_object_or_404(Reactor_content, pk=request.POST['id'])
        else:
            storage = get_object_or_404(Tank_content, pk=request.POST['id'])
        check_dependencies(storage, request.POST['type'])
        storage.amount = 0
        storage.reserved = 0
        storage.content_type = 3
        storage.batch = None
        storage.kneading = None
        storage.save()
        return HttpResponse('ok')

def edit_amm(request):
    if request.method == 'POST':
        id = request.POST['id'].split("-")[1]
        if request.POST['id'][0] == 'r':
            storage = get_object_or_404(Reactor_content, pk=id)
        else:
            storage = get_object_or_404(Tank_content, pk=id)
        amm = request.POST['amm']
        storage.amount = amm
        storage.save()
        return HttpResponse(amm)

def check_dependencies(storage, t):
    if t == 'r':
        for k in Kneading.objects.all():
            log = State_log.objects.filter(kneading = k).last().state.pk
            if  log == 1 or log == 2 or log == 5 or log == 7:
                if List_component.objects.filter(list = k.list, r_cont = storage).count() != 0:
                    comp = List_component.objects.filter(list = k.list, r_cont = storage)[0]
                    comp.formula = comp.r_cont.batch.kneading.list.formula
                    comp.batch = None
                    comp.r_cont = None
                    comp.save()
    else:
        for k in Kneading.objects.all():
            log = State_log.objects.filter(kneading = k).last().state.pk
            if  log == 1 or log == 2 or log == 5 or log == 7:
                if List_component.objects.filter(list = k.list, t_cont = storage).count() != 0:
                    comp = List_component.objects.filter(list = k.list, t_cont = storage)[0]
                    comp.formula = comp.t_cont.batch.kneading.list.formula
                    comp.batch = None
                    comp.t_cont = None
                    comp.save()


def move(request):
    loses = 1
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

        if donor.content_type == 1:
            if accepting.content_type == 3:
                accepting.batch = donor.batch
            else:
                if amm > accepting.amount:
                    accepting.batch.kneading.batch_num = donor.batch.kneading.batch_num
                    accepting.batch.kneading.save()
                for m in Batch_comp.objects.filter(batch = accepting.batch):
                    comp = Batch_comp.objects.filter(batch = donor.batch, mat = m.mat)[0]
                    m.ammount = ((m.ammount*accepting.batch.kneading.list.ammount/100 + comp.ammount * donor.batch.kneading.list.ammount/100)/(accepting.batch.kneading.list.ammount + donor.batch.kneading.list.ammount))*100
                    m.save()
        else:
            accepting.kneading = donor.kneading
        if amm / loses > donor.amount:
            temp_amm = donor.amount
            donor.amount = 0
            accepting.content_type = donor.content_type
            accepting.amount = accepting.amount + temp_amm*loses
        else:
            donor.amount = donor.amount - amm / loses
            accepting.content_type = donor.content_type
            accepting.amount = accepting.amount + amm
        if donor.reserved > donor.amount:
            donor.reserved = 0
            check_dependencies(donor, request.POST['donor'][0])
        if donor.amount <= 0.01:
            donor.amount = 0
            donor.reserved = 0
            check_dependencies(donor, request.POST['donor'][0])
            donor.batch = None
            donor.kneading = None
            donor.content_type = 3
        donor.save()
        accepting.save()
        return HttpResponse('ok')

def move_batch(request, kneading_id):
    loses = 1
    if request.method == 'POST':
        if request.POST['donor'][0] == 'r':
            donor = get_object_or_404(Reactor_content, pk=request.POST['donor'][2:])
        else:
            donor = get_object_or_404(Tank_content, pk=request.POST['donor'][2:])
        if request.POST['acc'][0] == 'r':
            accepting = get_object_or_404(Reactor_content, pk=request.POST['acc'][2:])
        else:
            accepting = get_object_or_404(Tank_content, pk=request.POST['acc'][2:])
        amm = float(request.POST['amm'])
        if accepting.content_type == 3:
            accepting.batch = donor.batch
        else:
            if amm > accepting.amount:
                accepting.batch.kneading.batch_num = donor.batch.kneading.batch_num
                accepting.batch.kneading.save()
            for m in Batch_comp.objects.filter(batch = accepting.batch):
                comp = Batch_comp.objects.filter(batch = donor.batch, mat = m.mat)[0]
                m.ammount = ((m.ammount*accepting.batch.kneading.list.ammount/100 + comp.ammount * donor.batch.kneading.list.ammount/100)/(accepting.batch.kneading.list.ammount + donor.batch.kneading.list.ammount))*100
                m.save()
        if amm / loses > donor.amount:
            temp_amm = donor.amount
            donor.amount = 0
            accepting.content_type = donor.content_type
            accepting.amount = accepting.amount + temp_amm*loses
        else:
            donor.amount = donor.amount - amm / loses
            accepting.content_type = donor.content_type
            accepting.amount = accepting.amount + amm
        if donor.reserved > donor.amount:
            donor.reserved = 0
            check_dependencies(donor, request.POST['donor'][0])
        if donor.amount <= 0.01:
            donor.amount = 0
            donor.reserved = 0
            check_dependencies(donor, request.POST['donor'][0])
            donor.batch = None
            donor.kneading = None
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

def get_state(request, kneading_id = None):
    if request.method == 'POST':
        if 'id' in request.POST:
            log = State_log.objects.filter(kneading = get_object_or_404(Kneading, pk=request.POST['id'])).last()
            name = log.get_state()
            return HttpResponse(name)

def check_is_empty(request):
    if request.method == 'POST':
        if 'id' in request.POST:
            reactor = Reactor_content.objects.filter(reactor = get_object_or_404(Reactor, pk=request.POST['id']))[0]
            if reactor.content_type == 3:
                res = "empty"
            else:
                res = "hasContent"
            return HttpResponse(res)

def check_is_empty2(request, kneading_id):
    if request.method == 'POST':
        if 'id' in request.POST:
            reactor = Reactor_content.objects.filter(reactor = get_object_or_404(Reactor, pk=request.POST['id']))[0]
            if reactor.content_type == 3:
                res = "empty"
            else:
                res = str(reactor.get_formula_id()) + "_" + str(reactor.amount)
            return HttpResponse(res)

def save_date(request, kneading_id):
    kneading = get_object_or_404(Kneading, pk=kneading_id)
    if request.method == 'POST':
        if 't' in request.POST:
            if request.POST['t'] == "start":
                kneading.start_date = datetime.datetime.strptime(request.POST['date'], "%d/%m/%Y").date()
            else:
                kneading.finish_date = datetime.datetime.strptime(request.POST['date'], "%d/%m/%Y").date()
    kneading.save()
    return HttpResponse("ok")

def add_comp(request, kneading_id):
    res = "ok"
    loses = 1
    op = request.POST['op']
    if request.method == 'POST':
        if 'mat_id' in request.POST:
            if request.POST['type'] == 'compl':
                mat = Compl_comp.objects.filter(pk=request.POST['mat_id'])[0]
                if op == "edit" or op == "add":
                    comp = List_component.objects.filter(list = get_object_or_404(Kneading, pk=kneading_id).list, compl=mat)[0]
                    if mat.store_amount + comp.ammount < float(request.POST['amm']):
                        res = str(mat.store_amount + comp.ammount)
                    else:
                        mat.store_amount = mat.store_amount + comp.ammount - float(request.POST['amm'])
                        mat.reserved = mat.reserved - float(request.POST['amm'])
                        mat.save()
                else:
                    if mat.store_amount < float(request.POST['amm']):
                        res = str(mat.store_amount)
                    else:
                        mat.store_amount = mat.store_amount - float(request.POST['amm'])
                        mat.reserved = mat.reserved - float(request.POST['amm'])
                        comp = List_component.objects.filter(list = get_object_or_404(Kneading, pk=kneading_id).list, compl=mat)[0]
                        mat.save()
            else:
                if request.POST['type'] == 'tank':
                        content = Tank_content.objects.filter(pk = request.POST['mat_id'])[0]
                        if op == "edit" or op == "add":
                            comp = List_component.objects.filter(list = get_object_or_404(Kneading, pk=kneading_id).list, t_cont=content)[0]
                            if content.amount + 1 + comp.ammount < float(request.POST['amm']):
                                res = str(content.amount + comp.ammount)
                            else:
                                content.amount = content.amount + comp.ammount - float(request.POST['amm'])/loses
                                content.reserved = content.reserved - float(request.POST['amm'])/loses
                                if content.reserved > content.amount:
                                    content.reserved = 0
                                    check_dependencies(content, 't')
                                content.save()
                        else:
                            if content.amount+1 < float(request.POST['amm']):
                                res = str(content.amount)
                            else:
                                content.amount = content.amount - float(request.POST['amm'])/loses
                                content.reserved = content.reserved - float(request.POST['amm'])/loses
                                if content.reserved > content.amount:
                                    content.reserved = 0
                                    check_dependencies(content, 't')
                                comp = List_component.objects.filter(list = get_object_or_404(Kneading, pk=kneading_id).list, t_cont=content)[0]
                                content.save()
                else:
                    if request.POST['type'] == 'reactor':
                        content = Reactor_content.objects.filter(pk = request.POST['mat_id'])[0]
                        if op == "edit" or op == "add":
                            comp = List_component.objects.filter(list = get_object_or_404(Kneading, pk=kneading_id).list, r_cont=content)[0]
                            if content.amount + 1 + comp.ammount < float(request.POST['amm']):
                                res = str(content.amount + comp.ammount)
                            else:
                                content.amount = content.amount + comp.ammount - float(request.POST['amm'])/loses
                                content.reserved = content.reserved - float(request.POST['amm'])/loses
                                if content.reserved > content.amount:
                                    content.reserved = 0
                                    check_dependencies(content, 'r')
                                content.save()
                        else:
                            if content.amount+1 < float(request.POST['amm']):
                                res = str(content.amount)
                            else:
                                content.amount = content.amount - float(request.POST['amm'])/loses
                                content.reserved = content.reserved - float(request.POST['amm'])/loses
                                if content.reserved > content.amount:
                                    content.reserved = 0
                                    check_dependencies(content, 'r')
                                comp = List_component.objects.filter(list = get_object_or_404(Kneading, pk=kneading_id).list, r_cont=content)[0]
                                content.save()
                    else:
                        mat = Material.objects.filter(pk=request.POST['mat_id'])[0]
                        if op == "edit" or op == "add":
                            comp = List_component.objects.filter(list = get_object_or_404(Kneading, pk=kneading_id).list, mat=mat)[0]
                            if mat.ammount + comp.ammount < float(request.POST['amm']):
                                res = str(mat.ammount + comp.ammount)
                            else:
                                mat.ammount = mat.ammount + comp.ammount - float(request.POST['amm'])
                                mat.reserved = mat.reserved - float(request.POST['amm'])
                                comp = List_component.objects.filter(list = get_object_or_404(Kneading, pk=kneading_id).list, mat=mat)[0]
                                mat.save()
                        else:
                            if mat.ammount < float(request.POST['amm']):
                                res = str(mat.ammount)
                            else:
                                mat.ammount = mat.ammount - float(request.POST['amm'])
                                mat.reserved = mat.reserved - float(request.POST['amm'])
                                comp = List_component.objects.filter(list = get_object_or_404(Kneading, pk=kneading_id).list, mat=mat)[0]
                                mat.save()
                #comp = List_component.objects.filter(list = get_object_or_404(Kneading, pk=kneading_id).list, mat=get_object_or_404(Material, pk=request.POST['mat_id']))[0]
            if res == "ok":
                comp.ammount = request.POST['amm']
                kneading = get_object_or_404(Kneading, pk=kneading_id)
                reactor_content = Reactor_content.objects.filter(reactor = kneading.reactor)[0]
                reactor_content.amount = kneading.list.ammount
                reactor_content.save()
                comp.loaded = True
                comp.save()
            return HttpResponse(res)

def start_kneading(request, kneading_id):
    kneading = get_object_or_404(Kneading, pk=kneading_id)
    st = State_log(kneading = kneading, state = get_object_or_404(State, pk=2))
    st.save()
    components = serializers.serialize("json", Components.objects.all())
    l_comp = serializers.serialize("json", List_component.objects.filter(list = kneading.list))
    materials = serializers.serialize("json", Material.objects.all())
    formula = serializers.serialize("json", Formula.objects.all())
    return redirect('kneading_detail', kneading_id = kneading_id)


def start_mixing(request, kneading_id):
    kneading = get_object_or_404(Kneading, pk=kneading_id)
    if 'water_amm' in request.POST:
         cmps = List_component(list=kneading.list, mat=get_object_or_404(Material, code='ВД01'), ammount=request.POST['water_amm'])
         cmps.save()
    st = State_log(kneading = kneading, state = get_object_or_404(State, pk=3))
    st.save()
    reactor_content = Reactor_content.objects.filter(reactor = kneading.reactor)[0]
    if reactor_content.content_type != 3:
        el = List_component.objects.filter(list = kneading.list, r_cont = reactor_content)[0]
        el.loaded = True
        el.save()
    #reactor_content.content_type = 2
    #reactor_content.kneading = kneading
    #reactor_content.save()
    components = serializers.serialize("json", Components.objects.all())
    l_comp = serializers.serialize("json", List_component.objects.filter(list = kneading.list))
    materials = serializers.serialize("json", Material.objects.all())
    formula = serializers.serialize("json", Formula.objects.all())
    return redirect('kneading_detail', kneading_id = kneading_id)

def get_stor_inf(request):
    id = request.POST['id']
    if (id.split("-")[0] == 'r'):
        content = Reactor_content.objects.filter(pk = id.split("-")[1])[0]
    else:
        content = Tank_content.objects.filter(pk = id.split("-")[1])[0]
    if content.content_type == 1:
        name = str(content.batch.kneading.list.formula)
        code = content.batch.kneading.list.formula.code
        finish = str(content.batch.finish_date)
        batch = content.batch.kneading.batch_num
        comps = Batch_comp.objects.filter(batch = content.batch)
    else:
        name = str(content.kneading.list.formula)
        code = content.kneading.list.formula.code
        finish = str(content.kneading.finish_date)
        batch = content.kneading.batch_num
        comps = None
    data = {}
    data['name'] = name
    data['code'] = code
    data['finish'] = finish
    data['batch'] = batch
    data['amount'] = content.amount
    data['comps'] = {}
    if comps is not None:
        for c in comps:
            data['comps'][str(c.pk)]={"code": c.mat.code, "name": str(c.mat), "amount": c.ammount/100*content.amount}
    json_data = json.dumps(data)
    return HttpResponse(json_data)


def start_testing(request, kneading_id):
    kneading = get_object_or_404(Kneading, pk=kneading_id)
    if 'list_amm' in request.POST:
         kneading.list.ammount = request.POST['list_amm']
         kneading.list.save()
    st = State_log(kneading = kneading, state = get_object_or_404(State, pk=4))
    st.save()
    batch = Batch(kneading = kneading)
    batch.save()
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
            if c.r_cont is None and c.t_cont is None:
                if c.mat is None:
                    for c2 in Formula_component.objects.filter(formula = c.formula):
                        if c2.mat.id in components:
                            components[c2.mat.id]['amount'] = round(float(components[c2.mat.id]['amount']) + (c2.ammount / 1020) * c.ammount, 2)
                            comp_amm = comp_amm + round((c2.ammount / 1020) * c.ammount, 2)
                else:
                    if c.mat.id in components:
                        components[c.mat.id]['amount'] = round(float(components[c.mat.id]['amount']) + c.ammount, 2)
                        comp_amm = comp_amm + c.ammount
            else:
                if c.r_cont is None:
                    for c2 in Batch_comp.objects.filter(batch = c.t_cont.batch):
                        if c2.mat.id in components:
                            components[c2.mat.id]['amount'] = round(float(components[c2.mat.id]['amount']) + (c2.ammount / 100) * c.ammount, 2)
                            comp_amm = comp_amm + round((c2.ammount / 100) * c.ammount, 2)
                    if round(c.t_cont.amount, 2) == 0.00:
                        c.t_cont.batch = None
                        c.t_cont.kneading = None
                        c.t_cont.content_type = 3
                        c.t_cont.amount = 0
                        c.t_cont.save()
                else:
                    for c2 in Batch_comp.objects.filter(batch = c.r_cont.batch):
                        if c2.mat.id in components:
                            components[c2.mat.id]['amount'] = round(float(components[c2.mat.id]['amount']) + (c2.ammount / 100) * c.ammount, 2)
                            comp_amm = comp_amm + round((c2.ammount / 100) * c.ammount, 2)
                    if round(c.r_cont.amount, 2) == 0.00:
                        c.r_cont.batch = None
                        c.r_cont.kneading = None
                        c.r_cont.content_type = 3
                        c.r_cont.amount = 0
                        c.r_cont.save()
        else:
            for c2 in Compl_comp_comp.objects.filter(compl = c.compl):
                if c2.mat.id in components:
                    components[c2.mat.id]['amount'] = round(float(components[c2.mat.id]['amount']) + (c2.ammount / c.compl.ammount) * c.ammount, 2)
                    comp_amm = comp_amm + round((c2.ammount / c.compl.ammount) * c.ammount, 2)
    components[water.mat.id]['amount'] = round(float(components[water.mat.id]['amount']) + (float(kneading.list.ammount) - comp_amm), 2)
    reactor_content = Reactor_content.objects.filter(reactor = kneading.reactor)[0]
    reactor_content.content_type = 1
    reactor_content.amount = kneading.list.ammount
    reactor_content.batch = batch
    reactor_content.save()
    for c in components:
        comp = Batch_comp(batch = batch, mat = Material.objects.filter(code = components[c]['code'])[0], ammount = (components[c]['amount']/float(kneading.list.ammount))*100)
        comp.save()
    return redirect('kneading_detail', kneading_id = kneading_id)

def stop_process(request, kneading_id):
    kneading = get_object_or_404(Kneading, pk=kneading_id)
    kneading.isFinished = True
    kneading.save()
    st = State_log(kneading = kneading, state = get_object_or_404(State, pk=6))
    st.save()
    return redirect('kneading_detail', kneading_id = kneading_id)

def finish_process(request, kneading_id):
    kneading = get_object_or_404(Kneading, pk=kneading_id)
    st = State_log(kneading = kneading, state = get_object_or_404(State, pk=7))
    st.save()
    kneading.isFinished = True
    kneading.save()
    return redirect('mixing')

def save_reactor(request, kneading_id):
    kneading = get_object_or_404(Kneading, pk=kneading_id)
    reactor = Reactor.objects.filter(pk = request.POST['reactor'])[0]
    kneading.reactor = reactor
    kneading.save()
    return redirect('kneading_detail', kneading_id = kneading_id)

def finish_testing(request, kneading_id):
    kneading = get_object_or_404(Kneading, pk=kneading_id)
    st = State_log(kneading = kneading, state = get_object_or_404(State, pk=5))
    st.save()
    return redirect('kneading_detail', kneading_id = kneading_id)

def print_passport(request, kneading_id):
    kneading = get_object_or_404(Kneading, pk=kneading_id)
    batch = Batch.objects.filter(kneading = kneading)[0]
    amount = 0
    comps = {}
    processes = Kneading.objects.filter(list__formula = kneading.list.formula, batch_num = kneading.batch_num, start_date__year = kneading.start_date.year)
    for p in processes:
        amount = amount + p.list.ammount
        batch_t = Batch.objects.filter(kneading = p)[0]
        components = Batch_comp.objects.filter(batch = batch_t)
        for c in components:
            if c.mat.id in comps:
                comps[c.mat.id]["ammount"] = comps[c.mat.id]["ammount"] + (c.ammount / 100 * kneading.list.ammount)
            else:
                comps[c.mat.id] = {"code": c.mat.code, "name": c.mat, "ammount": c.ammount / 100 * kneading.list.ammount}
    #Получение состава
    #components = Batch_comp.objects.filter(batch = batch)
    #for c in components:
        #comps[c.id] = {"code": c.mat.code, "name": c.mat, "ammount": c.ammount / 100 * kneading.list.ammount}
    chars = {}
    temp_chars = Kneading_char.objects.filter(kneading = kneading)
    i = 0
    for c in temp_chars:
        comp_char = Composition_char.objects.filter(comp = kneading.list.formula.composition, characteristic = c.characteristic)[0]
        if c.characteristic.char_type.id != 3:
            try:
                chars[i] = {'group' : c.characteristic.group.name, 'type': 1, 'norm': str(comp_char.comp_char_range.inf) + "-" + str(comp_char.comp_char_range.sup),'name': c.characteristic.name, 'value': c.kneading_char_number.number}
            except Kneading_char_number.DoesNotExist:
                chars[i] = {}
        else:
            vars = Comp_char_var.objects.filter(comp_char = comp_char)
            vars_str = ""
            for v in vars:
                vars_str = vars_str + str(v.char_var) + ", "
            vars_str = vars_str[:(len(vars_str) -2)]
            if Kneading_char_var.objects.filter(kneading_char = c).count() > 0:
                val = Kneading_char_var.objects.filter(kneading_char = c)[0].char_var.name
                chars[i] = {'group' : c.characteristic.group.name, 'type': 1, 'norm': vars_str,'name': c.characteristic.name, 'value': val}
        i = i+1
    temp_chars = Composition_char.objects.filter(comp = kneading.list.formula.composition, characteristic__is_general = True)
    for c in temp_chars:
        comp_char = Composition_char.objects.filter(comp = kneading.list.formula.composition, characteristic = c.characteristic)[0]
        if c.characteristic.char_type.id != 3:
            try:
                chars[i] = {'group' : c.characteristic.group.name, 'type': 2, 'norm': str(c.comp_char_range.inf) + "-" + str(c.comp_char_range.sup), 'name': c.characteristic.name, 'value': c.comp_prop_number.number}
            except Kneading_char_number.DoesNotExist:
                chars[i] = {}
        else:
            vars = Comp_char_var.objects.filter(comp_char = c)
            vars_str = ""
            for v in vars:
                vars_str = vars_str + str(v.char_var) + ", "
            vars_str = vars_str[:(len(vars_str) -2)]
            if Comp_prop_var.objects.filter(comp_prop = c).count() > 0:
                val = Comp_prop_var.objects.filter(comp_prop = c)[0].char_var.name
                chars[i] = {'group' : c.characteristic.group.name, 'type': 2, 'norm': vars_str, 'name': c.characteristic.name, 'value': val}
        i = i+1
    return render(request, 'print.html', {"comps": List_component.objects.filter(list = kneading.list),
                                            "components": comps,
                                            "chars": chars,
                                            "amount": amount,
                                            "reactor": Reactor_content.objects.all(),
                                            "tank": Tank_content.objects.all(),
                                            "location": "/processes/process/",
                                            "reactor_content" : Reactor_content.objects.filter(batch = batch, reactor = kneading.reactor)[0] if Reactor_content.objects.filter(batch = batch, reactor = kneading.reactor).count()!=0 else None,
                                            "p": batch})

def kneading_detail(request, kneading_id):
    kneading = get_object_or_404(Kneading, pk=kneading_id)
    state_id = State_log.objects.filter(kneading = kneading).last().state.pk
    components = serializers.serialize("json", Components.objects.all())
    l_comp = serializers.serialize("json", List_component.objects.filter(list = kneading.list))
    materials = serializers.serialize("json", Material.objects.all())
    formula = serializers.serialize("json", Formula.objects.all())
    l_comp2 = List_component.objects.filter(list = kneading.list)
    #Добавить минимум максимум
    if state_id != 5 and state_id != 4:
        comps = {}
        for c in l_comp2:
            if c.min is None:
                min = "-"
                max = "-"
            else:
                min = c.min / c.list.ammount * 100
                max = c.max / c.list.ammount * 100
            if c.compl is None:
                if c.r_cont is None and c.t_cont is None and c.formula is None:
                    comps[str(c.id)]={'mat_code': c.mat.code, 'cont_id': c.mat.id, 'mat_name': str(c.mat), 'amount': str(c.ammount), 'loaded': int(c.loaded), 'min': min, 'max': max, "type": 4, 'formula': "None"}
                else:
                    if c.r_cont is None and c.formula is None:
                        comps[str(c.id)]={'mat_code': c.t_cont.batch.id, 'cont_id': c.t_cont.id, 'mat_name': str(c.t_cont.batch.kneading.list.formula), 'amount': str(c.ammount), 'loaded': int(c.loaded), 'min': min, 'max': max, "type": 2, 'formula': str(c.t_cont.batch.kneading.list.formula.pk)}
                    else:
                        if c.formula is None:
                            comps[str(c.id)]={'mat_code': c.r_cont.batch.id, 'cont_id': c.r_cont.id, 'mat_name': str(c.r_cont.batch.kneading.list.formula), 'amount': str(c.ammount), 'loaded': int(c.loaded), 'min': min, 'max': max, "type": 1, 'formula': str(c.r_cont.batch.kneading.list.formula.pk)}
                        else:
                            comps[str(c.id)]={'mat_code': c.formula.code, 'cont_id': c.formula.id, 'mat_name': str(c.formula), 'amount': str(c.ammount), 'loaded': int(c.loaded), 'min': min, 'max': max, "type": 5, 'formula': c.formula.pk}
            else:
                comps[str(c.id)]={'mat_code': c.compl.code, 'cont_id': c.compl.id, 'mat_name': c.compl.name, 'amount': str(c.ammount), 'loaded': int(c.loaded), 'min': min, 'max': max, "type": 3, 'formula': c.compl.formula.pk}

        load_list = json.dumps(comps)

    batches = {}
    i=0
    for r in Reactor_content.objects.filter(content_type = "1"):
        batches[str(i)] = {"id": r.pk, "formula": str(r.batch.kneading.list.formula.pk), "batch": r.batch.pk, "name": ("Партия №" + str(r.batch.pk) + " " + str(r.reactor)), "type": "1", "amount": (r.amount - r.reserved)}
        i=i+1
    for t in Tank_content.objects.filter(content_type = "1"):
        batches[str(i)] = {"id": t.pk, "formula": str(t.batch.kneading.list.formula.pk), "batch": t.batch.pk, "name": ("Партия №" + str(t.batch.pk) + " " + str(t.tank)), "type": "2", "amount": (t.amount - t.reserved)}
        i=i+1
    for c in Compl_comp.objects.all():
        batches[str(i)] = {"id": c.pk, "formula": str(c.formula.pk), "name": c.name, "type": "3", "amount": (c.store_amount - c.reserved)}
        i=i+1

    if state_id == 1:
        return render(request, 'waiting.html', {"components": json.dumps(components),
                                                "materials": json.dumps(materials),
                                                "l_c": json.dumps(l_comp),
                                                "c_id": kneading.list.formula.composition.id,
                                                "load_list": load_list,
                                                "reactors": Reactor.objects.all(),
                                                "batches": json.dumps(batches),
                                                "location": "/processes/process/",
                                                "p": kneading})
    if state_id == 2:
        return render(request, 'started.html', {"components": json.dumps(components),
                                                "materials": json.dumps(materials),
                                                "l_c": json.dumps(l_comp),
                                                "c_id": kneading.list.formula.composition.id,
                                                "load_list": load_list,
                                                "reactors": Reactor.objects.all(),
                                                "batches": json.dumps(batches),
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
            chars = Composition_char.objects.filter(comp = kneading.list.formula.composition, characteristic__is_general = False)
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
        components = Batch_comp.objects.filter(batch = batch)
        comps = {}
        for c in components:
            comps[c.id] = {"code": c.mat.code, "name": c.mat, "ammount": c.ammount / 100 * kneading.list.ammount}
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
        temp_chars = Composition_char.objects.filter(comp = kneading.list.formula.composition, characteristic__is_general = True)
        for c in temp_chars:
            if c.characteristic.char_type.id != 3:
                try:
                    chars[i] = {'group' : c.characteristic.group.name, 'name': c.characteristic.name, 'value': c.comp_prop_number.number}
                except:
                    chars[i] = {}
            else:
                if  Comp_prop_var.objects.filter(comp_prop = c).count() != 0:
                    val = Comp_prop_var.objects.filter(comp_prop = c)[0].char_var.name
                    chars[i] = {'group' : c.characteristic.group.name, 'name': c.characteristic.name, 'value': val}
            i = i+1

        return render(request, 'finished.html', {"comps": List_component.objects.filter(list = kneading.list),
                                                "chars": chars,
                                                "components": comps,
                                                "reactor": Reactor_content.objects.all(),
                                                "tank": Tank_content.objects.all(),
                                                "location": "/processes/process/",
                                                "reactor_content" : Reactor_content.objects.filter(batch = batch, reactor = kneading.reactor)[0] if Reactor_content.objects.filter(batch = batch, reactor = kneading.reactor).count()!=0 else None,
                                                "p": batch})

def archive_detail(request, kneading_id):
    kneading = get_object_or_404(Kneading, pk=kneading_id)
    components = serializers.serialize("json", Components.objects.all())
    batch = Batch.objects.filter(kneading = kneading)[0]
    components = Batch_comp.objects.filter(batch = batch)
    comps = {}
    for c in components:
        comps[c.id] = {"code": c.mat.code, "name": c.mat, "ammount": c.ammount / 100 * kneading.list.ammount}
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
    return render(request, 'arch_detail.html', {"comps": List_component.objects.filter(list = kneading.list),
                                                "chars": chars,
                                                "header": "Архив",
                                                "components": comps,
                                                "location": "/processes/archive/",
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
