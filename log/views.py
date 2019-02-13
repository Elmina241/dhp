from django.http.response import HttpResponse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
import json
from django.core import serializers
from django.utils import timezone
import datetime
from .models import  Movement_rec, Operation, Acceptance, Packing_divergence, Packaged
from processes.models import Batch, Kneading_char, Kneading_char_number, Kneading_char_var, Kneading
from tables.models import Product, Composition, Compl_comp, Compl_comp_comp, Characteristic_set_var, Comp_char_var, Comp_char_range, Comp_char_number, Set_var, Composition_char, Material, Components, Formula, Formula_component, Reactor

def materials(request):
    return render(request, "materials.html", {"header": "Контроль входного сырья", "location": "/log/materials/", "lists": Model_list.objects.all})

def movement(request):
    try:
        last_acc = Acceptance.objects.latest('date').code + 1
    except:
        last_acc = 1
    prods = {}
    for p in Product.objects.all():
        prods[str(p.pk)] = {'name': p.code + " " + p.get_name_for_table(), 'composition': p.production.composition.id}
    records = {}
    for r in Movement_rec.objects.order_by("-id")[:20]:
        records[str(r.id)] = {"date": r.date.strftime('%d.%m.%Y'), "code": r.product.code, "name": r.product.get_name_for_table, "batch": r.get_batch, "operation": r.operation.name, "amount": r.amount, "comp": r.batch.kneading.list.formula.composition.id}
    batches = {}
    for p in Packaged.objects.all():
        name = str(p.rec.batch.id) + "_" + str(p.rec.product.id)
        if name in batches:
            batches[name]['amount'] = batches[name]['amount'] + p.amount
        else:
            batches[name] = {"pr_id": p.rec.product.id, "code": p.rec.product.code, "name": p.rec.product.get_name_for_table(), "batch": p.rec.get_batch(), "amount": p.amount}
    # for r in Movement_rec.objects.all():
    #     if r.operation.id == 1 or r.operation.id == 2 or r.operation.id == 3:
    #         name = str(r.batch.id) + "_" + str(r.product.id)
    #         if name not in batches:
    #             amm = 0
    #             for m in Movement_rec.objects.filter(product = r.product, batch = r.batch):
    #                 if m.operation.id == 1:
    #                     amm = amm + m.amount
    #                 else:
    #                     if m.operation.id == 2 or m.operation.id == 3:
    #                         amm = amm - m.amount
    #             if amm > 0:
    #                 batches[name] = {"pr_id": r.product.id, "code": r.product.code,  "name": r.product.get_name_for_table(), "batch": r.get_batch(), "amount": amm}
    return render(request, "movement.html", {"header": "Журнал прихода и расхода", "location": "/log/movement/", "movements": records, "batches": batches, "last_acc": last_acc, "products": json.dumps(prods), "batches2": json.dumps(batches)})

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
            #try:
                #code = Acceptance.objects.latest('code').code + 1
            #except:
                #code = 1
            rec.save()
            acc = Acceptance(code = code, prod = rec)
            acc.save()
        else:
            rec = Movement_rec(product = product, batch = batch, amount = request.POST['amm'], operation = Operation.objects.filter(id = 2)[0])
        rec.save()
        amm = float(request.POST['amm'])
        for p_rec in Packaged.objects.filter(rec__batch = batch, rec__product = product):
            if p_rec.amount <= amm:
                amm = amm - p_rec.amount
                p_rec.delete()
            else:
                p_rec.amount = p_rec.amount - amm
                p_rec.save()
                amm = 0
        return HttpResponse('ok')

