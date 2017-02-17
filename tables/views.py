from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect

from .models import Material_group, Prefix, Unit, Material, Product_group, Product_form, Product_use, Product_mark, Product_option, Product_detail, Product, Composition, Composition_group, Components, Container, Cap, Boxing, Sticker, Production, Reactor, Tank, Container_group, Container_mat, Colour, Container_form, Cap_group, Cap_form, Sticker_part
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


# Create your views here.
