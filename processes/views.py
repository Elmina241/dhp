from django.http.response import HttpResponse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from tables.models import Composition, Material, Components, Formula, Formula_component
from .models import Loading_list, List_component, Kneading, State, State_log
import json
from django.core import serializers
from django.utils import timezone
import datetime

def loading_lists(request):
    return render(request, "loading_lists.html", {"header": "Загрузочные листы", "location": "/processes/loading_lists/", "lists": Loading_list.objects.all})

def mixing(request):
    return render(request, "mixing.html", {"header": "Процессы смешения", "location": "/processes/mixing/", "kneading": Kneading.objects.all})

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
        "formulas": Formula.objects.all,
        "location": "/processes/planning/",
        "header": "Планирование"
        })

def save_list(request, list_id):
    if (list_id == '0'):
        list = Loading_list()
    else:
        list = get_object_or_404(Loading_list, pk=list_id)
    try:
        if 'ammount' in request.POST:
            ammount = request.POST['ammount']
            composition = get_object_or_404(Composition, pk=request.POST['composition'])
            list.ammount = ammount
            list.composition = composition
    except (KeyError, Loading_list.DoesNotExist):
        return render(request, 'loading_lists.html', {'error_message': 'Option does not exist'})
    else:
        list.save()
        List_component.objects.filter(list=list).delete()
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
        return redirect('loading_lists')

def save_process(request):
    list = Loading_list()
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
        if 'start' in request.POST:
            kneading = Kneading()
            st_date = request.POST['start']
            end_date = request.POST['end']
            kneading.start_date = datetime.datetime.strptime(st_date, "%d/%m/%Y").date()
            kneading.finish_date = datetime.datetime.strptime(end_date, "%d/%m/%Y").date()
            kneading.list = list
            kneading.save()
            st = State_log(kneading = kneading, state = get_object_or_404(State, pk=1))
            st.save()
        return redirect('loading_lists')

def get_state(request):
    if request.method == 'POST':
        if 'id' in request.POST:
            log = get_object_or_404(State, pk=1)
            #log = State_log.objects.filter(kneading = get_object_or_404(Kneading, pk=request.POST['id'])).first()
            name = log.name
            return HttpResponse(name)
