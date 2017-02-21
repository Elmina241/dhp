from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from tables.models import Composition, Material, Components
import json
from django.core import serializers

def loading_lists(request):
    return render(request, "loading_lists.html", {"header": "Загрузочные листы", "location": "/processes/loading_lists/"})

def list_detail(request, list_id):
    components = serializers.serialize("json", Components.objects.all())
    materials = serializers.serialize("json", Material.objects.all())
    if (list_id == '0'):
        return render(request, "loading_list.html",
            {"list": None,
            "components": json.dumps(components),
            "compositions": Composition.objects.all,
            "materials": json.dumps(materials),
            "location": "/processes/loading_lists/"
            })
    else:
        return render(request, "loading_list.html",
            {"list": get_object_or_404(Loading_list, pk=list_id),
            "components": json.dumps(components),
            "materials": json.dumps(materials),
            "compositions": Composition.objects.all,
            "location": "/processes/loading_lists/"
            })
