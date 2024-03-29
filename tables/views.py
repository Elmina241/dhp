# -*- coding: utf-8 -*-
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.db.models import deletion

from .models import Set_var, Characteristic_set_var, Characteristic, Char_group, Characteristic_type, Material_group, \
    Prefix, Unit, Material, Product_group, Product_form, Product_use, Product_mark, Product, Composition, \
    Composition_group, Components, Container, Cap, Boxing, Sticker, Production, Reactor, Tank, Container_group, \
    Container_mat, Colour, Cap_group, Sticker_part, Formula_component, Formula
from .models import Characteristic_range, Comp_prop_number, Comp_prop_var, Box_group, Boxing_mat, Material_char, \
    Compl_comp, Compl_comp_comp, Characteristic_number, Composition_char, Comp_char_var, Comp_char_range, \
    Comp_char_number
from .forms import Delete_form
from processes.models import Reactor_content, Tank_content
import json
from django.core import serializers
import xlsxwriter
import io
import base64


def index(request):
    """
    Возвращает страницу со списком реактивов
    """
    return render(request, "materials.html",
                  {"materials": Material.objects.all, "groups": Material_group.objects.all, "header": "Реактивы",
                   "location": "/tables/materials/"})


def products(request):
    """
    Возвращает страницу со списком продуктов
    """
    return render(request, "products.html",
                  {"products": Product.objects.all,
                   "groups": Product_group.objects.all, "header": "Продукция", "location": "/tables/products/"})


def characteristics(request):
    """
    Возвращает страницу с характеристиками
    """
    return render(request, "characteristics.html",
                  {"characteristics": Characteristic.objects.all,
                   "header": "Характеристики", "location": "/tables/characteristics/"})


def new_characteristic(request):
    """
        Возвращает страницу для создания новой характеристики
    """
    return render(request, "new_characteristic.html",
                  {"types": Characteristic_type.objects.all,
                   "groups": Char_group.objects.all,
                   "header": "Добавление характеристики", "location": "/tables/characteristics/"})


def packing2(request):
    """
        Возвращает страницу с тарой
    """
    return render(request, "packing2.html",
                  {"containers": Container.objects.all, "header": "Тара", "location": "/tables/packing/"})


def formulas(request):
    """
        Возвращает страницу с составами
    """
    return render(request, "formulas.html",
                  {"formulas": Formula.objects.all, "header": "Составы", "location": "/tables/formulas/"})


def caps(request):
    """
        Возвращает страницу с укупорками
    """
    return render(request, "caps.html",
                  {"caps": Cap.objects.all, "header": "Укупорка", "location": "/tables/packing/"})


def production(request):
    return render(request, "production.html",
                  {"production": Production.objects.all, "header": "Производство", "location": "/tables/production/"})


def storage(request):
    """
        Возвращает страницу с хранилищами
    """
    return render(request, "storage.html",
                  {"reactors": Reactor.objects.all, "tanks": Tank.objects.all, "header": "Хранилища",
                   "location": "/tables/storage/"})


def boxing(request):
    """
        Возвращает страницу с упаковкой
    """
    return render(request, "boxing.html",
                  {"boxes": Boxing.objects.all, "header": "Упаковка", "location": "/tables/packing/"})


def stickers2(request):
    """
        Возвращает страницу с этикетками
    """
    return render(request, "stickers2.html",
                  {"stickers": Sticker.objects.all, "header": "Этикетка", "location": "/tables/stickers_table/"})


def compositions(request):
    """
        Возвращает страницу с рецептами
    """
    return render(request, "compositions.html",
                  {"compositions": Composition.objects.all, "groups": Composition_group.objects.all,
                   "header": "Рецепты", "location": "/tables/compositions/"})


def comp_chars(request):
    """
        Возвращает страницу с характеристиками композиций
    """
    return render(request, "comp_chars.html",
                  {"compositions": Composition.objects.all, "groups": Composition_group.objects.all,
                   "header": "Характеристики", "location": "/tables/characteristics/"})


def comp_props(request):
    """
        Возвращает страницу с видовыми свойствами
    """
    return render(request, "comp_props.html", {"compositions": Composition.objects.all, "header": "Видовые свойства",
                                               "location": "/tables/comp_props/"})


def mat_chars(request):
    """
        Возвращает страницу с характеристиками реактивов
    """
    return render(request, "mat_chars.html",
                  {"materials": Material.objects.all, "groups": Material_group.objects.all, "header": "Характеристики",
                   "location": "/tables/characteristics/"})


def complex_comps(request):
    """
        Возвращает страницу с технологическими композициями
    """
    return render(request, "complex_comps.html",
                  {"comps": Compl_comp.objects.all, "header": "Технологические композиции",
                   "location": "/tables/complex_comps/"})


def detail(request, material_id):
    """
    Возвращает страницу с детальной информацией о реактиве с id - material_id
    """
    return render(request, "material.html",
                  {"material": get_object_or_404(Material, pk=material_id),
                   "location": "/tables/materials/",
                   "groups": Material_group.objects.all,
                   "header": "Редактирование реактива",
                   "units": Unit.objects.all})


