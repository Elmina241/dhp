from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect

from .models import Material_group, Prefix, Unit, Material, Product_group, Product_form, Product_use, Product_mark, Product_option, Product_detail, Product, Composition, Composition_group, Components, Container, Cap, Boxing, Sticker, Production, Reactor, Tank, Container_group, Container_mat, Colour, Container_form, Cap_group, Cap_form, Sticker_part, Formula_component, Formula
from .forms import Delete_form
import json
from django.core import serializers


def index(request):
    return render(request, "materials.html", {"materials": Material.objects.all, "header": "Реактивы", "location": "/tables/materials/"})

def products(request):
    return render(request, "products.html",
        {"products": Product.objects.all,
        "groups": Product_group.objects.all, "header": "Продукция", "location": "/tables/products/"})

def packing(request):
    return render(request, "packing.html",
        {"containers": Container.objects.all, "header": "Фасовка", "location": "/tables/packing/"})

def formulas(request):
    return render(request, "formulas.html",
        {"formulas": Formula.objects.all, "header": "Составы", "location": "/tables/formulas/"})

def caps(request):
    return render(request, "caps.html",
        {"caps": Cap.objects.all, "header": "Фасовка", "location": "/tables/packing/"})

def production(request):
    return render(request, "production.html",
        {"production": Production.objects.all, "header": "Производство", "location": "/tables/production/"})

def storage(request):
    return render(request, "storage.html",
        {"reactors": Reactor.objects.all, "tanks": Tank.objects.all, "header": "Хранилища", "location": "/tables/storage/"})

def boxing(request):
    return render(request, "boxing.html",
        {"boxes": Boxing.objects.all, "header": "Фасовка", "location": "/tables/packing/"})

def stickers(request):
    return render(request, "stickers.html",
        {"stickers": Sticker.objects.all, "header": "Фасовка", "location": "/tables/packing/"})

def compositions(request):
    return render(request, "compositions.html", {"compositions": Composition.objects.all, "groups": Composition_group.objects.all, "header": "Рецепты", "location": "/tables/compositions/"})

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

def comm_detail(request, commodity_id):
        if (commodity_id == '0'):
            return render(request, "commodity.html",
                {"container": None,
                "products": Product.objects.all,
                "compositions": Composition.objects.all,
                "containers": Container.objects.all,
                "caps": Cap.objects.all,
                "location": "/tables/production/",
                "stickers": Sticker.objects.all,
                "boxing": Boxing.objects.all
                })
        else:
            return render(request, "commodity.html",
                {"commodity": get_object_or_404(Production, pk=commodity_id),
                "products": Product.objects.all,
                "compositions": Composition.objects.all,
                "containers": Container.objects.all,
                "caps": Cap.objects.all,
                "location": "/tables/production/",
                "stickers": Sticker.objects.all,
                "boxing": Boxing.objects.all
                })

def formula_detail(request, formula_id):
        components = serializers.serialize("json", Components.objects.all())
        materials = serializers.serialize("json", Material.objects.all())
        if (formula_id == '0'):
            return render(request, "formula.html",
                {"formula": None,
                "components": json.dumps(components),
                "compositions": Composition.objects.all,
                "materials": json.dumps(materials),
                "location": "/tables/formulas/"
                })
        else:
            return render(request, "formula.html",
                {"formula": get_object_or_404(Formula, pk=formula_id),
                "components": json.dumps(components),
                "compositions": Composition.objects.all,
                "materials": json.dumps(materials),
                "location": "/tables/formulas/"
                })

def storage_detail(request):
        return render(request, "edit_storage.html",
                {"storage": None,
                "location": "/tables/storage/"
                })


def comp_detail(request, composition_id):
    return render(request, "composition.html",
        {"comp": get_object_or_404(Composition, pk=composition_id),
        "groups": Composition_group.objects.all,
        "location": "/tables/compositions/",
        "comps": Components.objects.filter(comp=get_object_or_404(Composition, pk=composition_id)),
        "materials": Material.objects.all
        })

def container_detail(request, container_id):
    if (container_id == '0'):
        return render(request, "container.html",
            {"container": None,
            "groups": Container_group.objects.all,
            "colours": Colour.objects.all,
            "materials": Container_mat.objects.all,
            "location": "/tables/packing/",
            "forms": Container_form.objects.all
            })
    else:
        return render(request, "container.html",
            {"container": get_object_or_404(Container, pk=container_id),
            "groups": Container_group.objects.all,
            "colours": Colour.objects.all,
            "materials": Container_mat.objects.all,
            "location": "/tables/packing/",
            "forms": Container_form.objects.all
            })

