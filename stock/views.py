from django.http.response import HttpResponse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
import json
from tables.models import Material
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
    return render(request, "goods_models.html", {"header": "Макеты материальных ценностей", "tree": json.dumps(tree)})
