from django.http.response import HttpResponse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from tables.models import Composition, Characteristic_set_var, Comp_char_var, Comp_char_range, Comp_char_number, Set_var, Composition_char, Material, Components, Formula, Formula_component, Reactor
from .models import Kneading_char_number, Batch, Kneading_char_var, Loading_list, List_component, Kneading, State, State_log, Kneading_char
import json
from django.core import serializers
from django.utils import timezone
import datetime

def loading_lists(request):
    return render(request, "loading_lists.html", {"header": "Загрузочные листы", "location": "/processes/loading_lists/", "lists": Loading_list.objects.all})

def mixing(request):
    return render(request, "process.html", {"header": "Процессы смешения", "location": "/processes/process/", "kneading": Kneading.objects.all})

def list_detail(request, list_id):
    components = serializers.serialize("json", Components.objects.all())
    materials = serializers.serialize("json", Material.objects.all())
    if (list_id == '0'):
        return render(request, "loading_list.html",
            {"list": None,
            "components": json.dumps(components),
            "compositions": Composition.objects.all,
            "materials": json.dumps(materials),
            "location": "/processes/loading_lists/",
            "header": "Загрузочные листы"
            })
    else:
        return render(request, "loading_list.html",
            {"list": get_object_or_404(Loading_list, pk=list_id),
            "components": json.dumps(components),
            "materials": json.dumps(materials),
            "compositions": Composition.objects.all,
            "location": "/processes/loading_lists/",
            "header": "Загрузочные листы"
            })

def planning(request):
    components = serializers.serialize("json", Components.objects.all())
    f_comp = serializers.serialize("json", Formula_component.objects.all())
    materials = serializers.serialize("json", Material.objects.all())
    formula = serializers.serialize("json", Formula.objects.all())
    return render(request, "planning.html",
        {"components": json.dumps(components),
        "materials": json.dumps(materials),
        "f_c": json.dumps(f_comp),
        "f": json.dumps(formula),
        "reactors": Reactor.objects.all,
        "formulas": Formula.objects.all,
        "location": "/processes/planning/",
        "header": "Планирование"
        })

def save_list(request, kneading_id):
    kneading = get_object_or_404(Kneading, pk=kneading_id)
    list = kneading.list
    if 'ammount' in request.POST:
        ammount = request.POST['ammount']
        list.ammount = ammount
    list.save()
    if 'json' in request.POST:
        table = request.POST['json']
        data = json.loads(table)
        for d in data:
            if d['Код']!='ВД01':
                mat = Material.objects.filter(code=d['Код'])[0]
                ammount=d["Количество, кг"]
                cmps = List_component.objects.filter(list=list, mat=mat)[0]
                cmps.ammount=ammount
                cmps.save()
        return redirect('loading_lists')

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
                    mat = Material.objects.filter(code=d['Код'])[0]
                    ammount=request.POST[d['Код']]
                    if d['Код'] in request.POST:
                        cmps = List_component(list=list, mat=mat, ammount=request.POST[d['Код']])
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
        return redirect('loading_lists')

def get_state(request):
    if request.method == 'POST':
        if 'id' in request.POST:
            log = State_log.objects.filter(kneading = get_object_or_404(Kneading, pk=request.POST['id'])).last()
            name = log.get_state()
            return HttpResponse(name)

def add_comp(request, kneading_id):
    if request.method == 'POST':
        if 'mat_id' in request.POST:
            comp = List_component.objects.filter(list = get_object_or_404(Kneading, pk=kneading_id).list, mat=get_object_or_404(Material, pk=request.POST['mat_id']))[0]
            comp.ammount = request.POST['amm']
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
    return render(request, 'started.html', {"components": json.dumps(components),
                                            "materials": json.dumps(materials),
                                            "l_c": json.dumps(l_comp),
                                            "c_id": kneading.list.formula.composition.id,
                                            "location": "/processes/process/",
                                            "p": kneading})

def start_mixing(request, kneading_id):
    kneading = get_object_or_404(Kneading, pk=kneading_id)
    if 'water_amm' in request.POST:
         cmps = List_component(list=kneading.list, mat=get_object_or_404(Material, code='ВД01'), ammount=request.POST['water_amm'])
         cmps.save()
    st = State_log(kneading = kneading, state = get_object_or_404(State, pk=3))
    st.save()
    components = serializers.serialize("json", Components.objects.all())
    l_comp = serializers.serialize("json", List_component.objects.filter(list = kneading.list))
    materials = serializers.serialize("json", Material.objects.all())
    formula = serializers.serialize("json", Formula.objects.all())
    return render(request, 'mixing.html', {"components": json.dumps(components),
                                            "materials": json.dumps(materials),
                                            "comp": List_component.objects.filter(list=kneading.list),
                                            "l_c": json.dumps(l_comp),
                                            "c_id": kneading.list.formula.composition.id,
                                            "location": "/processes/process/",
                                            "p": kneading})

def start_testing(request, kneading_id):
    kneading = get_object_or_404(Kneading, pk=kneading_id)
    if 'list_amm' in request.POST:
         kneading.list.ammount = request.POST['list_amm']
         kneading.list.save()
    st = State_log(kneading = kneading, state = get_object_or_404(State, pk=4))
    st.save()
    return render(request, 'testing.html', {
                                            "chars": Composition_char.objects.filter(comp = kneading.list.formula.composition),
                                            "location": "/processes/process/",
                                            "p": kneading})

def finish_testing(request, kneading_id):
    kneading = get_object_or_404(Kneading, pk=kneading_id)
    st = State_log(kneading = kneading, state = get_object_or_404(State, pk=5))
    st.save()
    batch = Batch(kneading = kneading)
    batch.save()
    return render(request, 'finished.html', {
                                            "location": "/processes/process/",
                                            "p": batch})

def kneading_detail(request, kneading_id):
    kneading = get_object_or_404(Kneading, pk=kneading_id)
    state_id = State_log.objects.filter(kneading = kneading).last().state.pk
    components = serializers.serialize("json", Components.objects.all())
    l_comp = serializers.serialize("json", List_component.objects.filter(list = kneading.list))
    materials = serializers.serialize("json", Material.objects.all())
    formula = serializers.serialize("json", Formula.objects.all())
    if state_id == 1:
        return render(request, 'waiting.html', {"components": json.dumps(components),
                                                "materials": json.dumps(materials),
                                                "l_c": json.dumps(l_comp),
                                                "c_id": kneading.list.formula.composition.id,
                                                "location": "/processes/process/",
                                                "p": kneading})
    if state_id == 2:
        return render(request, 'started.html', {"components": json.dumps(components),
                                                "materials": json.dumps(materials),
                                                "l_c": json.dumps(l_comp),
                                                "c_id": kneading.list.formula.composition.id,
                                                "location": "/processes/process/",
                                                "p": kneading})
    if state_id == 3:
        return render(request, 'mixing.html', {"components": json.dumps(components),
                                                "materials": json.dumps(materials),
                                                "comp": List_component.objects.filter(list=kneading.list),
                                                "l_c": json.dumps(l_comp),
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
                    isValid = isValid & (kneading_char.number <= comp_char.сomp_char_range.sup & kneading_char.number >= comp_char.сomp_char_range.inf)
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