def cap_detail(request, cap_id):
    if (cap_id == '0'):
        return render(request, "cap.html",
            {"cap": None,
            "groups": Cap_group.objects.all,
            "colours": Colour.objects.all,
            "materials": Container_mat.objects.all,
            "location": "/tables/packing/",
            "forms": Cap_form.objects.all
            })
    else:
        return render(request, "cap.html",
            {"cap": get_object_or_404(Cap, pk=cap_id),
            "groups": Cap_group.objects.all,
            "colours": Colour.objects.all,
            "materials": Container_mat.objects.all,
            "location": "/tables/packing/",
            "forms": Cap_form.objects.all
            })

def box_detail(request, box_id):
    if (box_id == '0'):
        return render(request, "box.html",
            {"box": None,
            "location": "/tables/packing/",
            })
    else:
        return render(request, "box.html",
            {"box": get_object_or_404(Boxing, pk=box_id),
            "location": "/tables/packing/"
            })

def sticker_detail(request, sticker_id):
    if (sticker_id == '0'):
        return render(request, "sticker.html",
            {"sticker": None,
            "products": Product.objects.all,
            "parts": Sticker_part.objects.all,
            "location": "/tables/packing/",
            })
    else:
        return render(request, "sticker.html",
            {"sticker": get_object_or_404(Sticker, pk=sticker_id),
            "products": Product.objects.all,
            "parts": Sticker_part.objects.all,
            "location": "/tables/packing/"
            })

def reactor_detail(request, storage_id):
    return render(request, "edit_storage.html",
        {"storage": get_object_or_404(Reactor, pk=storage_id),
        "is_tank": "",
        "location": "/tables/storage/"
        })

def tank_detail(request, storage_id):
    return render(request, "edit_storage.html",
        {"storage": get_object_or_404(Tank, pk=storage_id),
        "is_tank": "checked",
        "location": "/tables/storage/"
        })

def new_material(request):
    return render(request, "new_material.html",
    {"groups": Material_group.objects.all,
    "units": Unit.objects.all,
    "prefixes": Prefix.objects.all})

def new_composition(request):
    return render(request, "new_composition.html",
    {"materials": Material.objects.all, "header": "Добавление рецепта", "location": "/tables/compositions/", "groups": Composition_group.objects.all})

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

def del_box(request):
    del_var = request.POST.getlist('del_list')
    for d in del_var:
        del_obj = get_object_or_404(Boxing, pk=d)
        del_obj.delete()
    return redirect('boxing')

def del_cap(request):
    del_var = request.POST.getlist('del_list')
    for d in del_var:
        del_obj = get_object_or_404(Cap, pk=d)
        del_obj.delete()
    return redirect('caps')

def del_composition(request):
    del_var = request.POST.getlist('del_list')
    for d in del_var:
        del_obj = get_object_or_404(Composition, pk=d)
        Components.objects.filter(comp=del_obj).delete()
        del_obj.delete()
    return redirect('compositions')

def del_packing(request):
    del_var = request.POST.getlist('del_list')
    for d in del_var:
        del_obj = get_object_or_404(Container, pk=d)
        del_obj.delete()
    return redirect('packing')

def del_commodity(request):
    del_var = request.POST.getlist('del_list')
    for d in del_var:
        del_obj = get_object_or_404(Production, pk=d)
        del_obj.delete()
    return redirect('production')

def del_sticker(request):
    del_var = request.POST.getlist('del_list')
    for d in del_var:
        del_obj = get_object_or_404(Sticker, pk=d)
        del_obj.delete()
    return redirect('stickers')

def del_storage(request):
    del_var1 = request.POST.getlist('del_list1')
    del_var2 = request.POST.getlist('del_list2')
    for d in del_var1:
        del_obj = get_object_or_404(Reactor, pk=d)
        del_obj.delete()
    for d in del_var2:
        del_obj = get_object_or_404(Tank, pk=d)
        del_obj.delete()
    return redirect('storage')

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

