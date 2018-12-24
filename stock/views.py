from django.http.response import HttpResponse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
import json
from tables.models import Material
from django.core import serializers
from django.utils import timezone
import datetime

def goods_models(request):
    return render(request, "goods_models.html", {"header": "Макеты материальных ценностей"})

