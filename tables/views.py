from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect

from .models import Material_group, Prefix, Unit, Material, Product_group, Product_form, Product_use, Product_mark, Product_option, Product_detail, Product, Composition, Composition_group, Components, Container
from .forms import Delete_form
import json


def index(request):
    return render(request, "materials.html", {"materials": Material.objects.all, "header": "Реактивы", "location": "/tables/materials/"})

def products(request):
    return render(request, "products.html",
        {"products": Product.objects.all,
        "groups": Product_group.objects.all, "header": "Продукция", "location": "/tables/products/"})

def packing(request):
    return render(request, "packing.html",
        {"containers": Container.objects.all, "header": "Фасовка", "location": "/tables/packing/"})


def compositions(request):
    return render(request, "compositions.html", {"compositions": Composition.objects.all, "groups": Composition_group.objects.all, "header": "Составы", "location": "/tables/compositions/"})

def detail(request, material_id):
    return render(request, "material.html",
        {"material": get_object_or_404(Material, pk=material_id),
        "groups": Material_group.objects.all,
        "units": Unit.objects.all,
        "prefixes": Prefix.objects.all})

def pr_detail(request, product_id):
    return render(request, "product.html",
        {"product": get_object_or_404(Product, pk=product_id),
        "groups": Product_group.objects.all,
        "forms": Product_form.objects.all,
        "uses": Product_use.objects.all,
        "marks": Product_mark.objects.all,
        "details": Product_detail.objects.all,
        "options": Product_option.objects.all,})

def comp_detail(request, composition_id):
    return render(request, "composition.html",
        {"comp": get_object_or_404(Composition, pk=composition_id),
        "groups": Composition_group.objects.all,
        "location": "/tables/compositions/",
        "comps": Components.objects.filter(comp=get_object_or_404(Composition, pk=composition_id)),
        "materials": Material.objects.all
        })

def new_material(request):
    return render(request, "new_material.html",
    {"groups": Material_group.objects.all,
    "units": Unit.objects.all,
    "prefixes": Prefix.objects.all})

def new_composition(request):
    return render(request, "new_composition.html",
    {"materials": Material.objects.all, "header": "Добавление состава", "location": "/tables/compositions/", "groups": Composition_group.objects.all})

def del_material(request):
    del_var = request.POST.getlist('del_list')
    for d in del_var:
        del_obj = get_object_or_404(Material, pk=d)
        del_obj.delete()
    return redirect('index')

def del_product(request):
    del_var = request.POST.getlist('del_list')
    for d in del_var:
        del_obj = get_object_or_404(Product, pk=d)
        del_obj.delete()
    return redirect('products')

def new_product(request):
    return render(request, "new_product.html",
    {"groups": Product_group.objects.all,
    "forms": Product_form.objects.all,
    "uses": Product_use.objects.all,
    "marks": Product_mark.objects.all,
    "details": Product_detail.objects.all,
    "options": Product_option.objects.all,})

def add_material(request):
    try:
        code = request.POST['code']
        name = request.POST['name']
        group = get_object_or_404(Material_group, pk=request.POST['group'])
        prefix = get_object_or_404(Prefix, pk=request.POST['prefix'])
        mark = request.POST['mark']
        unit = get_object_or_404(Unit, pk=request.POST['unit'])
        concentration = request.POST['concentration']
        ammount = request.POST['ammount']
        material = Material(code = code,
        name = name,
        group = group,
        prefix = prefix,
        mark = mark,
        unit = unit,
        concentration = concentration,
        ammount = ammount)

    except (KeyError, Material_group.DoesNotExist):
        return render(request, 'index.html', {"materials": Material.objects.all, 'error_message': 'Option does not exist'})
    else:
        material.save()
        return redirect('index')


def save_material(request, material_id):
    material = get_object_or_404(Material, pk=material_id)
    try:
        code = request.POST['code']
        name = request.POST['name']
        group = get_object_or_404(Material_group, pk=request.POST['group'])
        prefix = get_object_or_404(Prefix, pk=request.POST['prefix'])
        mark = request.POST['mark']
        unit = get_object_or_404(Unit, pk=request.POST['unit'])
        concentration = request.POST['concentration']
        ammount = request.POST['ammount']
        material.code = code
        material.name = name
        material.group = group
        material.prefix = prefix
        material.mark = mark
        material.unit = unit
        material.concentration = concentration
        material.ammount = ammount
    except (KeyError, Material_group.DoesNotExist):
        return render(request, 'index.html', {"materials": Material.objects.all, 'error_message': 'Option does not exist'})
    else:
        material.save()
        return redirect('index')

