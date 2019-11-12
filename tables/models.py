# -*- coding: utf-8 -*-
from django.db import models


# Модели для химвеществ
class Material_group(models.Model):
    name = models.CharField(max_length=200, verbose_name="Наименование")
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Группы реактивов"
        verbose_name = "Группа реактива"

class Prefix(models.Model):
    name = models.CharField(max_length=200, verbose_name="Наименование")
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Префиксы"
        verbose_name = "Префикс"

class Unit(models.Model):
    name = models.CharField(max_length=80, verbose_name="Наименование")
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Единицы измерения"
        verbose_name = "Единица измерения"

class Material(models.Model):
    code = models.CharField(max_length=80, verbose_name="Артикул")
    name = models.CharField(max_length=80, verbose_name="Наименование")
    group = models.ForeignKey('Material_group', on_delete=models.CASCADE, verbose_name="Группа")
    prefix = models.ForeignKey('Prefix', on_delete=models.CASCADE, verbose_name="Префикс")
    mark = models.CharField(max_length=80, verbose_name="Марка")
    ammount = models.FloatField(verbose_name="Количество")
    reserved = models.FloatField(default = 0, verbose_name="Зарезервировано")
    unit = models.ForeignKey('Unit', on_delete=models.CASCADE, verbose_name="Ед. изм.")
    concentration = models.FloatField(verbose_name="Концентрация")
    price = models.FloatField(verbose_name="Цена")
    def __str__(self):
        full_name = self.name + ('' if self.mark == '-' else (' ' + self.mark))
        return full_name
    def get_name(self):
        full_name = self.code + " " + self.name
        return full_name
    def get_full_name(self):
        full_name = self.name + ('' if self.mark == '-' else (' ' + self.mark))
        full_name = self.code + " " + full_name
        return full_name
    class Meta:
        verbose_name_plural = "Реактивы"
        verbose_name = "Реактив"


# Модели для продукции
class Product_group(models.Model):
    name = models.CharField(max_length=200, verbose_name="Наименование")
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Группы продукции"
        verbose_name = "Группа продукции"

class Product_form(models.Model):
    name = models.CharField(max_length=200, verbose_name="Наименование")
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Формы продукции"
        verbose_name = "Форма продукции"

class Product_use(models.Model):
    name = models.CharField(max_length=200, verbose_name="Наименование")
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Назначения продукции"
        verbose_name = "Назначение продукции"

class Product_mark(models.Model):
    name = models.CharField(max_length=200, verbose_name="Наименование")
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Марки продукции"
        verbose_name = "Марка продукции"

class Product(models.Model):
    code = models.CharField(max_length=13, verbose_name="Артикул")
    name = models.CharField(max_length=80, verbose_name="Наименование")
    group = models.ForeignKey('Product_group', on_delete=models.CASCADE, verbose_name="Группа")
    use = models.ForeignKey('Product_use', on_delete=models.CASCADE, verbose_name="Назначение")
    option = models.CharField(max_length=80, verbose_name="Варианты")
    detail = models.CharField(max_length=80, verbose_name="Уточнение")
    mark = models.ForeignKey('Product_mark', on_delete=models.CASCADE, verbose_name="Марка")
    production = models.OneToOneField('Production', null=True, on_delete=models.CASCADE, verbose_name="Комплект")
    def __str__(self):
        opt = ' (' + self.mark.name + ', ' + ('' if self.production is None else (self.production.container.mat.name + " " + self.production.container.group.name + ', ')) + ('' if self.production is None else (self.production.cap.group.name + ', ')) + ('0' if self.production is None else str(self.production.compAmount)) + ' кг.' + ')'
        full_name =  ('' if self.production is None or self.production.composition.form is None else self.production.composition.form.name) + ' ' + self.use.name + ' ' + ('' if self.option == 'отсутствует' else (self.option + ' ')) + ('' if self.detail == 'отсутствует' else self.detail) + opt
        return full_name
    def get_short_code(self):
        return self.code[9:]
    def get_short_name(self):
        return ('' if self.production is None or self.production.composition.form is None else self.production.composition.form.name) + ' ' + self.use.name + ' ' + ('' if self.option == 'отсутствует' else (self.option + ' ')) + ('' if self.detail == 'отсутствует' else self.detail)
    def get_name_for_table(self):
        return self.name + ' ' + self.mark.name + ' ' + ('' if self.option == 'отсутствует' else (self.option + ' '))
    class Meta:
        verbose_name_plural = "Продукция"
        verbose_name = "Продукция"

#Модели для рецептов

