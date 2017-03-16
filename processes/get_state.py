from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from .models import Kneading, State, State_log
import json
from django.core import serializers

if 'id' in request.GET:
    log = State_log.objects.filter(kneading = get_object_or_404(Kneading, pk=GET['id'])).last()
    print(log.state.name)