def pr_detail(request, product_id):
    """
    Возвращает страницу с информацией о продукте с id - product_id
    """
    formulas_json = [{
        'pk': f.pk,
        'composition': f.composition.pk,
        'name': f.get_name2(),
        'price': f.price()
    } for f in Formula.objects.all()]
    return render(request, "product.html",
                  {"product": get_object_or_404(Product, pk=product_id),
                   "location": "/tables/products/",
                   "groups": Product_group.objects.all,
                   "formulas": Formula.objects.all,
                   "formulas_json": formulas_json,
                   "forms": Product_form.objects.all,
                   "caps": Cap_group.objects.all,
                   "header": "Редактирование продукта",
                   "containers": Container_group.objects.all,
                   "uses": Product_use.objects.all,
                   "marks": Product_mark.objects.all,
                   "compositions": Composition.objects.all,
                   "containers": Container.objects.all,
                   "caps": Cap.objects.all,
                   "stickers": Sticker.objects.all,
                   "boxing": Boxing.objects.all,
                   "units": Unit.objects.all()})


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
    '''
    Возвращает страницу с информацией о составе с id - formula_id.
    Если formula_id - 0, то возвращает страницу для создания нового состава
    '''
    components = serializers.serialize("json", Components.objects.all())
    materials = serializers.serialize("json", Material.objects.all())
    if (formula_id == '0'):
        return render(request, "formula.html",
                      {"formula": None,
                       "header": "Добавление состава",
                       "components": json.dumps(components),
                       "compositions": Composition.objects.all,
                       "f_components": "0",
                       "materials": json.dumps(materials),
                       "location": "/tables/formulas/"
                       })
    else:
        f_components = serializers.serialize("json", Formula_component.objects.filter(
            formula=get_object_or_404(Formula, pk=formula_id)))
        return render(request, "formula.html",
                      {"formula": get_object_or_404(Formula, pk=formula_id),
                       "components": json.dumps(components),
                       "header": "Редактирование состава",
                       "compositions": Composition.objects.all,
                       "f_components": json.dumps(f_components),
                       "materials": json.dumps(materials),
                       "location": "/tables/formulas/"
                       })


def get_comps(request):
    """
    Возвращает компоненты технологической композиции
    """
    components = {}
    if 'comp_id' in request.POST:
        for c in Compl_comp_comp.objects.filter(compl__pk=request.POST['comp_id']):
            components[c.id] = {'code': c.mat.code, 'name': c.mat.name, 'amount': c.ammount}
    return HttpResponse(json.dumps(components))


def new_comp(request, comp_id):
    components = serializers.serialize("json", Formula_component.objects.all())
    materials = serializers.serialize("json", Material.objects.all())
    formulas = serializers.serialize("json", Formula.objects.all())
    if (comp_id == '0'):
        return render(request, "new_component.html",
                      {"comp": None,
                       "components": json.dumps(components),
                       "compositions": Composition.objects.filter(isFinal=False),
                       "f_components": "0",
                       "materials2": Material.objects.all(),
                       "forms": Product_form.objects.all(),
                       "formulas": json.dumps(formulas),
                       "materials": json.dumps(materials),
                       "location": "/tables/complex_comps/",
                       "header": "Технологические композиции"
                       })
    else:
        f_components = serializers.serialize("json", Formula_component.objects.filter(
            formula=get_object_or_404(Formula, pk=formula_id)))
        return render(request, "formula.html",
                      {"formula": get_object_or_404(Formula, pk=formula_id),
                       "components": json.dumps(components),
                       "compositions": Composition.objects.all,
                       "f_components": json.dumps(f_components),
                       "forms": Product_form.objects.all(),
                       "materials": json.dumps(materials),
                       "location": "/tables/formulas/"
                       })


def characteristic_detail(request, characteristic_id):
    char = get_object_or_404(Characteristic, pk=characteristic_id)
    if (char.char_type.id != 3):
        return render(request, "characteristic.html",
                      {"characteristic": char,
                       "groups": Char_group.objects.all,
                       "location": "/tables/characteristics/",
                       "header": "Редактирование характеристики"
                       })
    else:
        return render(request, "characteristic.html",
                      {"characteristic": char,
                       "groups": Char_group.objects.all,
                       "set_values": Characteristic_set_var.objects.filter(char_set=char),
                       "location": "/tables/characteristics/",
                       "header": "Редактирование характеристики"
                       })


def storage_detail(request):
    return render(request, "edit_storage.html",
                  {"storage": None,
                   "location": "/tables/storage/"
                   })


def comp_char_detail(request, composition_id):
    return render(request, "comp_char.html",
                  {"composition": get_object_or_404(Composition, pk=composition_id),
                   "characteristics": Characteristic.objects.all(),
                   "chars": Composition_char.objects.filter(comp=get_object_or_404(Composition, pk=composition_id)),
                   "location": "/tables/characteristics/",
                   "header": "Редактирование характеристик рецепта"
                   })


def comp_prop_detail(request, composition_id):
    return render(request, "comp_prop.html",
                  {"chars": Composition_char.objects.filter(characteristic__is_general=True,
                                                            comp=get_object_or_404(Composition, pk=composition_id)),
                   # "isTested": isTested,
                   # "isValid": kneading.isValid,
                   # "kneading_chars": Kneading_char.objects.filter(kneading = kneading),
                   "location": "/tables/comp_props/",
                   "comp": get_object_or_404(Composition, pk=composition_id),
                   "header": "Редактирование видовых свойств рецепта"
                   })


def mat_char_detail(request, mat_id):
    return render(request, "mat_char.html",
                  {"material": get_object_or_404(Material, pk=mat_id),
                   "characteristics": Characteristic.objects.all(),
                   "chars": Material_char.objects.filter(mat=get_object_or_404(Material, pk=mat_id)),
                   "location": "/tables/characteristics/"
                   })


def comp_detail(request, composition_id):
    """
    Возвращает страницу с информацией о рецепте с id composition_id
    """
    return render(request, "composition.html",
                  {"comp": get_object_or_404(Composition, pk=composition_id),
                   "groups": Composition_group.objects.all,
                   "location": "/tables/compositions/",
                   "forms": Product_form.objects.all(),
                   "comps": Components.objects.filter(comp=get_object_or_404(Composition, pk=composition_id)),
                   "materials": Material.objects.all(),
                   "header": "Редактирование рецепта"
                   })