class Composition_group(models.Model):
    name = models.CharField(max_length=80, verbose_name="Наименование")
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Группы рецептов"
        verbose_name = "Группа рецептов"

class Composition(models.Model):
    code = models.CharField(max_length=80, verbose_name="Код")
    name = models.CharField(max_length=80, verbose_name="Наименование")
    sgr = models.CharField(max_length=80, verbose_name="СГР")
    sh_life = models.IntegerField(default = 24, verbose_name="Срок годности")
    date = models.DateField(null = True, verbose_name="Дата СГР")
    package = models.CharField(max_length=80, null = True, verbose_name="Упаковка")
    standard = models.CharField(max_length=80, null = True, verbose_name="Стандарт")
    certificate = models.CharField(max_length=80, null = True, verbose_name="Свидетельство о гос. регистрации")
    declaration = models.CharField(max_length=80, null = True, verbose_name="Требования качества продукции")
    cur_batch = models.FloatField(default = 1, verbose_name="Текущий номер партии")
    group = models.ForeignKey('Composition_group', on_delete=models.CASCADE, verbose_name="Группа")
    form = models.ForeignKey('Product_form', null=True, on_delete=models.CASCADE, verbose_name="Форма")
    isFinal = models.BooleanField(default = True, verbose_name="Не технологическая?")
    def __str__(self):
        return self.name
    def get_name(self):
        return self.code + " " + self.name
    def get_package(self):
        res = self.package + " по "
        prods = Production.objects.filter(composition = self)
        amms = set()
        for p in prods:
            if p.compAmount != 0:
                amms.add(str(int(p.compAmount * 1000)))
        length = len(amms)
        for i in range(length):
            res = res + amms.pop()
            if len(amms) != 0:
                res = res + " или "
            else:
                res = res + " г"
        return res
    def get_package_pass(self):
        res = self.package + " по "
        prods = Production.objects.filter(composition = self)
        amms = set()
        for p in prods:
            if p.compAmount != 0 and p.compAmount != 5:
                amms.add(str(int(p.compAmount * 1000)))
        length = len(amms)
        for i in range(length):
            res = res + amms.pop()
            if len(amms) != 0:
                res = res + " или "
            else:
                res = res + " г"
        return res
    class Meta:
        verbose_name_plural = "Рецепты"
        verbose_name = "Рецепт"


class Components(models.Model):
    comp = models.ForeignKey('Composition', on_delete=models.CASCADE, verbose_name="Рецепт")
    mat = models.ForeignKey('Material', on_delete=models.CASCADE, verbose_name="Реактив")
    min = models.FloatField(verbose_name="Мин. %")
    max = models.FloatField(verbose_name="Макс. %")
    class Meta:
        verbose_name_plural = "Компоненты рецептов"
        verbose_name = "Компонент рецепта"

#Модели для тары

class Container_group(models.Model):
    name = models.CharField(max_length=80, verbose_name="Наименование")
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Группы тары"
        verbose_name = "Группа тары"

class Colour(models.Model):
    name = models.CharField(max_length=80, verbose_name="Наименование")
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Цвета"
        verbose_name = "Цвет"

class Container_mat(models.Model):
    name = models.CharField(max_length=80, verbose_name="Наименование")
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Материалы тары"
        verbose_name = "Материал тары"

class Container(models.Model):
    code = models.CharField(max_length=80, verbose_name="Наименование")
    group = models.ForeignKey('Container_group', on_delete=models.CASCADE, verbose_name="Группа")
    form = models.CharField(max_length=80, verbose_name="Форма")
    colour = models.ForeignKey('Colour', on_delete=models.CASCADE, verbose_name="Цвет")
    mat = models.ForeignKey('Container_mat', on_delete=models.CASCADE, verbose_name="Материал")
    def __str__(self):
        return 'Нет' if self.code == 'Т000' else self.group.name + " " + self.form + " " + self.mat.name + " " + self.colour.name
    class Meta:
        verbose_name_plural = "Тара"
        verbose_name = "Тара"

#Модели для укупорки

class Cap_group(models.Model):
    name = models.CharField(max_length=80, verbose_name="Наименование")
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Группы укупорки"
        verbose_name = "Группа укупорки"

class Cap(models.Model):
    code = models.CharField(max_length=80, verbose_name="Наименование")
    group = models.ForeignKey('Cap_group', on_delete=models.CASCADE, verbose_name="Группа")
    form = models.CharField(max_length=80, verbose_name="Форма")
    colour = models.ForeignKey('Colour', on_delete=models.CASCADE, verbose_name="Цвет")
    mat = models.ForeignKey('Container_mat', on_delete=models.CASCADE, verbose_name="Материал")
    def __str__(self):
        return 'Нет' if self.code == 'У000' else self.group.name + " " + self.form + " " + self.mat.name + " " + self.colour.name
    class Meta:
        verbose_name_plural = "Укупорка"
        verbose_name = "Укупорка"

