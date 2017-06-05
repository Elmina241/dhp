from django.db import models


# Модели для химвеществ
class Material_group(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Prefix(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Unit(models.Model):
    name = models.CharField(max_length=80)
    def __str__(self):
        return self.name

class Material(models.Model):
    code = models.CharField(max_length=80)
    name = models.CharField(max_length=80)
    group = models.ForeignKey('Material_group')
    prefix = models.ForeignKey('Prefix')
    mark = models.CharField(max_length=80)
    ammount = models.FloatField()
    unit = models.ForeignKey('Unit')
    concentration = models.FloatField()
    price = models.FloatField()
    def __str__(self):
        full_name = self.name + ('' if self.mark == '-' else (' ' + self.mark))
        return full_name
    def get_name(self):
        full_name = self.code + " " + self.name
        return full_name


# Модели для продукции
class Product_group(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Product_form(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Product_use(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Product_option(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Product_detail(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Product_mark(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Product(models.Model):
    code = models.CharField(max_length=13)
    name = models.CharField(max_length=80)
    group = models.ForeignKey('Product_group')
    form = models.ForeignKey('Product_form')
    use = models.ForeignKey('Product_use')
    option = models.ForeignKey('Product_option')
    detail = models.ForeignKey('Product_detail')
    mark = models.ForeignKey('Product_mark')
    def __str__(self):
        full_name = self.form.name + ' ' + self.use.name + ' ' + ('' if self.option.name == 'отсутствует' else (self.option.name + ' ')) + ('' if self.detail.name == 'отсутствует' else self.detail.name) + ' (' + self.mark.name + ')'
        return full_name
    def get_short_code(self):
        return self.code[9:]

#Модели для рецептов

class Composition_group(models.Model):
    name = models.CharField(max_length=80)
    def __str__(self):
        return self.name

class Composition(models.Model):
    code = models.CharField(max_length=80)
    name = models.CharField(max_length=80)
    sgr = models.CharField(max_length=80)
    group = models.ForeignKey('Composition_group')
    isFinal = models.BooleanField(default = True)
    def __str__(self):
        return self.name
    def get_name(self):
        return self.code + " " + self.name

class Components(models.Model):
    comp = models.ForeignKey('Composition')
    mat = models.ForeignKey('Material')
    min = models.FloatField()
    max = models.FloatField()

#Модели для тары

class Container_group(models.Model):
    name = models.CharField(max_length=80)
    def __str__(self):
        return self.name

class Container_form(models.Model):
    name = models.CharField(max_length=80)
    def __str__(self):
        return self.name

class Colour(models.Model):
    name = models.CharField(max_length=80)
    def __str__(self):
        return self.name

class Container_mat(models.Model):
    name = models.CharField(max_length=80)
    def __str__(self):
        return self.name

class Container(models.Model):
    code = models.CharField(max_length=80)
    group = models.ForeignKey('Container_group')
    form = models.ForeignKey('Container_form')
    colour = models.ForeignKey('Colour')
    mat = models.ForeignKey('Container_mat')
    def __str__(self):
        return self.group.name + " " + self.form.name + " " + self.mat.name + " " + self.colour.name

#Модели для укупорки

class Cap_group(models.Model):
    name = models.CharField(max_length=80)
    def __str__(self):
        return self.name

class Cap_form(models.Model):
    name = models.CharField(max_length=80)
    def __str__(self):
        return self.name

class Cap(models.Model):
    code = models.CharField(max_length=80)
    group = models.ForeignKey('Cap_group')
    form = models.ForeignKey('Cap_form')
    colour = models.ForeignKey('Colour')
    mat = models.ForeignKey('Container_mat')
    def __str__(self):
        return self.group.name + " " + self.form.name + " " + self.mat.name + " " + self.colour.name

#Модели для упаковки

class Boxing(models.Model):
    code = models.CharField(max_length=80)
    name = models.CharField(max_length=80)
    def __str__(self):
        return self.name

#Модели для этикетки

class Sticker_part(models.Model):
    name = models.CharField(max_length=80)
    def __str__(self):
        return self.name

class Sticker(models.Model):
    code = models.CharField(max_length=80)
    product = models.ForeignKey('Product')
    part = models.ForeignKey('Sticker_part')
    def __str__(self):
        return "Этикетка " + self.product.code + " " + self.part.name + " / " + self.product.name

#Модели для производства

class Production(models.Model):
    product = models.ForeignKey('Product')
    composition = models.ForeignKey('Composition')
    container = models.ForeignKey('Container')
    cap = models.ForeignKey('Cap')
    sticker = models.ForeignKey('Sticker')
    boxing = models.ForeignKey('Boxing')
    def __str__(self):
        return self.product.name

#Модели для хранилищ

class Reactor(models.Model):
    code = models.CharField(max_length=80)
    name = models.CharField(max_length=80)
    #capacity = models.FloatField()
    min = models.FloatField()
    max = models.FloatField()
    ready = models.BooleanField()
    def __str__(self):
        return self.code + ' ' + self.name
    def get_check(self):
        return 'checked' if self.ready else ''

class Tank(models.Model):
    code = models.CharField(max_length=80)
    name = models.CharField(max_length=80)
    capacity = models.FloatField()
    ready = models.BooleanField()
    def __str__(self):
        return self.name
    def get_check(self):
        return 'checked' if self.ready else ''

#Модели для составов

class Formula(models.Model):
    code = models.CharField(max_length=80)
    composition = models.ForeignKey('Composition')
    def __str__(self):
        return self.code + ' ' + self.composition.name
    def get_name(self):
        return self.code + ' ' + self.composition.name


class Formula_component(models.Model):
    formula = models.ForeignKey('Formula')
    mat = models.ForeignKey('Material')
    ammount = models.FloatField()
    def __str__(self):
        return self.mat.name

#Составной компонент
class Compl_comp(models.Model):
    composition = models.ForeignKey('Composition', blank=True, default = None, null=True)
    code = models.CharField(max_length=80)
    name = models.CharField(max_length=80)
    ammount = models.FloatField()
    def __str__(self):
        return self.name
    def get_name(self):
        return self.code + ' ' + self.name

#Составляющая составного компонента
class Compl_comp_comp(models.Model):
    compl = models.ForeignKey('Compl_comp')
    mat = models.ForeignKey('Material')
    ammount = models.FloatField()
    def __str__(self):
        return self.mat.name

#Характеристики


class Characteristic_type(models.Model):
    name = models.CharField(max_length=80)
    def __str__(self):
        return self.name

class Characteristic(models.Model):
    name = models.CharField(max_length=80)
    char_type = models.ForeignKey('Characteristic_type', default=1)
    group = models.ForeignKey('Char_group')
    def __str__(self):
        return ('' if self.group.name == 'отсутствует' else self.group.name + ': ') + self.name
    def get_group(self):
        return '' if self.group.name == 'отсутствует' else self.group.name + ': '

class Char_group(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Set_var(models.Model):
    name = models.CharField(max_length=80)
    def __str__(self):
        return self.name

class Characteristic_set_var(models.Model):
    char_set = models.ForeignKey('Characteristic')
    char_var = models.ForeignKey('Set_var')
    def __str__(self):
        return self.char_var.name

class Characteristic_range(Characteristic):
    inf = models.FloatField()
    sup = models.FloatField()
    def __str__(self):
        return self.name

class Characteristic_number(Characteristic):
    inf = models.FloatField()
    sup = models.FloatField()
    def __str__(self):
        return self.name


class Composition_char(models.Model):
    comp = models.ForeignKey('Composition')
    characteristic = models.ForeignKey('Characteristic')
    def __str__(self):
        return self.characteristic.name
    def get_name(self):
        return self.comp.name + ' ' + self.characteristic.name

class Comp_char_range(Composition_char):
    inf = models.FloatField()
    sup = models.FloatField()
    def __str__(self):
        return self.get_name()

class Comp_char_number(Composition_char):
    number = models.FloatField()
    def __str__(self):
        return self.get_name()

class Comp_char_var(models.Model):
    comp_char = models.ForeignKey('Composition_char')
    char_var = models.ForeignKey('Set_var')
    def __str__(self):
        return self.comp_char.get_name() + ' ' + self.char_var.name

#Модели для составного компонента