def pr_group(request):
    if 'group1' in request.POST:
        pk = request.POST['group1']
    else:
        pk=0
    group = get_object_or_404(Product_group, pk=pk)
    product_group = Product.objects.filter(group=group)
    return render(request, "products.html",
            {"products": product_group,
            "groups": Product_group.objects.all, "header": "Продукция", "location": "/tables/products/"})

def comp_group(request):
    if 'group1' in request.POST:
        pk = request.POST['group1']
    else:
        pk=0
    group = get_object_or_404(Composition_group, pk=pk)
    comp_group = Composition.objects.filter(group=group)
    return render(request, "compositions.html",
            {"compositions": comp_group,
            "groups": Composition_group.objects.all, "header": "Составы", "location": "/tables/compositions/"})

def save_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    try:
        code = request.POST['code']
        name = request.POST['name']
        group = get_object_or_404(Product_group, pk=request.POST['group'])
        form = get_object_or_404(Product_form, pk=request.POST['form'])
        use = get_object_or_404(Product_use, pk=request.POST['use'])
        option = get_object_or_404(Product_option, pk=request.POST['option'])
        detail = get_object_or_404(Product_detail, pk=request.POST['detail'])
        mark = get_object_or_404(Product_mark, pk=request.POST['mark'])

        product.code = code
        product.name = name
        product.group = group
        product.form = form
        product.use = use
        product.option = option
        product.detail = detail
        product.mark = mark
    except (KeyError, Material_group.DoesNotExist):
        return render(request, 'products.html', {"materials": Material.objects.all, 'error_message': 'Option does not exist'})
    else:
        product.save()
        return redirect("products")

def add_product(request):
    try:
        code = request.POST['code']
        name = request.POST['name']
        group = get_object_or_404(Product_group, pk=request.POST['group'])
        form = get_object_or_404(Product_form, pk=request.POST['form'])
        use = get_object_or_404(Product_use, pk=request.POST['use'])
        option = get_object_or_404(Product_option, pk=request.POST['option'])
        detail = get_object_or_404(Product_detail, pk=request.POST['detail'])
        mark = get_object_or_404(Product_mark, pk=request.POST['mark'])
        product = Product(
            code = code,
            name = name,
            group = group,
            form = form,
            use = use,
            option = option,
            detail = detail,
            mark = mark)

    except (KeyError, Material_group.DoesNotExist):
        return render(request, 'index.html', {"materials": Material.objects.all, 'error_message': 'Option does not exist'})
    else:
        product.save()
        return redirect('products')

def add_composition(request):
    try:
        code = request.POST['code']
        name = request.POST['name']
        group = get_object_or_404(Composition_group, pk=request.POST['group'])
        sgr = request.POST['sgr']
        comp = Composition(
            code = code,
            name = name,
            group = group,
            sgr = sgr)
    except (KeyError, Composition_group.DoesNotExist):
        return render(request, 'index.html', {"materials": Material.objects.all, 'error_message': 'Option does not exist'})
    else:
        comp.save()
        if 'json' in request.POST:
            table = request.POST['json']
            data = json.loads(table)
            for d in data:
                mat = Material.objects.filter(code=d['Код'])[0]
                cmps = Components(comp=comp, mat=mat, min=d["Минимум чистого реактива"], max=d["Максимум чистого реактива"])
                cmps.save()

        return redirect('compositions')

def save_composition(request, composition_id):
    comp = get_object_or_404(Composition, pk=composition_id)
    try:
        code = request.POST['code']
        name = request.POST['name']
        group = get_object_or_404(Composition_group, pk=request.POST['group'])
        sgr = request.POST['sgr']
        comp.code = code
        comp.name = name
        comp.group = group
        comp.sgr = sgr
    except (KeyError, Composition_group.DoesNotExist):
        return render(request, 'index.html', {"materials": Material.objects.all, 'error_message': 'Option does not exist'})
    else:
        comp.save()
        Components.objects.filter(comp=comp).delete()
        if 'json' in request.POST:
            table = request.POST['json']
            data = json.loads(table)
            for d in data:
                mat = Material.objects.filter(code=d['Код'])[0]
                cmps = Components(comp=comp, mat=mat, min=d["Минимум чистого реактива"], max=d["Максимум чистого реактива"])
                cmps.save()

        return redirect('compositions')


# Create your views here.