#Модели для упаковки

class Box_group(models.Model):
    name = models.CharField(max_length=80, verbose_name="Наименование")
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Группы реактивов"
        verbose_name = "Группа реактива"

class Boxing_mat(models.Model):
    name = models.CharField(max_length=80, verbose_name="Наименование")
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Группы реактивов"
        verbose_name = "Группа реактива"

class Boxing(models.Model):
    code = models.CharField(max_length=80, verbose_name="Наименование")
    group = models.ForeignKey('Box_group', null=True, on_delete=models.CASCADE, verbose_name="Наименование")
    form = models.CharField(max_length=80, verbose_name="Наименование")
    colour = models.ForeignKey('Colour', null=True, on_delete=models.CASCADE, verbose_name="Наименование")
    mat = models.ForeignKey('Boxing_mat', null=True, on_delete=models.CASCADE, verbose_name="Наименование")
    def __str__(self):
        return 'Нет' if self.code == 'Я000' else self.group.name + " " + self.form + " " + self.mat.name + " " + self.colour.name
    class Meta:
        verbose_name_plural = "Группы реактивов"
        verbose_name = "Группа реактива"

#Модели для этикетки

class Sticker_part(models.Model):
    name = models.CharField(max_length=80, verbose_name="Наименование")
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Группы реактивов"
        verbose_name = "Группа реактива"

class Sticker(models.Model):
    code = models.CharField(max_length=80, verbose_name="Наименование")
    product = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name="Наименование")
    part = models.ForeignKey('Sticker_part', on_delete=models.CASCADE, verbose_name="Наименование")
    def __str__(self):
        return 'Нет' if self.code == '0000Э' else "Этикетка " + self.product.code + " " + self.part.name + " / " + self.product.name + ' ' + self.product.mark.name + ' ' + ('' if self.product.option == 'отсутствует' else self.product.option)
    class Meta:
        verbose_name_plural = "Группы реактивов"
        verbose_name = "Группа реактива"


#Модели для производства

class Production(models.Model):
    composition = models.ForeignKey('Composition', on_delete=models.CASCADE, verbose_name="Наименование")
    container = models.ForeignKey('Container', on_delete=models.CASCADE, verbose_name="Наименование")
    cap = models.ForeignKey('Cap', on_delete=models.CASCADE, verbose_name="Наименование")
    sticker = models.ForeignKey('Sticker', on_delete=models.CASCADE, verbose_name="Наименование")
    boxing = models.ForeignKey('Boxing', on_delete=models.CASCADE, verbose_name="Наименование")
    compAmount = models.FloatField(default = 0, verbose_name="Наименование")
    compUnit = models.ForeignKey('Unit', null = True, on_delete=models.CASCADE, verbose_name="Наименование")
    contAmount = models.FloatField(default = 0, verbose_name="Наименование")
    contUnit = models.ForeignKey('Unit', null = True, related_name="cont_unit", on_delete=models.CASCADE, verbose_name="Наименование")
    capAmount = models.FloatField(default = 0, verbose_name="Наименование")
    capUnit = models.ForeignKey('Unit', null = True, related_name="cap_unit", on_delete=models.CASCADE, verbose_name="Наименование")
    stickerAmount = models.FloatField(default = 0, verbose_name="Наименование")
    stickerUnit = models.ForeignKey('Unit', null = True, related_name="sticker_unit", on_delete=models.CASCADE, verbose_name="Наименование")
    boxingAmount = models.FloatField(default = 0, verbose_name="Наименование")
    boxingUnit = models.ForeignKey('Unit', null = True, related_name="boxing_unit", on_delete=models.CASCADE, verbose_name="Наименование")
    def __str__(self):
        return self.product.name
    def get_boxing_amm(self):
        if self.boxingAmount == 0:
            res = 0
        else:
            res = int(1 / self.boxingAmount)
        return res
    class Meta:
        verbose_name_plural = "Группы реактивов"
        verbose_name = "Группа реактива"

#Модели для хранилищ