def save_container(request, container_id):
    if (container_id == '0'):
        container = Container()
    else:
        container = get_object_or_404(Container, pk=container_id)
    try:
        code = request.POST['code']
        group = get_object_or_404(Container_group, pk=request.POST['group'])
        form = get_object_or_404(Container_form, pk=request.POST['form'])
        colour = get_object_or_404(Colour, pk=request.POST['colour'])
        mat = get_object_or_404(Container_mat, pk=request.POST['container_mat'])
        container.code = code
        container.group = group
        container.form = form
        container.colour = colour
        container.mat = mat
    except (KeyError, Container_group.DoesNotExist):
        return render(request, 'index.html', {"materials": Material.objects.all, 'error_message': 'Option does not exist'})
    else:
        container.save()
        return redirect('packing')

def save_cap(request, cap_id):
    if (cap_id == '0'):
        cap = Cap()
    else:
        cap = get_object_or_404(Cap, pk=cap_id)
    try:
        code = request.POST['code']
        group = get_object_or_404(Cap_group, pk=request.POST['group'])
        form = get_object_or_404(Cap_form, pk=request.POST['form'])
        colour = get_object_or_404(Colour, pk=request.POST['colour'])
        mat = get_object_or_404(Container_mat, pk=request.POST['container_mat'])
        cap.code = code
        cap.group = group
        cap.form = form
        cap.colour = colour
        cap.mat = mat
    except (KeyError, Cap_group.DoesNotExist):
        return render(request, 'index.html', {"materials": Material.objects.all, 'error_message': 'Option does not exist'})
    else:
        cap.save()
        return redirect('caps')

def save_box(request, box_id):
    if (box_id == '0'):
        box = Boxing()
    else:
        box = get_object_or_404(Boxing, pk=box_id)
    if ('name' in request.POST) & ('code' in request.POST):
        code = request.POST['code']
        name = request.POST['name']
        box.code = code
        box.name = name
        box.save()
        return redirect('boxing')
    else:
        return render(request, 'index.html', {"materials": Material.objects.all, 'error_message': 'Option does not exist'})


def save_sticker(request, sticker_id):
    if (sticker_id == '0'):
        sticker = Sticker()
    else:
        sticker = get_object_or_404(Sticker, pk=sticker_id)
    try:
        code = request.POST['code']
        product = get_object_or_404(Product, pk=request.POST['product'])
        part = get_object_or_404(Sticker_part, pk=request.POST['part'])
        sticker.code = code
        sticker.product = product
        sticker.part = part
    except (KeyError, Cap_group.DoesNotExist):
        return render(request, 'index.html', {"materials": Material.objects.all, 'error_message': 'Option does not exist'})
    else:
        sticker.save()
        return redirect('stickers')

def save_commodity(request, commodity_id):
    if (commodity_id == '0'):
        commodity = Production()
    else:
        commodity = get_object_or_404(Production, pk=commodity_id)
    try:
        product = get_object_or_404(Product, pk=request.POST['product'])
        composition = get_object_or_404(Composition, pk=request.POST['composition'])
        container = get_object_or_404(Container, pk=request.POST['container'])
        cap = get_object_or_404(Cap, pk=request.POST['cap'])
        sticker = get_object_or_404(Sticker, pk=request.POST['sticker'])
        boxing = get_object_or_404(Boxing, pk=request.POST['boxing'])
        commodity.product = product
        commodity.composition = composition
        commodity.container = container
        commodity.cap = cap
        commodity.sticker = sticker
        commodity.boxing = boxing
    except (KeyError, Product.DoesNotExist):
        return render(request, 'index.html', {"materials": Material.objects.all, 'error_message': 'Option does not exist'})
    else:
        commodity.save()
        return redirect('production')

def save_storage(request, storage_id):
    if ('store_type' in request.POST):
        s_type = request.POST['store_type']
    if (storage_id == '0'):
        if (s_type == 'reactor'):
            storage = Reactor()
        else:
            storage = Tank()
    else:
        if (s_type == 'reactor'):
            storage = get_object_or_404(Reactor, pk=storage_id)
        else:
            storage = get_object_or_404(Tank, pk=storage_id)
    if  ('name' in request.POST) & ('code' in request.POST):
        code = request.POST['code']
        name = request.POST['name']
        capacity = request.POST['capacity']
        if 'ready' in request.POST:
            ready = request.POST['ready']
        else:
            ready = False
        storage.ready = ready
        if (s_type == 'reactor'):
            min = request.POST['min']
            max = request.POST['max']
            storage.min = min
            storage.max = max
        storage.code = code
        storage.name = name
        storage.capacity = capacity
        storage.save()
        return redirect('storage')
    else:
        return render(request, 'index.html', {"materials": Material.objects.all, 'error_message': 'Option does not exist'})
