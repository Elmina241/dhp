from django.db import models


#Классы модели МЦ
class Product_model(models.Model):
    name = models.CharField(max_length=200)
    group = models.ForeignKey('Model_group')
    def __str__(self):
        return self.name


class Model_unit(models.Model):
    model = models.ForeignKey('Product_model')
    unit = models.ForeignKey('tables.Unit')
    #coeff = models.FloatField()
    #is_base = models.BooleanField()
    def __str__(self):
        return self.unit.name

class Model_group(models.Model):
    name = models.CharField(max_length=200)
    parent = models.IntegerField(null = True)
    def __str__(self):
        return self.name

class Property(models.Model):
    name = models.CharField(max_length=200)
    prop_type = models.PositiveSmallIntegerField()
    #visible = models.BooleanField()
    #editable = models.BooleanField()
    #default = models.CharField(max_length=200, null = True)
    def __str__(self):
        return self.name

class Property_range(Property):
    inf = models.FloatField()
    sup = models.FloatField()
    def __str__(self):
        return self.name


class Property_var(models.Model):
    prop = models.ForeignKey('Property')
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Model_property(models.Model):
    model = models.ForeignKey('Product_model')
    prop = models.ForeignKey('Property')
    visible = models.BooleanField()
    editable = models.BooleanField()
    isDefault = models.BooleanField()
    def __str__(self):
        return self.name

class Default_text(Model_property):
    text = models.CharField(max_length=200)
    def __str__(self):
        return self.text

class Default_number(Model_property):
    number = models.FloatField()
    def __str__(self):
        return self.number

class Default_var(Model_property):
    var = models.ForeignKey('Property_var')
    def __str__(self):
        return str(self.var)

#Модели МЦ

class Goods(models.Model):
    model = models.ForeignKey('Product_model')
    base_unit = models.ForeignKey('tables.Unit')
    supply_price = models.FloatField()
    income_price = models.FloatField()
    def __str__(self):
        return self.model.name

class Goods_property(models.Model):
    product = models.ForeignKey('Goods')
    property = models.ForeignKey('Property')
    applicable = models.BooleanField()
    def __str__(self):
        return str(self.product) + " " + str(self.property)

class Property_num(Goods_property):
    number = models.FloatField()
    def __str__(self):
        return self.number

class Goods_string(Goods_property):
    text = models.CharField(max_length=500)
    def __str__(self):
        return self.text

class Goods_var(Goods_property):
    var = models.ForeignKey('Property_var')
    def __str__(self):
        return str(self.var)

class Counterparty(models.Model):
    ORG = '0'
    PHYS = '1'
    ENTR = '2'
    DIV = '3'
    PROV = '0'
    CONS = '1'
    MIX = '2'
    INF = '3'
    KIND_CHOICES = (
        (ORG, 'Организация'),
        (PHYS, 'Физлицо'),
        (ENTR, 'Предприниматель'),
        (DIV, 'Подразделение'),
    )
    CATEGORY_CHOICES = (
        (PROV, 'Поставщик'),
        (CONS, 'Потребитель'),
        (MIX, 'Смешанный'),
        (INF, 'Информационный'),
    )
    name = models.CharField(max_length=200)
    kind = models.CharField(choices=KIND_CHOICES, max_length=20)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=20)
    def __str__(self):
        return self.name