def add_rows(request):
    if request.method == 'POST':
        count = request.POST['count']
        count = int(count) + 1
        records = {}
        for r in Movement_rec.objects.order_by("-id")[20*(int(count)-1):20*int(count)]:
            date = r.date.strftime('%d.%m.%Y')
            name = r.product.get_name_for_table()
            batch = r.get_batch()
            records[str(r.id)] = {"date": date, "code": r.product.code, "name": name, "batch": batch, "operation": r.operation.name, "amount": r.amount, "comp": r.batch.kneading.list.formula.composition.id}
        res = json.dumps(records)
        return HttpResponse(res)

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
        err = True
        for a in Acceptance.objects.filter(code = code):
            date = a.date
            err = err and Movement_rec.objects.filter(batch = a.prod.batch)[0].is_printed
            inf_a[str(a.prod.pk)] = {"code": a.prod.product.code, "name": a.prod.product.get_name_for_table(), "batch": a.prod.get_batch(), "amount": str(a.prod.amount)}
            print(err)
        inf_a['date'] = date.strftime('%d.%m.%Y')
        inf_a['code'] = code
        inf_a['check'] = err
        data = json.dumps(inf_a)
        return HttpResponse(data)

def get_pass(request):
    if request.method == 'POST':
        prod = request.POST['prod']
        product = Movement_rec.objects.filter(pk = prod)[0]
        #amount2 = Packing_divergence.objects.filter(batch = product.batch, date = product.date)[0].pack_amm
        pass_num = Movement_rec.objects.filter(operation__id = 1, pk__lte = prod).count()
        amount = 0
        processes = Kneading.objects.filter(list__formula=product.batch.kneading.list.formula, batch_num=product.batch.kneading.batch_num,
                                            start_date__year=product.batch.kneading.start_date.year)
        for p in processes:
            amount = amount + p.list.ammount
        inf_a = {
            "id": pass_num,
            "code": product.product.code,
            "name": product.product.get_name_for_table(),
            "batch": product.get_batch(),
            "amount": amount,
            "date": product.date.strftime('%d.%m.%Y'),
            "standard": product.batch.kneading.list.formula.composition.standard,
            "pack": product.batch.kneading.list.formula.composition.get_package_pass(),
            "sh_life": product.batch.kneading.list.formula.composition.sh_life
        }
        kneading = product.batch.kneading
        chars = {}
        temp_chars = Kneading_char.objects.filter(kneading=kneading).order_by('-characteristic__group')  # type: Any
        i = 0
        for c in temp_chars:
            comp_char = Composition_char.objects.filter(comp=kneading.list.formula.composition, characteristic=c.characteristic)[0]
            if c.characteristic.char_type.id != 3:
                try:
                    chars[i] = {'group': c.characteristic.group.name, 'type': 1,
                                'norm': str(comp_char.comp_char_range.inf) + "-" + str(comp_char.comp_char_range.sup),
                                'name': c.characteristic.name, 'value': c.kneading_char_number.number}
                except Kneading_char_number.DoesNotExist:
                    chars[i] = {}
            else:
                vars = Comp_char_var.objects.filter(comp_char=comp_char)
                vars_str = ""
                for v in vars:
                    vars_str = vars_str + str(v.char_var) + ", "
                vars_str = vars_str[:(len(vars_str) - 2)]
                if Kneading_char_var.objects.filter(kneading_char=c).count() > 0:
                    val = Kneading_char_var.objects.filter(kneading_char=c)[0].char_var.name
                    chars[i] = {'group': c.characteristic.group.name, 'type': 1, 'norm': vars_str,
                                'name': c.characteristic.name, 'value': val}
            i = i + 1
        data = {}
        data["inf_a"] = inf_a
        data["chars"] = chars
        data = json.dumps(data)
        return HttpResponse(data)

def print_pass(request):
    if request.method == 'POST':
        if "prod" in request.POST:
            product = Movement_rec.objects.filter(pk = request.POST['prod'])[0]
            product.is_printed = True
            product.save()
            return HttpResponse("ok")

def edit_pack(request):
    if request.method == 'POST':
        #Дописать соответсвие выпуску товара
        movm = Movement_rec.objects.get(id = request.POST['id'])
        div = Packing_divergence.objects.filter(batch = movm.batch, date = movm.date)[0]
        div.prod_num = request.POST['amm']
        prod = get_object_or_404(Product, pk=request.POST['pr_id'])
        div.product = prod
        movm.product = prod
        movm.amount = request.POST['amm']
        p_rec = Packaged.objects.filter(rec = movm)[0]
        p_rec.amount = movm.amount
        p_rec.save()
        div.save()
        movm.save()
        return HttpResponse('ok')
