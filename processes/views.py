from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from tables.models import Composition, Material, Components, Formula, Formula_component
from .models import Loading_list, List_component
import json
from django.core import serializers

def loading_lists(request):
    return render(request, "loading_lists.html", {"header": "Загрузочные листы", "location": "/processes/loading_lists/", "lists": Loading_list.objects.all})

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
