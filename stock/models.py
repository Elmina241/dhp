#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
import datetime

#Классы модели МЦ
class Product_model(models.Model):
    name = models.CharField(max_length=200)
    group = models.ForeignKey('Model_group', on_delete=models.CASCADE)
    def __str__(self):
        return self.name


class Model_unit(models.Model):
    model = models.ForeignKey('Product_model', on_delete=models.CASCADE)
    unit = models.ForeignKey('tables.Unit', on_delete=models.CASCADE)
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
    prop = models.ForeignKey('Property', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Model_property(models.Model):
    model = models.ForeignKey('Product_model', on_delete=models.CASCADE)
    prop = models.ForeignKey('Property', on_delete=models.CASCADE)
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
    var = models.ForeignKey('Property_var', on_delete=models.CASCADE)
    def __str__(self):
        return str(self.var)

#Модели МЦ

class Goods(models.Model):
    model = models.ForeignKey('Product_model', on_delete=models.CASCADE)
    producer = models.ForeignKey('Counterparty', null=True, default=None, on_delete=models.CASCADE)
    def __str__(self):
        return self.model.name
    def get_name(self, t='0'):
        name = Good_name.objects.filter(product = self, name_type='0', area=t)
        if name.count() != 0:
            return name[0].name
        else:
            return '-'
    def get_article(self, t='0'):
        article = Good_name.objects.filter(product = self, name_type='1', area=t)
        if article.count():
            return article[0].name
        else:
            return '-'
    def get_unit(self):
        unit = Goods_unit.objects.filter(product=self, isBase=True)
        if unit.count() != 0:
            return unit[0].unit
        return "-"
    def get_base_amount(self, amount, unit):
        u = Goods_unit.objects.filter(unit = unit, product = self)[0]
        coeff = u.coeff
        return amount / coeff
    def get_full_name(self, t):
        name = ""
        if Good_name.objects.filter(product=self, area=t).count() != 0:
            t_1 = Good_name.objects.filter(product = self, name_type='1', area=t)
            if t_1.count() != 0:
                name = name + t_1[0].name
            t_2 = Good_name.objects.filter(product=self, name_type='0', area=t)
            if t_2.count() != 0:
                name = name + " " + t_2[0].name
            t_3 = Good_name.objects.filter(product = self, name_type='2', area=t)
            if t_3.count() != 0:
                name = name + " " + t_3[0].name
        return name


class Good_name(models.Model):
    product = models.ForeignKey('Goods', on_delete=models.CASCADE)
    TYPE_CHOICES = (
        ('0', 'Наименование'),
        ('1', 'Артикул'),
        ('2', 'Штрихкод'),
    )
    AREA_CHOICES = (
        ('0', 'Локальное'),
        ('1', 'Транзитное'),
        ('2', 'Оригинальное'),
    )
    name_type = models.CharField(choices=TYPE_CHOICES, max_length=20)
    area = models.CharField(choices=AREA_CHOICES, max_length=20)
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Goods_property(models.Model):
    product = models.ForeignKey('Goods', on_delete=models.CASCADE)
    property = models.ForeignKey('Property', on_delete=models.CASCADE)
    applicable = models.BooleanField()
    visible = models.BooleanField()
    editable = models.BooleanField()
    def __str__(self):
        return str(self.product) + " " + str(self.property)

class Goods_unit(models.Model):
    product = models.ForeignKey('Goods', on_delete=models.CASCADE)
    unit = models.ForeignKey('tables.Unit', on_delete=models.CASCADE)
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
    var = models.ForeignKey('Property_var', on_delete=models.CASCADE)
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
    cur_vin = models.IntegerField(default='0', blank=True)
    def __str__(self):
        return self.name
    def has_stock(self, stock):
        return Counter_stock.objects.filter(counter = self, stock = stock).count() != 0

class Counter_stock(models.Model):
    counter = models.ForeignKey('Counterparty', on_delete=models.CASCADE)
    stock = models.ForeignKey('Stock', on_delete=models.CASCADE)
    def __str__(self):
        return str(self.counter) + ' ' + str(self.stock)

class Currency(models.Model):
    name = models.CharField(max_length=200)
    abbreviation = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Stock(models.Model):
    name = models.CharField(max_length=200)
    currency = models.ForeignKey('Currency', null=True, on_delete=models.CASCADE)
    cur_vin = models.IntegerField(default='0')
    def __str__(self):
        if self is None:
            return "-"
        else:
            return self.name

class Base(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

#class User(models.Model):
    #name = models.CharField(max_length=500)
    #group = models.IntegerField(default=0)
    #def __str__(self):
        #return self.name

class User_group(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    group = models.ForeignKey('Counterparty', on_delete=models.CASCADE)
    def __str__(self):
        return str(self.user)
    def get_permissions(self):
        permissions = {}
        for p in User_permission.objects.filter(user = self.user):
            permissions[p.section.pk] = p.is_allowed
        return permissions

class Demand(models.Model):
    date = models.DateField(auto_now_add=True)
    matrix = models.ForeignKey('Matrix', on_delete=models.CASCADE)
    consumer = models.ForeignKey('Counterparty', on_delete=models.CASCADE,  related_name="consumer", null=True)
    provider = models.ForeignKey('Counterparty', on_delete=models.CASCADE,  related_name="provider", null=True)
    donor = models.ForeignKey('Stock', related_name="donor", null=True, on_delete=models.CASCADE)
    acceptor = models.ForeignKey('Stock', related_name="acceptor", null=True, on_delete=models.CASCADE)
    is_closed = models.BooleanField(default=False)
    release_date = models.DateField(null=True)
    finish_date = models.DateField(null = True)
    is_edited = models.BooleanField(default=False)
    vin = models.IntegerField(blank=True)
    is_demand = models.BooleanField(default=True)
    user = models.ForeignKey('auth.User', blank=True, on_delete=models.CASCADE)
    #status = models.CharField(choices=STATUS_CHOICES, max_length=20, default='3')
    def __str__(self):
        return str(self.pk) + " " + str(self.date)

class Section(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return str(self.pk) + " " + self.name

class User_permission(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    section = models.ForeignKey('Section', on_delete=models.CASCADE)
    is_allowed = models.BooleanField(default=True)
    def __str__(self):
        return str(self.user) + " " + str(self.section)

class Demand_good(models.Model):
    matrix = models.ForeignKey('Matrix', on_delete=models.CASCADE)
    good = models.ForeignKey('Goods', on_delete=models.CASCADE)
    name = models.CharField(max_length=500)
    article = models.CharField(max_length=200, default = '-')
    unit = models.ForeignKey('tables.Unit', on_delete=models.CASCADE)
    amount = models.IntegerField(default=0)
    balance = models.IntegerField(default=0)
    def __str__(self):
        return str(self.demand) + ' ' + str(self.good)
    def get_demand(self):
        return Demand.objects.filter(matrix = self.matrix)[0]

class Stock_operation(models.Model):
    OPERATION_CHOICES = (
        ('0', 'Приход'),
        ('1', 'Расход'),
        ('2', 'Коррекция'),
    )
    package = models.ForeignKey('Package', on_delete=models.CASCADE)
    good = models.ForeignKey('Goods', on_delete=models.CASCADE)
    operation = models.CharField(choices=OPERATION_CHOICES, max_length=20, default='0')
    date = models.DateTimeField(auto_now_add=True, blank=True)
    unit = models.ForeignKey('tables.Unit', on_delete=models.CASCADE)
    amount = models.IntegerField(default=0)
    cost = models.FloatField(default=0, blank=True)
    last_value = models.FloatField(default=0, blank=True)
    def __str__(self):
        return str(self.stock) + ' ' + str(self.good)
    def get_good_name(self):
        return Demand_good.objects.filter(demand__pk = self.cause_id, good = self.good)[0].name

    class Meta:
        ordering = ['-date']

class Stock_good(models.Model):
    stock = models.ForeignKey('Stock', on_delete=models.CASCADE)
    good = models.ForeignKey('Goods', on_delete=models.CASCADE)
    unit = models.ForeignKey('tables.Unit', on_delete=models.CASCADE)
    amount = models.FloatField(default=0)
    cost = models.FloatField(default=0, blank=True)
    def __str__(self):
        return str(self.stock) + ' ' + str(self.good)

class Matrix(models.Model):
    ACCESS_CHOICES = (
        ('0', 'Открыто всем'),
        ('1', 'Открыто донору'),
        ('2', 'Открыто акцептору'),
        ('3', 'Закрыто'),
        ('4', 'Выполнение')
    )
    CAUSE_CHOICES = (
        ('0', 'Перемещение'),
        ('1', 'Оприходование/Выбытие'),
        ('2', 'Инвентаризация'),
    )
    access = cause = models.CharField(choices=ACCESS_CHOICES, max_length=20, default='0')
    cause = models.CharField(choices=CAUSE_CHOICES, max_length=20, default='0')
    cause_id = models.IntegerField(default=0, null = True)
    name = models.CharField(max_length=500, null=True)
    def __str__(self):
        return self.access


class Order(models.Model):
    STATUS_CHOICES = (
        ('0', 'Свободно'),
        ('1', 'Заполнение'),
        ('2', 'Завершено')
    )
    CAUSE_CHOICES = (
        ('0', 'Перемещение'),
        ('1', 'Производство'),
        ('2', 'Списание')
    )
    cause = models.CharField(choices=CAUSE_CHOICES, max_length=20, default='0')
    stock = models.ForeignKey('Stock', on_delete=models.CASCADE)
    matrix = models.ForeignKey('Matrix', on_delete=models.CASCADE)
    isDonor = models.BooleanField()
    date = models.DateField(auto_now_add=True, blank=True)
    status = models.CharField(choices=STATUS_CHOICES, max_length=20, default='0')
    def __str__(self):
        return str(self.stock) + ' ' + str(self.matrix)

class Package(models.Model):
    stock = models.ForeignKey('Stock', on_delete=models.CASCADE)
    matrix = models.ForeignKey('Matrix', on_delete=models.CASCADE)
    date = models.DateTimeField(blank=True)
    vin = models.IntegerField(blank=True)
    def __str__(self):
        return str(self.stock) + ' ' + str(self.matrix)

class Inventory(models.Model):
    date = models.DateTimeField(blank=True, auto_now_add=True)
    stock = models.ForeignKey('Stock', on_delete=models.CASCADE)
    is_finished = models.BooleanField()
    def __str__(self):
        return str(self.date) + ' ' + str(self.stock)

class Inventory_good(models.Model):
    good = models.ForeignKey('Goods', on_delete=models.CASCADE)
    inventory = models.ForeignKey('Inventory', on_delete=models.CASCADE)
    amount = models.IntegerField(default=0)
    def __str__(self):
        return str(self.inventory) + ' ' + str(self.good)