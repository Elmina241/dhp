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
    def get_name(self):
        return Good_name.objects.filter(product = self)[0].name

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
    KIND_CHOICES = (
        ('0', 'Организация'),
        ('1', 'Физлицо'),
        ('2', 'Административная группа'),
    )
    name = models.CharField(max_length=200)
    kind = models.CharField(choices=KIND_CHOICES, max_length=20)
    is_provider = models.BooleanField()
    is_consumer = models.BooleanField()
    is_member = models.BooleanField()
    def __str__(self):
        return self.name

class Counter_stock(models.Model):
    counter = models.ForeignKey('Counterparty')
    stock = models.ForeignKey('Stock')
    def __str__(self):
        return str(self.counter) + ' ' + str(self.stock)

class Currency(models.Model):
    name = models.CharField(max_length=200)
    abbreviation = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Stock(models.Model):
    name = models.CharField(max_length=200)
    currency = models.ForeignKey('Currency', null=True)
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
        #('0', 'Отказ'),
        #('1', 'Выполнение'),
        #('2', 'Закрыт'),
    )
    date = models.DateField(auto_now_add=True)
    consumer = models.ForeignKey('Counterparty', related_name="consumer")
    provider = models.ForeignKey('Counterparty', related_name="provider")
    donor = models.ForeignKey('Stock', related_name="donor")
    acceptor = models.ForeignKey('Stock', related_name="acceptor")
    is_closed = models.BooleanField()
    release_date = models.DateField(null=True)
    finish_date = models.DateField(null = True)
    status = models.CharField(choices=STATUS_CHOICES, max_length=20)
    def __str__(self):
        return str(self.pk) + " " + str(self.date)

class Demand_good(models.Model):
    demand = models.ForeignKey('Demand')
    good = models.ForeignKey('Goods')
    name = models.ForeignKey('Good_name')
    unit = models.ForeignKey('tables.Unit')
    amount = models.IntegerField(default=0)
    def __str__(self):
        return str(self.demand) + ' ' + str(self.good)