class Reactor(models.Model):
    code = models.CharField(max_length=80, verbose_name="Наименование")
    name = models.CharField(max_length=80, verbose_name="Наименование")
    product = models.CharField(max_length=250, verbose_name="Наименование")
    location = models.CharField(max_length=80, verbose_name="Наименование")
    #capacity = models.FloatField()
    min = models.FloatField(verbose_name="Наименование")
    max = models.FloatField(verbose_name="Наименование")
    ready = models.BooleanField(verbose_name="Наименование")
    def __str__(self):
        return self.code + ' ' + self.name
    def get_check(self):
        return 'checked' if self.ready else ''
    class Meta:
        verbose_name_plural = "Группы реактивов"
        verbose_name = "Группа реактива"

class Tank(models.Model):
    code = models.CharField(max_length=80, verbose_name="Наименование")
    name = models.CharField(max_length=80, verbose_name="Наименование")
    capacity = models.FloatField(verbose_name="Наименование")
    ready = models.BooleanField(verbose_name="Наименование")
    def __str__(self):
        return self.code + ' ' + self.name
    def get_check(self):
        return 'checked' if self.ready else ''
    class Meta:
        verbose_name_plural = "Группы реактивов"
        verbose_name = "Группа реактива"

#Модели для составов

class Formula(models.Model):
    code = models.CharField(max_length=80, verbose_name="Наименование")
    name = models.CharField(max_length=80, null=True, verbose_name="Наименование")
    composition = models.ForeignKey('Composition', on_delete=models.CASCADE, verbose_name="Наименование")
    cur_batch = models.FloatField(default = 1, verbose_name="Наименование")
    def __str__(self):
        return self.composition.name + (' ' if self.name is None else (' ' + self.name))
    def get_name(self):
        return self.composition.name + (' ' if self.name is None else (' ' + self.name))
    def get_name2(self):
        return self.code + ' ' + self.composition.name + (' ' if self.name is None else (' ' + self.name))
    def get_short_name(self):
        return '' if self.name is None else self.name
    class Meta:
        verbose_name_plural = "Группы реактивов"
        verbose_name = "Группа реактива"


class Formula_component(models.Model):
    formula = models.ForeignKey('Formula', on_delete=models.CASCADE, verbose_name="Наименование")
    mat = models.ForeignKey('Material', on_delete=models.CASCADE, verbose_name="Наименование")
    ammount = models.FloatField(verbose_name="Наименование")
    def __str__(self):
        return self.mat.name
    class Meta:
        verbose_name_plural = "Группы реактивов"
        verbose_name = "Группа реактива"

#Составной компонент
class Compl_comp(models.Model):
    formula = models.ForeignKey('Formula', blank=True, default = None, null=True, on_delete=models.CASCADE, verbose_name="Наименование")
    code = models.CharField(max_length=80, verbose_name="Наименование")
    name = models.CharField(max_length=80, verbose_name="Наименование")
    ammount = models.FloatField(verbose_name="Наименование")
    reserved = models.FloatField(default = 0, verbose_name="Наименование")
    store_amount = models.FloatField(default = 0, verbose_name="Наименование")
    form = models.ForeignKey('Product_form', blank=True, null=True, on_delete=models.CASCADE, verbose_name="Наименование")
    def __str__(self):
        return self.name
    def get_name(self):
        return self.code + ' ' + self.name
    class Meta:
        verbose_name_plural = "Группы реактивов"
        verbose_name = "Группа реактива"

#Составляющая составного компонента
class Compl_comp_comp(models.Model):
    compl = models.ForeignKey('Compl_comp', on_delete=models.CASCADE, verbose_name="Наименование")
    mat = models.ForeignKey('Material', on_delete=models.CASCADE, verbose_name="Наименование")
    ammount = models.FloatField(verbose_name="Наименование")
    def __str__(self):
        return self.mat.name
    class Meta:
        verbose_name_plural = "Группы реактивов"
        verbose_name = "Группа реактива"

#Характеристики


class Characteristic_type(models.Model):
    name = models.CharField(max_length=80, verbose_name="Наименование")
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Группы реактивов"
        verbose_name = "Группа реактива"

class Characteristic(models.Model):
    name = models.CharField(max_length=80, verbose_name="Наименование")
    char_type = models.ForeignKey('Characteristic_type', default=1, on_delete=models.CASCADE, verbose_name="Наименование")
    is_general = models.BooleanField(default = True, verbose_name="Наименование")
    group = models.ForeignKey('Char_group', on_delete=models.CASCADE, verbose_name="Наименование")
    def __str__(self):
        return ('' if self.group.name == 'отсутствует' else self.group.name + ': ') + self.name
    def get_group(self):
        return '' if self.group.name == 'отсутствует' else self.group.name + ': '
    class Meta:
        verbose_name_plural = "Группы реактивов"
        verbose_name = "Группа реактива"

class Char_group(models.Model):
    name = models.CharField(max_length=200, verbose_name="Наименование")
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Группы реактивов"
        verbose_name = "Группа реактива"