def container_detail(request, container_id):
    if (container_id == '0'):
        return render(request, "container.html",
                      {"container": None,
                       "groups": Container_group.objects.all,
                       "colours": Colour.objects.all,
                       "materials": Container_mat.objects.all,
                       "location": "/tables/packing/"
                       })
    else:
        return render(request, "container.html",
                      {"container": get_object_or_404(Container, pk=container_id),
                       "groups": Container_group.objects.all,
                       "colours": Colour.objects.all,
                       "materials": Container_mat.objects.all,
                       "location": "/tables/packing/"
                       })


def cap_detail(request, cap_id):
    if (cap_id == '0'):
        return render(request, "cap.html",
                      {"cap": None,
                       "groups": Cap_group.objects.all,
                       "colours": Colour.objects.all,
                       "materials": Container_mat.objects.all,
                       "location": "/tables/packing/"
                       })
    else:
        return render(request, "cap.html",
                      {"cap": get_object_or_404(Cap, pk=cap_id),
                       "groups": Cap_group.objects.all,
                       "colours": Colour.objects.all,
                       "materials": Container_mat.objects.all,
                       "location": "/tables/packing/"
                       })


def box_detail(request, box_id):
    if (box_id == '0'):
        return render(request, "box.html",
                      {"box": None,
                       "groups": Box_group.objects.all,
                       "colours": Colour.objects.all,
                       "materials": Boxing_mat.objects.all,
                       "location": "/tables/packing/",
                       })
    else:
        return render(request, "box.html",
                      {"box": get_object_or_404(Boxing, pk=box_id),
                       "groups": Box_group.objects.all,
                       "colours": Colour.objects.all,
                       "materials": Boxing_mat.objects.all,
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
    """
    Возвращает страницу для создания нового реактива
    """
    return render(request, "new_material.html",
                  {"groups": Material_group.objects.all,
                   "location": "/tables/materials/",
                   "header": "Добавление реактива",
                   "units": Unit.objects.all})


def new_composition(request):
    """
    Возвращает страницу для создания нового рецепта
    """
    return render(request, "new_composition.html",
                  {"materials": Material.objects.all, "forms": Product_form.objects.all(),
                   "header": "Добавление рецепта", "location": "/tables/compositions/",
                   "groups": Composition_group.objects.all})


def del_material(request):
    """
    Удаляет реактивы с id из списка del_list
    """
    del_var = request.POST.getlist('del_list')
    for d in del_var:
        del_obj = get_object_or_404(Material, pk=d)
        del_obj.delete()
    return redirect('index')


def del_product(request):
    """
    Удаляет продукты с id из del_list
    """
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


def del_comp(request):
    del_var = request.POST.getlist('del_list1')
    for d in del_var:
        del_obj = get_object_or_404(Compl_comp, pk=d)
        del_obj.delete()
    return redirect('complex_comps')


def del_characteristic(request):
    del_var = request.POST.getlist('del_list')
    for d in del_var:
        del_obj = get_object_or_404(Characteristic, pk=d)
        del_obj.delete()
    return redirect('characteristics')


def del_cap(request):
    del_var = request.POST.getlist('del_list')
    for d in del_var:
        del_obj = get_object_or_404(Cap, pk=d)
        del_obj.delete()
    return redirect('caps')


def del_composition(request):
    """
    Удаляет рецепты с id из del_list
    """
    del_var = request.POST.getlist('del_list')
    for d in del_var:
        del_obj = get_object_or_404(Composition, pk=d)
        Components.objects.filter(comp=del_obj).delete()
        del_obj.delete()
    return redirect('compositions')


def del_formula(request):
    del_var = request.POST.getlist('del_list')
    for d in del_var:
        del_obj = get_object_or_404(Formula, pk=d)
        Formula_component.objects.filter(formula=del_obj).delete()
        del_obj.delete()
    return redirect('formulas')


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
    """
    Возвращает страницу для создания нового продукта
    """
    return render(request, "new_product.html",
                  {"groups": Product_group.objects.all,
                   "location": "/tables/products/",
                   "forms": Product_form.objects.all,
                   "uses": Product_use.objects.all,
                   "caps": Cap_group.objects.all,
                   "header": "Добавление продукта",
                   "containers": Container_group.objects.all,
                   "marks": Product_mark.objects.all,
                   "compositions": Composition.objects.all,
                   "containers": Container.objects.all,
                   "caps": Cap.objects.all,
                   "stickers": Sticker.objects.all,
                   "boxing": Boxing.objects.all,
                   "units": Unit.objects.all()})


def add_material(request):
    try:
        code = request.POST['code']
        name = request.POST['name']
        group = get_object_or_404(Material_group, pk=request.POST['group'])
        prefix = get_object_or_404(Prefix, pk=1)
        mark = request.POST['mark']
        unit = get_object_or_404(Unit, pk=request.POST['unit'])
        concentration = request.POST['concentration']
        ammount = request.POST['ammount']
        price = request.POST['price']
        material = Material(code=code,
                            name=name,
                            group=group,
                            prefix=prefix,
                            mark=mark,
                            unit=unit,
                            concentration=concentration,
                            ammount=ammount, price=price)

    except (KeyError, Material_group.DoesNotExist):
        return render(request, 'index.html',
                      {"materials": Material.objects.all, 'error_message': 'Option does not exist'})
    else:
        material.save()
        return redirect('index')


def save_material(request, material_id):
    material = get_object_or_404(Material, pk=material_id)
    try:
        code = request.POST['code']
        name = request.POST['name']
        group = get_object_or_404(Material_group, pk=request.POST['group'])
        prefix = get_object_or_404(Prefix, pk=1)
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
        material.price = request.POST['price']
    except (KeyError, Material_group.DoesNotExist):
        return render(request, 'index.html',
                      {"materials": Material.objects.all, 'error_message': 'Option does not exist'})
    else:
        material.save()
        return redirect('tables:index')


def mat_group(request):
    if 'group1' in request.POST:
        pk = request.POST['group1']
    else:
        pk = 0
    if pk == '-1':
        return redirect('index')
    group = get_object_or_404(Material_group, pk=pk)
    material_group = Material.objects.filter(group=group)
    return render(request, "materials.html",
                  {"materials": material_group, "group": group,
                   "groups": Material_group.objects.all, "header": "Реактивы", "location": "/tables/materials/"})


def pr_group(request):
    if 'group1' in request.POST:
        pk = request.POST['group1']
    else:
        pk = 0
    if pk == '-1':
        return redirect('products')
    group = get_object_or_404(Product_group, pk=pk)
    product_group = Product.objects.filter(group=group)
    return render(request, "products.html",
                  {"products": product_group, "group": group,
                   "groups": Product_group.objects.all, "header": "Продукция", "location": "/tables/products/"})


def comp_group(request):
    if 'group1' in request.POST:
        pk = request.POST['group1']
    else:
        pk = 0
    if pk == '-1':
        return redirect('compositions')
    group = get_object_or_404(Composition_group, pk=pk)
    comp_group = Composition.objects.filter(group=group)
    return render(request, "compositions.html",
                  {"compositions": comp_group, "group": group,
                   "groups": Composition_group.objects.all, "header": "Составы", "location": "/tables/compositions/"})


def save_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    try:
        commodity = Production() if product.production is None else product.production
        composition = get_object_or_404(Composition, pk=request.POST['composition'])
        container = get_object_or_404(Container, pk=request.POST['container'])
        cap = get_object_or_404(Cap, pk=request.POST['cap'])
        sticker = get_object_or_404(Sticker, pk=request.POST['sticker'])
        boxing = get_object_or_404(Boxing, pk=request.POST['boxing'])
        commodity.composition = composition
        commodity.container = container
        commodity.cap = cap
        commodity.sticker = sticker
        commodity.boxing = boxing
        commodity.compAmount = request.POST['compAmount']
        commodity.contAmount = request.POST['contAmount']
        commodity.capAmount = request.POST['capAmount']
        commodity.stickerAmount = request.POST['stickerAmount']
        commodity.boxingAmount = request.POST['boxingAmount']
        commodity.compUnit = get_object_or_404(Unit, pk=request.POST['compUnit'])
        commodity.contUnit = get_object_or_404(Unit, pk=request.POST['contUnit'])
        commodity.capUnit = get_object_or_404(Unit, pk=request.POST['capUnit'])
        commodity.stickerUnit = get_object_or_404(Unit, pk=request.POST['stickerUnit'])
        commodity.boxingUnit = get_object_or_404(Unit, pk=request.POST['boxingUnit'])
        commodity.formula = get_object_or_404(Formula, pk=request.POST['formula'])
        commodity.save()
        code = request.POST['code']
        name = request.POST['name']
        group = get_object_or_404(Product_group, pk=request.POST['group'])
        use = get_object_or_404(Product_use, pk=request.POST['use'])
        option = request.POST['option']
        detail = request.POST['detail']
        mark = get_object_or_404(Product_mark, pk=request.POST['mark'])
        product.code = code
        product.name = name
        product.group = group
        product.use = use
        product.option = option
        product.detail = detail
        product.mark = mark
        product.production = commodity
    except (KeyError, Material_group.DoesNotExist):
        return render(request, 'products.html',
                      {"materials": Material.objects.all, 'error_message': 'Option does not exist'})
    else:
        product.save()
        return redirect("products")


def add_product(request):
    try:
        commodity = Production()
        composition = get_object_or_404(Composition, pk=request.POST['composition'])
        container = get_object_or_404(Container, pk=request.POST['container'])
        cap = get_object_or_404(Cap, pk=request.POST['cap'])
        sticker = get_object_or_404(Sticker, pk=request.POST['sticker'])
        boxing = get_object_or_404(Boxing, pk=request.POST['boxing'])
        commodity.composition = composition
        commodity.container = container
        commodity.cap = cap
        commodity.sticker = sticker
        commodity.boxing = boxing
        commodity.compAmount = request.POST['compAmount']
        commodity.contAmount = request.POST['contAmount']
        commodity.capAmount = request.POST['capAmount']
        commodity.stickerAmount = request.POST['stickerAmount']
        commodity.boxingAmount = request.POST['boxingAmount']
        commodity.compUnit = get_object_or_404(Unit, pk=request.POST['compUnit'])
        commodity.contUnit = get_object_or_404(Unit, pk=request.POST['contUnit'])
        commodity.capUnit = get_object_or_404(Unit, pk=request.POST['capUnit'])
        commodity.stickerUnit = get_object_or_404(Unit, pk=request.POST['stickerUnit'])
        commodity.boxingUnit = get_object_or_404(Unit, pk=request.POST['boxingUnit'])
        commodity.save()
        code = request.POST['code']
        name = request.POST['name']
        group = get_object_or_404(Product_group, pk=request.POST['group'])
        use = get_object_or_404(Product_use, pk=request.POST['use'])
        option = request.POST['option']
        detail = request.POST['detail']
        mark = get_object_or_404(Product_mark, pk=request.POST['mark'])
        product = Product(
            code=code,
            name=name,
            group=group,
            use=use,
            option=option,
            detail=detail,
            mark=mark,
            production=commodity)

    except (KeyError, Material_group.DoesNotExist):
        return render(request, 'index.html',
                      {"materials": Material.objects.all, 'error_message': 'Option does not exist'})
    else:
        product.save()
        return redirect('products')


def add_composition(request):
    """
    Сохраняет новый рецепт
    """
    try:
        code = request.POST['code']
        name = request.POST['name']
        group = get_object_or_404(Composition_group, pk=request.POST['group'])
        sgr = request.POST['sgr']
        isFinal = True
        if 'isFinal' in request.POST:
            if request.POST['isFinal'] == 'on':
                isFinal = False
            else:
                isFinal = True
        comp = Composition(
            code=code,
            name=name,
            group=group,
            form=get_object_or_404(Product_form, pk=request.POST['form']),
            sgr=sgr,
            isFinal=isFinal)
    except (KeyError, Composition_group.DoesNotExist):
        return render(request, 'index.html',
                      {"materials": Material.objects.all, 'error_message': 'Option does not exist'})
    else:
        comp.save()
        if 'json' in request.POST:
            table = request.POST['json']
            data = json.loads(table)
            for d in data:
                mat = Material.objects.filter(code=d['Код'])[0]
                cmps = Components(comp=comp, mat=mat, min=d["Минимум чистого реактива"],
                                  max=d["Максимум чистого реактива"])
                cmps.save()

        return redirect('compositions')


def add_characteristic(request):
    try:
        name = request.POST['name']
        group = get_object_or_404(Char_group, pk=request.POST['group'])
        type = get_object_or_404(Characteristic_type, pk=request.POST['type'])
        is_general = False
        if 'is_general' in request.POST:
            if request.POST['is_general'] == 'on':
                is_general = True
            else:
                is_general = False
    except (KeyError, Char_group.DoesNotExist):
        return render(request, 'index.html',
                      {"materials": Material.objects.all, 'error_message': 'Option does not exist'})
    else:
        if type.id == 1:
            char = Characteristic_range(name=name, group=group, char_type=type, inf=request.POST['from'],
                                        sup=request.POST['to'], is_general=is_general)
            char.save()
        if type.id == 2:
            char = Characteristic_number(name=name, group=group, char_type=type, inf=request.POST['from'],
                                         sup=request.POST['to'], is_general=is_general)
            char.save()
        if type.id == 3:
            char = Characteristic(name=name, group=group, char_type=type, is_general=is_general)
            char.save()
            # if 'json' in request.POST:
            table = request.POST['json']
            data = json.loads(table)
            for d in data:
                set_var = Set_var(name=d['Значение'])
                set_var.save()
                characteristic_set_var = Characteristic_set_var(char_set=char, char_var=set_var)
                characteristic_set_var.save()
        return redirect('characteristics')


def save_characteristic(request, characteristic_id):
    try:
        name = request.POST['name']
        group = get_object_or_404(Char_group, pk=request.POST['group'])
        type = get_object_or_404(Characteristic_type, pk=request.POST['type'])
        is_general = False
        if 'is_general' in request.POST:
            if request.POST['is_general'] == 'on':
                is_general = True
            else:
                is_general = False
    except (KeyError, Char_group.DoesNotExist):
        return render(request, 'index.html',
                      {"materials": Material.objects.all, 'error_message': 'Option does not exist'})
    else:
        if type.id == 1:
            char = get_object_or_404(Characteristic_range, pk=characteristic_id)
            char.name = name
            char.group = group
            char.char_type = type
            char.is_general = is_general
            char.inf = request.POST['from']
            char.sup = request.POST['to']
            char.save()
        if type.id == 2:
            char = get_object_or_404(Characteristic_number, pk=characteristic_id)
            char.name = name
            char.group = group
            char.char_type = type
            char.is_general = is_general
            char.inf = request.POST['from']
            char.sup = request.POST['to']
            char.save()
        if type.id == 3:
            char = get_object_or_404(Characteristic, pk=characteristic_id)
            char.name = name
            char.group = group
            char.char_type = type
            char.is_general = is_general
            char.save()
            # if 'json' in request.POST:
            table = request.POST['json']
            data = json.loads(table)
            Characteristic_set_var.objects.filter(char_set=char).delete()
            for d in data:
                set_var = Set_var(name=d['Значение'])
                set_var.save()
                characteristic_set_var = Characteristic_set_var(char_set=char, char_var=set_var)
                characteristic_set_var.save()
        return redirect('characteristics')


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
        comp.form = get_object_or_404(Product_form, pk=request.POST['form'])
    except (KeyError, Composition_group.DoesNotExist):
        return render(request, 'index.html',
                      {"materials": Material.objects.all, 'error_message': 'Option does not exist'})
    else:
        comp.save()
        Components.objects.filter(comp=comp).delete()
        if 'json' in request.POST:
            table = request.POST['json']
            data = json.loads(table)
            for d in data:
                mat = Material.objects.filter(code=d['Код'])[0]
                cmps = Components(comp=comp, mat=mat, min=d["Минимум чистого реактива"],
                                  max=d["Максимум чистого реактива"])
                cmps.save()
        for f in Formula.objects.filter(composition=comp):
            for c in Formula_component.objects.filter(formula=f):
                if Components.objects.filter(comp=comp, mat=c.mat).count() == 0:
                    c.delete()
            for c1 in Components.objects.filter(comp=comp):
                if Formula_component.objects.filter(formula=f, mat=c.mat).count() == 0:
                    f_c = Formula_component(formula=f, mat=c.mat, ammount=0)
                    f_c.save()
        return redirect('compositions')


def save_container(request, container_id):
    if (container_id == '0'):
        container = Container()
    else:
        container = get_object_or_404(Container, pk=container_id)
    try:
        code = request.POST['code']
        group = get_object_or_404(Container_group, pk=request.POST['group'])
        form = request.POST['form']
        colour = get_object_or_404(Colour, pk=request.POST['colour'])
        mat = get_object_or_404(Container_mat, pk=request.POST['container_mat'])
        container.code = code
        container.group = group
        container.form = form
        container.colour = colour
        container.mat = mat
        container.price = request.POST['price']
    except (KeyError, Container_group.DoesNotExist):
        return render(request, 'index.html',
                      {"materials": Material.objects.all, 'error_message': 'Option does not exist'})
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
        form = request.POST['form']
        colour = get_object_or_404(Colour, pk=request.POST['colour'])
        mat = get_object_or_404(Container_mat, pk=request.POST['container_mat'])
        cap.code = code
        cap.group = group
        cap.form = form
        cap.colour = colour
        cap.mat = mat
        cap.price = request.POST['price']
    except (KeyError, Cap_group.DoesNotExist):
        return render(request, 'index.html',
                      {"materials": Material.objects.all, 'error_message': 'Option does not exist'})
    else:
        cap.save()
        return redirect('caps')


def save_box(request, box_id):
    if (box_id == '0'):
        box = Boxing()
    else:
        box = get_object_or_404(Boxing, pk=box_id)
    if 'code' in request.POST:
        group = get_object_or_404(Box_group, pk=request.POST['group'])
        form = request.POST['form']
        colour = get_object_or_404(Colour, pk=request.POST['colour'])
        mat = get_object_or_404(Boxing_mat, pk=request.POST['boxing_mat'])
        code = request.POST['code']
        box.code = code
        box.group = group
        box.form = form
        box.colour = colour
        box.mat = mat
        box.price = request.POST['price']
        box.save()
        return redirect('boxing')
    else:
        return render(request, 'index.html',
                      {"materials": Material.objects.all, 'error_message': 'Option does not exist'})


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
        sticker.price = request.POST['price']
    except (KeyError, Cap_group.DoesNotExist):
        return render(request, 'index.html',
                      {"materials": Material.objects.all, 'error_message': 'Option does not exist'})
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
        return render(request, 'index.html',
                      {"materials": Material.objects.all, 'error_message': 'Option does not exist'})
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
    if ('name' in request.POST) & ('code' in request.POST):
        code = request.POST['code']
        name = request.POST['name']
        # capacity = request.POST['capacity']
        if 'ready' in request.POST:
            ready = request.POST['ready']
        else:
            ready = False
        storage.ready = ready
        if (s_type == 'reactor'):
            product = request.POST['product']
            location = request.POST['location']
            min = request.POST['min']
            max = request.POST['max']
            storage.product = product
            storage.location = location
            storage.min = min
            storage.max = max
        else:
            storage.capacity = request.POST['capacity']
        storage.code = code
        storage.name = name
        # storage.capacity = capacity
        storage.save()
        if (storage_id == '0'):
            if (s_type == 'reactor'):
                r_c = Reactor_content(reactor=storage, amount=0)
                r_c.save()
            else:
                t_c = Tank_content(tank=storage, amount=0)
                t_c.save()
        return redirect('storage')
    else:
        return render(request, 'index.html',
                      {"materials": Material.objects.all, 'error_message': 'Option does not exist'})


# количество компонентов сохраняется на норму веса (1020кг)
def save_formula(request, formula_id):
    if (formula_id == '0'):
        formula = Formula()
    else:
        formula = get_object_or_404(Formula, pk=formula_id)
    try:
        if 'code' in request.POST:
            formula.code = request.POST['code']
            formula.name = request.POST['name']
            composition = get_object_or_404(Composition, pk=request.POST['composition'])
            formula.composition = composition
    except (KeyError, Formula.DoesNotExist):
        return render(request, 'index.html', {'error_message': 'Option does not exist'})
    else:
        formula.save()
        Formula_component.objects.filter(formula=formula).delete()
        if 'json' in request.POST:
            table = request.POST['json']
            data = json.loads(table)
            for d in data:
                mat = Material.objects.filter(code=d['Код'])[0]
                if d['Код'] in request.POST:
                    ammount = (float(request.POST[d['Код']]) / 100) * 1020
                    print(float(request.POST[d['Код']]) / 100)
                    print(str(mat) + '-' + str(ammount) + "-" + str(float(request.POST[d['Код']])))
                    cmps = Formula_component(formula=formula, mat=mat, ammount=ammount)
                    cmps.save()
        return redirect('formulas')


def save_comp(request):
    comp = Compl_comp()
    # if ('comp_type' in request.POST):
    # c_type = request.POST['comp_type']
    if 'code' in request.POST:
        # c_type = request.POST['comp_type']
        comp.code = request.POST['code']
        comp.name = request.POST['name']
        comp.ammount = request.POST['ammount']
        comp.store_amount = request.POST['ammount']
        # if 'form' in request.POST:
        # comp.form = get_object_or_404(Product_form, pk=request.POST['form'])
        formula = Formula.objects.filter(pk=request.POST['formula'])[0]
        comp.formula = formula
    comp.save()
    if 'json' in request.POST:
        table = request.POST['json']
        data = json.loads(table)
        for d in data:
            mat = Material.objects.filter(code=d['Код'])[0]
            # Содержание компонентов сохраняется в %
            # if d['Код'] in request.POST:
            if d['Код'] != 'ВД01':
                ammount = float(d['%'])
                cmps = Compl_comp_comp(compl=comp, mat=mat, ammount=ammount)
                cmps.save()
        return redirect('complex_comps')


def get_char(request, composition_id):
    if request.method == 'POST':
        if 'char_id' in request.POST:
            char = Characteristic.objects.filter(pk=request.POST['char_id'])
            data = {}
            data['char'] = serializers.serialize("json", char)
            # data['char_val'] = {}
            if (char[0].char_type.id == 1):
                data['char_val'] = serializers.serialize("json", [char[0].characteristic_range])
            if (char[0].char_type.id == 2):
                data['char_val'] = serializers.serialize("json", [char[0].characteristic_number])
            if (char[0].char_type.id == 3):
                char_val = {}
                vals = Characteristic_set_var.objects.filter(char_set=char)
                length = Characteristic_set_var.objects.filter(char_set=char).count()
                for i in range(0, length):
                    char_val[str(vals[i].char_var.id)] = vals[i].char_var.name
                data['char_val'] = char_val
            json_data = json.dumps(data)
            return HttpResponse(json_data)


def get_elems(request, composition_id):
    if request.method == 'POST':
        if 'char_id' in request.POST:
            char = get_object_or_404(Composition_char, pk=request.POST['char_id'])
            data = {}
            vars = {}
            checked = {}
            all_var = Characteristic_set_var.objects.filter(char_set=char.characteristic)
            length = Characteristic_set_var.objects.filter(char_set=char.characteristic).count()
            for i in range(0, length):
                vars[str(all_var[i].char_var.id)] = all_var[i].char_var.name
            checked_var = Comp_char_var.objects.filter(comp_char=char)
            length = Comp_char_var.objects.filter(comp_char=char).count()
            for i in range(0, length):
                checked[str(checked_var[i].char_var.id)] = checked_var[i].char_var.name
            data['vars'] = vars
            data['checked'] = checked
            json_data = json.dumps(data)
            return HttpResponse(json_data)


def save_mat_char(request, mat_id):
    mat = get_object_or_404(Material, pk=mat_id)
    Material_char.objects.filter(mat=mat).delete()
    if 'json' in request.POST:
        chars = request.POST['json']
        data = json.loads(chars)
        for d in data:
            char = get_object_or_404(Characteristic, pk=d)
            m_char = Material_char(mat=mat, characteristic=char)
            m_char.save()
        return redirect('characteristics')


def save_comp_char(request, composition_id):
    comp = get_object_or_404(Composition, pk=composition_id)
    if 'json' in request.POST:
        chars = request.POST['json']
        data = json.loads(chars)
        for c in Composition_char.objects.filter(comp=comp):
            if str(c.characteristic.pk) not in data:
                c.delete()
        for d in data:
            char = get_object_or_404(Characteristic, pk=d)
            if (char.char_type.id == 1):
                if (str(char.id) + "'from'") in request.POST:
                    if Composition_char.objects.filter(comp=comp, characteristic=char).exists():
                        comp_char = Composition_char.objects.filter(comp=comp, characteristic=char).first()
                        comp_char.inf = request.POST[str(char.id) + "'from'"]
                        comp_char.sup = request.POST[str(char.id) + "'to'"]
                    else:
                        comp_char = Comp_char_range(comp=comp, characteristic=char,
                                                inf=request.POST[str(char.id) + "'from'"],
                                                sup=request.POST[str(char.id) + "'to'"])
                    comp_char.save()
            if (char.char_type.id == 2):
                if str(char.id) in request.POST:
                    if Composition_char.objects.filter(comp=comp, characteristic=char).exists():
                        comp_char = Composition_char.objects.filter(comp=comp, characteristic=char)
                        comp_char.number = request.POST[str(char.id)]
                    else:
                        comp_char = Comp_char_number(comp=comp, characteristic=char, number=request.POST[str(char.id)])
                    comp_char.save()
            if (char.char_type.id == 3):
                if (str(char.id) + "'checked_list'") in request.POST:
                    char_var = request.POST.getlist(str(char.id) + "'checked_list'")
                    if Composition_char.objects.filter(comp=comp, characteristic=char).exists():
                        char = Composition_char.objects.filter(comp=comp, characteristic=char).first()
                        for ch in Comp_char_var.objects.filter(comp_char=char):
                            if str(ch.char_var.pk) not in char_var:
                                ch.delete()
                    else:
                        char = Composition_char(comp=comp, characteristic=char)
                        char.save()
                    for c in char_var:
                        set_var = get_object_or_404(Set_var, pk=c)
                        if Comp_char_var.objects.filter(comp_char=char, char_var=set_var).count() == 0:
                            сomp_char_var = Comp_char_var(comp_char=char, char_var=set_var)
                            сomp_char_var.save()
        return redirect('characteristics')


def save_comp_prop(request, composition_id):
    comp = get_object_or_404(Composition, pk=composition_id)
    Comp_prop_var.objects.filter(comp_prop__comp=comp).delete()
    numbers = Comp_prop_number.objects.filter(comp=comp)
    temp = Composition_char(comp=comp, characteristic=Characteristic.objects.all()[0])
    temp.save()
    for n in numbers:
        n.composition_char = temp
        n.save()
    temp.delete()
    chars = Composition_char.objects.filter(comp=comp)
    isValid = True
    for char in chars:
        if (char.characteristic.char_type.id != 3):
            if str(char.characteristic.id) in request.POST:
                char.comp_prop_number = Comp_prop_number(comp=char.comp, characteristic=char.characteristic,
                                                         number=request.POST[str(char.characteristic.id)])
                char.comp_prop_number.save()
                # comp_char = Comp_prop_number(char, number = request.POST[str(char.characteristic.id)])
                # comp_char.save()
                # Проверка на соответсвие показателям
                # comp_char = Composition_char.objects.filter(comp = kneading.list.formula.composition, characteristic = char.characteristic)[0]
                # if (char.characteristic.char_type.id == 1):
                # range = Comp_char_range.objects.filter(comp = kneading.list.formula.composition, characteristic = char.characteristic)[0]
                # isValid = isValid & ((float(kneading_char.number) <= float(range.sup)) & (float(kneading_char.number) >= float(range.inf)))
                # if (char.characteristic.char_type.id == 2):
                # isValid = isValid & (kneading_char.number == comp_char.сomp_char_number.number)
        else:
            if (str(char.characteristic.id) + "checked") in request.POST:
                char_var = request.POST.getlist(str(char.characteristic.id) + "checked")
                for v in char_var:
                    set_var = get_object_or_404(Set_var, pk=v)
                    prop_var = Comp_prop_var(comp_prop=char, char_var=set_var)
                    prop_var.save()
                # Проверка на соответсвие показателям
                # comp_char = Composition_char.objects.filter(comp_prop = char, char_var = char)[0]
                # isValid = isValid & (Comp_char_var.objects.filter(comp_char = comp_char, char_var = set_var).count() != 0)
    # kneading.isTested = True
    # kneading.isValid = isValid
    # kneading.save()
    return redirect('comp_props')


def get_checked_elems(request, composition_id):
    if request.method == 'POST':
        if 'char_id' in request.POST:
            char = get_object_or_404(Composition_char, pk=request.POST['char_id'])
            data = {}
            vars = {}
            checked = {}
            all_var = Characteristic_set_var.objects.filter(char_set=char.characteristic)
            length = Characteristic_set_var.objects.filter(char_set=char.characteristic).count()
            for i in range(0, length):
                vars[str(all_var[i].char_var.id)] = all_var[i].char_var.name
            checked_var = Comp_prop_var.objects.filter(comp_prop=char)
            # length = Comp_char_var.objects.filter(comp_char = char).count()
            # for i in range(0, length):
            if Comp_prop_var.objects.filter(comp_prop=char).count() != 0:
                checked[str(checked_var[0].char_var.id)] = checked_var[0].char_var.name
                data['checked'] = checked
            data['vars'] = vars
            json_data = json.dumps(data)
            return HttpResponse(json_data)


def add_matAm(request):
    if request.method == 'POST':
        if 'mat_id' in request.POST:
            mat = Material.objects.filter(pk=request.POST['mat_id'])[0]
            mat.ammount = request.POST['amm']
            mat.save()
            return HttpResponse("ok")


def add_compAm(request):
    if request.method == 'POST':
        if 'comp_id' in request.POST:
            comp = Compl_comp.objects.filter(pk=request.POST['comp_id'])[0]
            comp.store_amount = request.POST['amm']
            comp.save()
            return HttpResponse("ok")

def get_excel_product(request):
    products = Product.objects.all()
    output = io.BytesIO()
    workbook = xlsxwriter.Workbook(output)
    worksheet = workbook.add_worksheet()

    merge_format = workbook.add_format({
        'align': 'center',
        'valign': 'vcenter',
        'text_wrap': True
    })
    merge_header_format = workbook.add_format({
        'align': 'center',
        'valign': 'vcenter',
        'text_wrap': True,
        'bold': 2
    })
    border_format = workbook.add_format({
        'border': 1,
        'border_color': '#d7d7d7'
    })

    worksheet.write('A1', 'Код', merge_header_format)
    worksheet.write('B1', 'Наименование',merge_header_format)
    worksheet.write('C1', 'Группа', merge_header_format)
    worksheet.write('D1', 'Комплект', merge_header_format)
    worksheet.write('E1', 'Кол-во', merge_header_format)
    worksheet.write('F1', 'Цена', merge_header_format)

    worksheet.set_column(1, 1, 60)
    worksheet.set_column(2, 2, 30)
    worksheet.set_column(3, 3, 60)
    cur_row = 2
    for p in products:
        worksheet.merge_range('A'+str(cur_row) + ':A' + str(cur_row+4), p.code, merge_format)
        worksheet.merge_range('B'+str(cur_row) + ':B' + str(cur_row+4), str(p), merge_format)
        worksheet.merge_range('C'+str(cur_row) + ':C' + str(cur_row+4), str(p.group), merge_format)
        worksheet.write('D' + str(cur_row), str(p.production.composition))
        worksheet.write('E' + str(cur_row), str(p.production.compAmount))
        worksheet.write('F' + str(cur_row), str(round(p.production.compAmount * p.production.composition.min_price()/100, 2)) + '-' + str(round(p.production.compAmount * p.production.composition.max_price()/100, 2)))

        worksheet.write('D' + str(cur_row + 1), str(p.production.container))
        worksheet.write('E' + str(cur_row + 1), str(p.production.compAmount))
        worksheet.write('F' + str(cur_row + 1), str(round(p.production.contAmount * p.production.container.price, 2)))

        worksheet.write('D' + str(cur_row + 2), str(p.production.cap))
        worksheet.write('E' + str(cur_row + 2), str(p.production.capAmount))
        worksheet.write('F' + str(cur_row + 2), str(round(p.production.capAmount * p.production.cap.price, 2)))

        worksheet.write('D' + str(cur_row + 3), str(p.production.sticker))
        worksheet.write('E' + str(cur_row + 3), str(p.production.stickerAmount))
        worksheet.write('F' + str(cur_row + 3), str(round(p.production.stickerAmount * p.production.sticker.price, 2)))

        worksheet.write('D' + str(cur_row + 4), str(p.production.boxing))
        worksheet.write('E' + str(cur_row + 4), str(p.production.boxingAmount))
        worksheet.write('F' + str(cur_row + 4), str(round(p.production.boxingAmount * p.production.boxing.price, 2)))

        cur_row = cur_row + 5

    workbook.close()
    # Rewind the buffer.
    output.seek(0)
    # Set up the Http response.
    filename = 'products.xlsx'
    response = HttpResponse(
        base64.b64encode(output.getvalue()).decode(),
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = 'attachment; filename=%s' % filename
    return response
