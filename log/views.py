from django.http.response import HttpResponse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
import json
from django.core import serializers
from django.utils import timezone
import datetime
from .models import  Movement_rec, Operation, Acceptance
from processes.models import Batch
from tables.models import Product, Composition, Compl_comp, Compl_comp_comp, Characteristic_set_var, Comp_char_var, Comp_char_range, Comp_char_number, Set_var, Composition_char, Material, Components, Formula, Formula_component, Reactor

def materials(request):
    return render(request, "materials.html", {"header": "Контроль входного сырья", "location": "/log/materials/", "lists": Model_list.objects.all})

def movement(request):
    try:
        last_acc = Acceptance.objects.latest('date').code + 1
    except:
        last_acc = 1
    batches = {}
    for r in Movement_rec.objects.all():
        if r.operation.id == 1 or r.operation.id == 2 or r.operation.id == 3:
            name = str(r.batch.id) + "_" + str(r.product.id)
            if name not in batches:
                amm = 0
                for m in Movement_rec.objects.filter(product = r.product, batch = r.batch):
                    if m.operation.id == 1:
                        amm = amm + m.amount
                    else:
                        if m.operation.id == 2 or m.operation.id == 3:
                            amm = amm - m.amount
                if amm > 0:
                    batches[name] = {"pr_id": r.product.id, "code": r.product.code,  "name": r.product.get_name_for_table(), "batch": r.get_batch(), "amount": amm}
    return render(request, "movement.html", {"header": "Журнал прихода и расхода", "location": "/log/movement/", "movements": Movement_rec.objects.all, "batches": batches, "last_acc": last_acc, "batches2": json.dumps(batches)})

def accepting(request):
    acts = {}
    for a in Acceptance.objects.all():
        if a.code not in acts:
            acts[a.code] = {"date": a.date.strftime('%d.%m.%Y')}
    return render(request, "accepting.html", {"header": "Акты приёма передачи товара", "location": "/log/accepting/", "acts": acts})

def release(request):
    if request.method == 'POST':
        id = request.POST['id']
        pr_id = id.split("_")[1]
        b_id = id.split("_")[0]
        product = Product.objects.filter(id = pr_id)[0]
        batch = Batch.objects.filter(id = b_id)[0]
        if request.POST['op']=='1':
            rec = Movement_rec(product = product, batch = batch, amount = request.POST['amm'], operation = Operation.objects.filter(id = 3)[0])
            code = request.POST['code']
            try:
                code = Acceptance.objects.latest('date').code + 1
            except:
                code = 1
            rec.save()
            acc = Acceptance(code = code, prod = rec)
            acc.save()
        else:
            rec = Movement_rec(product = product, batch = batch, amount = request.POST['amm'], operation = Operation.objects.filter(id = 2)[0])
        rec.save()
        return HttpResponse('ok')

def get_act(request):
    if request.method == 'POST':
        code = request.POST['code']
        inf_a = {}
        for a in Acceptance.objects.filter(code = code):
            date = a.date
            inf_a[str(a.prod.pk)] = {"code": a.prod.product.code, "name": a.prod.product.get_name_for_table(), "batch": a.prod.get_batch(), "amount": str(a.prod.amount)}
        inf_a['date'] = date.strftime('%d.%m.%Y')
        data = json.dumps(inf_a)
        return HttpResponse(data)

def get_act_by_prod(request):
    if request.method == 'POST':
        prod = request.POST['prod']
        product = Movement_rec.objects.filter(pk = prod)[0]
        code = Acceptance.objects.filter(prod = product)[0].code
        inf_a = {}
        for a in Acceptance.objects.filter(code = code):
            date = a.date
            inf_a[str(a.prod.pk)] = {"code": a.prod.product.code, "name": a.prod.product.get_name_for_table(), "batch": a.prod.get_batch(), "amount": str(a.prod.amount)}
        inf_a['date'] = date.strftime('%d.%m.%Y')
        inf_a['code'] = code
        data = json.dumps(inf_a)
        return HttpResponse(data)