class Set_var(models.Model):
    name = models.CharField(max_length=80, verbose_name="Наименование")
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Группы реактивов"
        verbose_name = "Группа реактива"

class Characteristic_set_var(models.Model):
    char_set = models.ForeignKey('Characteristic', on_delete=models.CASCADE, verbose_name="Наименование")
    char_var = models.ForeignKey('Set_var', on_delete=models.CASCADE, verbose_name="Наименование")
    def __str__(self):
        return self.char_var.name
    class Meta:
        verbose_name_plural = "Группы реактивов"
        verbose_name = "Группа реактива"

class Characteristic_range(Characteristic):
    inf = models.FloatField(verbose_name="Наименование")
    sup = models.FloatField(verbose_name="Наименование")
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Группы реактивов"
        verbose_name = "Группа реактива"

class Characteristic_number(Characteristic):
    inf = models.FloatField(verbose_name="Наименование")
    sup = models.FloatField(verbose_name="Наименование")
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Группы реактивов"
        verbose_name = "Группа реактива"


class Composition_char(models.Model):
    comp = models.ForeignKey('Composition', on_delete=models.CASCADE, verbose_name="Наименование")
    characteristic = models.ForeignKey('Characteristic', on_delete=models.CASCADE, verbose_name="Наименование")
    def __str__(self):
        return self.characteristic.name
    def get_name(self):
        return self.comp.name + ' ' + self.characteristic.name
    class Meta:
        verbose_name_plural = "Группы реактивов"
        verbose_name = "Группа реактива"

class Comp_char_range(Composition_char):
    inf = models.FloatField(verbose_name="Наименование")
    sup = models.FloatField(verbose_name="Наименование")
    def __str__(self):
        return self.get_name()
    class Meta:
        verbose_name_plural = "Группы реактивов"
        verbose_name = "Группа реактива"

class Comp_char_number(Composition_char):
    number = models.FloatField(verbose_name="Наименование")
    def __str__(self):
        return self.get_name()
    class Meta:
        verbose_name_plural = "Группы реактивов"
        verbose_name = "Группа реактива"

class Comp_char_var(models.Model):
    comp_char = models.ForeignKey('Composition_char', on_delete=models.CASCADE, verbose_name="Наименование")
    char_var = models.ForeignKey('Set_var', on_delete=models.CASCADE, verbose_name="Наименование")
    def __str__(self):
        return self.comp_char.get_name() + ' ' + self.char_var.name
    class Meta:
        verbose_name_plural = "Группы реактивов"
        verbose_name = "Группа реактива"

#Характеристики реактивов
class Material_char(models.Model):
    mat = models.ForeignKey('Material', on_delete=models.CASCADE, verbose_name="Наименование")
    characteristic = models.ForeignKey('Characteristic', on_delete=models.CASCADE, verbose_name="Наименование")
    def __str__(self):
        return self.characteristic.name
    def get_name(self):
        return self.mat.name + ' ' + self.characteristic.name
    class Meta:
        verbose_name_plural = "Группы реактивов"
        verbose_name = "Группа реактива"

class Mat_char_number(Material_char):
    number = models.FloatField(verbose_name="Наименование")
    def __str__(self):
        return self.get_name()
    class Meta:
        verbose_name_plural = "Группы реактивов"
        verbose_name = "Группа реактива"

class Mat_char_var(models.Model):
    mat_char = models.ForeignKey('Material_char', on_delete=models.CASCADE, verbose_name="Наименование")
    char_var = models.ForeignKey('Set_var', on_delete=models.CASCADE, verbose_name="Наименование")
    def __str__(self):
        return self.mat_char.get_name() + ' ' + self.char_var.name
    class Meta:
        verbose_name_plural = "Группы реактивов"
        verbose_name = "Группа реактива"

# Модели для видовых характеристик

class Comp_prop_number(Composition_char):
    number = models.FloatField(verbose_name="Наименование")
    def __str__(self):
        return self.get_name()
    class Meta:
        verbose_name_plural = "Группы реактивов"
        verbose_name = "Группа реактива"

class Comp_prop_var(models.Model):
    comp_prop = models.ForeignKey('Composition_char', on_delete=models.CASCADE, verbose_name="Наименование")
    char_var = models.ForeignKey('Set_var', on_delete=models.CASCADE, verbose_name="Наименование")
    def __str__(self):
        return self.comp_char.get_name() + ' ' + self.char_var.name
    class Meta:
        verbose_name_plural = "Группы реактивов"
        verbose_name = "Группа реактива"
