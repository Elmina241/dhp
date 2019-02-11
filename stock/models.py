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
    producer = models.ForeignKey('Counterparty', null=True, default=None)
    def __str__(self):
        return self.model.name

class Good_name(models.Model):
    product = models.ForeignKey('Goods')
    article = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    barcode = models.CharField(max_length=200)
    original = models.CharField(max_length=200)
    local = models.CharField(max_length=200)
    transit = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Goods_property(models.Model):
    product = models.ForeignKey('Goods')
    property = models.ForeignKey('Property')
    applicable = models.BooleanField()
    visible = models.BooleanField()
    editable = models.BooleanField()
    def __str__(self):
        return str(self.product) + " " + str(self.property)

class Goods_unit(models.Model):
    product = models.ForeignKey('Goods')
    unit = models.ForeignKey('tables.Unit')
    applicable = models.BooleanField()
    isBase = models.BooleanField()
    coeff = models.FloatField()
    def __str__(self):
        return str(self.product) + " " + str(self.unit)

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

class Currency(models.Model):
    name = models.CharField(max_length=200)
    abbreviation = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Stock(models.Model):
    name = models.CharField(max_length=200)
    currency = models.ForeignKey('Currency')
    def __str__(self):
        return self.name

class Base(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class User(models.Model):
    name = models.CharField(max_length=500)
    group = models.IntegerField(default=0)
    def __str__(self):
        return self.name


class Demand(models.Model):
    STATUS_CHOICES = (
        ('0', 'Не рассмотренно'),
        ('1', 'Одобрено'),
        ('2', 'Отвергнуто'),
    )
    date = models.DateField(auto_now_add=True)
    consumer = models.ForeignKey('Counterparty')
    stock = models.ForeignKey('Stock')
    base = models.ForeignKey('Base')
    is_closed = models.BooleanField()
    finish_date = models.DateField(null = True)
    status = models.CharField(choices=STATUS_CHOICES, max_length=20)
    signer = models.ForeignKey('User')
    def __str__(self):
        return self.name

