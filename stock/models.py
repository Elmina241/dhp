#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
import pytz

local_tz = pytz.timezone('Asia/Vladivostok')

#Классы модели МЦ
class Product_model(models.Model):
    name = models.CharField(max_length=200, verbose_name="Наименование")
    group = models.ForeignKey('Model_group', on_delete=models.CASCADE, verbose_name="Группа")
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Модели товаров"
        verbose_name = "Модель товара"


class Model_unit(models.Model):
    model = models.ForeignKey('Product_model', on_delete=models.CASCADE, verbose_name="Модель товара")
    unit = models.ForeignKey('tables.Unit', on_delete=models.CASCADE, verbose_name="Единица измерения")
    def __str__(self):
        return self.unit.name
    class Meta:
        verbose_name_plural = "Единицы измерения моделей"
        verbose_name = "Единица измерения модели"

class Model_group(models.Model):
    name = models.CharField(max_length=200, verbose_name="Наименование")
    parent = models.IntegerField(null = True, verbose_name="Родительская группа")
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Группы моделей"
        verbose_name = "Группа модели"

class Property(models.Model):
    name = models.CharField(max_length=200, verbose_name="Наименование")
    prop_type = models.PositiveSmallIntegerField(verbose_name="Тип")
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Свойства"
        verbose_name = "Свойство"

class Property_range(Property):
    inf = models.FloatField(verbose_name="Минимум")
    sup = models.FloatField(verbose_name="Максимум")
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Диапазоны свойств"
        verbose_name = "Диапазон свойства"


class Property_var(models.Model):
    prop = models.ForeignKey('Property', on_delete=models.CASCADE, verbose_name="Свойство")
    name = models.CharField(max_length=200, verbose_name="Наименование")
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Варианты свойств"
        verbose_name = "Вариант свойства"

class Model_property(models.Model):
    model = models.ForeignKey('Product_model', on_delete=models.CASCADE, verbose_name="Модель")
    prop = models.ForeignKey('Property', on_delete=models.CASCADE, verbose_name="Свойство")
    visible = models.BooleanField(verbose_name="Видимое")
    editable = models.BooleanField(verbose_name="Изменяемое")
    isDefault = models.BooleanField(verbose_name="Значение по умолчанию?")
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Свойства моделей"
        verbose_name = "Свойство модели"

class Default_text(Model_property):
    text = models.CharField(max_length=200, verbose_name="Текст")
    def __str__(self):
        return self.text
    class Meta:
        verbose_name_plural = "Тексты по умолчанию"
        verbose_name = "Текст по умолчанию"

class Default_number(Model_property):
    number = models.FloatField(verbose_name="Число")
    def __str__(self):
        return self.number
    class Meta:
        verbose_name_plural = "Числа по умолчанию"
        verbose_name = "Число по умолчанию"

class Default_var(Model_property):
    var = models.ForeignKey('Property_var', on_delete=models.CASCADE, verbose_name="Значение")
    def __str__(self):
        return str(self.var)
    class Meta:
        verbose_name_plural = "Значения по умолчанию"
        verbose_name = "Значение по умолчанию"

#Модели МЦ

class Goods(models.Model):
    model = models.ForeignKey('Product_model', on_delete=models.CASCADE, verbose_name="Модель")
    producer = models.ForeignKey('Counterparty', null=True, default=None, on_delete=models.CASCADE, verbose_name="Создатель")
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
        if article.count() != 0:
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
        full_name = ""
        if Good_name.objects.filter(product=self, area=t).count() != 0:
            t_1 = Good_name.objects.filter(product=self, name_type='1', area=t)
            if t_1.count() != 0:
                full_name = full_name + t_1[0].name
            t_2 = Good_name.objects.filter(product=self, name_type='0', area=t)
            if t_2.count() != 0:
                full_name = full_name + " " + t_2[0].name
            t_3 = Good_name.objects.filter(product=self, name_type='2', area=t)
            if t_3.count() != 0:
                full_name = full_name + " " + t_3[0].name
        return full_name
    def get_full_name2(self, t):
        full_name = ""
        article = ""
        name = ""
        if Good_name.objects.filter(product=self, area=t).count() != 0:
            t_1 = Good_name.objects.filter(product = self, name_type='1', area=t)
            if t_1.count() != 0:
                article = t_1[0].name
                full_name = full_name + article
            t_2 = Good_name.objects.filter(product=self, name_type='0', area=t)
            if t_2.count() != 0:
                name = t_2[0].name
                full_name = full_name + " " + name
            t_3 = Good_name.objects.filter(product = self, name_type='2', area=t)
            if t_3.count() != 0:
                full_name = full_name + " " + t_3[0].name
        return [full_name, article, name]
    class Meta:
        verbose_name_plural = "Товары"
        verbose_name = "Товар"


class Good_name(models.Model):
    product = models.ForeignKey('Goods', on_delete=models.CASCADE, verbose_name="Товар")
    TYPE_CHOICES = (
        ('1', 'Артикул'),
        ('0', 'Наименование'),
        ('2', 'Штрихкод'),
    )
    AREA_CHOICES = (
        ('0', 'Локальное'),
        ('1', 'Транзитное'),
        ('2', 'Оригинальное'),
    )
    name_type = models.CharField(choices=TYPE_CHOICES, max_length=20, verbose_name="Тип имени")
    area = models.CharField(choices=AREA_CHOICES, max_length=20, verbose_name="Область")
    name = models.CharField(max_length=200, verbose_name="Имя")
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Имена товаров"
        verbose_name = "Имя товара"

class Goods_property(models.Model):
    product = models.ForeignKey('Goods', on_delete=models.CASCADE, verbose_name="Товар")
    property = models.ForeignKey('Property', on_delete=models.CASCADE, verbose_name="Свойство")
    applicable = models.BooleanField(verbose_name="Применимое")
    visible = models.BooleanField(verbose_name="Видимое")
    editable = models.BooleanField(verbose_name="Изменяемое")
    def __str__(self):
        return str(self.product) + " " + str(self.property)
    class Meta:
        verbose_name_plural = "Свойства товаров"
        verbose_name = "Свойство товара"

class Goods_unit(models.Model):
    product = models.ForeignKey('Goods', on_delete=models.CASCADE, verbose_name="Товар")
    unit = models.ForeignKey('tables.Unit', on_delete=models.CASCADE, verbose_name="Ед. изм.")
    applicable = models.BooleanField(verbose_name="Применимая")
    isBase = models.BooleanField(verbose_name="Базова")
    coeff = models.FloatField(verbose_name="Коэффициент")
    def __str__(self):
        return str(self.product) + " " + str(self.unit)
    class Meta:
        verbose_name_plural = "Единицы измерения товаров"
        verbose_name = "Единица измерения товара"

class Property_num(Goods_property):
    number = models.FloatField(verbose_name="Число")
    def __str__(self):
        return self.number
    class Meta:
        verbose_name_plural = "Числовые свойства товаров"
        verbose_name = "Числовое свойство товара"

class Goods_string(Goods_property):
    text = models.CharField(max_length=500, verbose_name="Текст")
    def __str__(self):
        return self.text
    class Meta:
        verbose_name_plural = "Текстовое свойство товара"
        verbose_name = "Текстовые свойства товаров"

class Goods_var(Goods_property):
    var = models.ForeignKey('Property_var', on_delete=models.CASCADE, verbose_name="Вариант")
    def __str__(self):
        return str(self.var)
    class Meta:
        verbose_name_plural = "Варианты свойств товаров"
        verbose_name = "Вариант свойства товара"

class Counterparty(models.Model):
    KIND_CHOICES = (
        ('0', 'Организация'),
        ('1', 'Физлицо'),
        ('2', 'Административная группа'),
    )
    name = models.CharField(max_length=200, verbose_name="Наименование")
    kind = models.CharField(choices=KIND_CHOICES, max_length=20, verbose_name="Тип")
    is_provider = models.BooleanField(verbose_name="Поставщик")
    is_consumer = models.BooleanField(verbose_name="Потребитель")
    is_member = models.BooleanField(verbose_name="Член группы")
    cur_vin = models.IntegerField(default='0', blank=True, verbose_name="Текущий ВИН")
    def __str__(self):
        return self.name
    def has_stock(self, stock):
        return Counter_stock.objects.filter(counter = self, stock = stock).count() != 0
    class Meta:
        verbose_name_plural = "Контрагенты"
        verbose_name = "Контрагент"

class Counter_stock(models.Model):
    counter = models.ForeignKey('Counterparty', on_delete=models.CASCADE, verbose_name="Контрагент")
    stock = models.ForeignKey('Stock', on_delete=models.CASCADE, verbose_name="Склад")
    def __str__(self):
        return str(self.counter) + ' ' + str(self.stock)
    class Meta:
        verbose_name_plural = "Склады контрагентов"
        verbose_name = "Склад контрагента"

class Currency(models.Model):
    name = models.CharField(max_length=200, verbose_name="Наименование")
    abbreviation = models.CharField(max_length=200, verbose_name="Аббревиатура")
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Валюты"
        verbose_name = "Валюта"

class Stock(models.Model):
    name = models.CharField(max_length=200, verbose_name="Наименование")
    currency = models.ForeignKey('Currency', null=True, on_delete=models.CASCADE, verbose_name="Валюта")
    cur_vin = models.IntegerField(default='0', verbose_name="Текущий ВИН")
    def __str__(self):
        if self is None:
            return "-"
        else:
            return self.name

    class Meta:
        verbose_name_plural = "Склады"
        verbose_name = "Склад"

class Base(models.Model):
    name = models.CharField(max_length=200, verbose_name="Наименование")
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Основания"
        verbose_name = "Основание"

#class User(models.Model):
    #name = models.CharField(max_length=500)
    #group = models.IntegerField(default=0)
    #def __str__(self):
        #return self.name

class User_group(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name="Пользователь")
    group = models.ForeignKey('Counterparty', on_delete=models.CASCADE, verbose_name="Группа")
    def __str__(self):
        return str(self.user)
    def get_permissions(self):
        permissions = {}
        for p in User_permission.objects.filter(user = self.user):
            permissions[p.section.pk] = p.is_allowed
        return permissions
    class Meta:
        verbose_name_plural = "Пользовательские группы"
        verbose_name = "Пользовательская группа"

class Demand(models.Model):
    date = models.DateField(auto_now_add=True, verbose_name="Дата")
    matrix = models.ForeignKey('Matrix', on_delete=models.CASCADE, verbose_name="Матрица")
    consumer = models.ForeignKey('Counterparty', on_delete=models.CASCADE,  related_name="consumer", null=True, verbose_name="Потребитель")
    provider = models.ForeignKey('Counterparty', on_delete=models.CASCADE,  related_name="provider", null=True, verbose_name="Поставщик")
    donor = models.ForeignKey('Stock', related_name="donor", null=True, on_delete=models.CASCADE, verbose_name="Донор")
    acceptor = models.ForeignKey('Stock', related_name="acceptor", null=True, on_delete=models.CASCADE, verbose_name="Акцептор")
    is_closed = models.BooleanField(default=False, verbose_name="Закрыто")
    release_date = models.DateField(null=True, verbose_name="Дата отпуска")
    finish_date = models.DateField(null = True, verbose_name="Дата поставки")
    is_edited = models.BooleanField(default=False, verbose_name="Отредактировано")
    vin = models.IntegerField(blank=True, verbose_name="ВИН")
    is_demand = models.BooleanField(default=True, verbose_name="Требование")
    user = models.ForeignKey('auth.User', blank=True, null=True, on_delete=models.CASCADE, verbose_name="Создатель")
    #status = models.CharField(choices=STATUS_CHOICES, max_length=20, default='3')
    def __str__(self):
        return str(self.pk) + " " + str(self.date)
    class Meta:
        verbose_name_plural = "Требования"
        verbose_name = "Требование"

class Section(models.Model):
    name = models.CharField(max_length=200, verbose_name="Наименование")
    def __str__(self):
        return str(self.pk) + " " + self.name
    class Meta:
        verbose_name_plural = "Области"
        verbose_name = "Область"

class User_permission(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name="Пользователь")
    section = models.ForeignKey('Section', on_delete=models.CASCADE, verbose_name="Область")
    is_allowed = models.BooleanField(default=True, verbose_name="Разрешено")
    def __str__(self):
        return str(self.user) + " " + str(self.section)
    class Meta:
        verbose_name_plural = "Пользовательские разрешения"
        verbose_name = "Пользовательское разрешение"

class Demand_good(models.Model):
    matrix = models.ForeignKey('Matrix', on_delete=models.CASCADE, verbose_name="Матрица")
    good = models.ForeignKey('Goods', on_delete=models.CASCADE, verbose_name="Товар")
    name = models.CharField(max_length=500, verbose_name="Наименование")
    article = models.CharField(max_length=200, default = '-', verbose_name="Артикул")
    unit = models.ForeignKey('tables.Unit', on_delete=models.CASCADE, verbose_name="Ед. изм.")
    amount = models.FloatField(default=0, verbose_name="Количество")
    balance = models.FloatField(default=0, verbose_name="Остаток")
    def __str__(self):
        return str(self.demand) + ' ' + str(self.good)
    def get_demand(self):
        return Demand.objects.filter(matrix = self.matrix)[0]
    class Meta:
        verbose_name_plural = "Товары требований"
        verbose_name = "Товар требования"

class Stock_operation(models.Model):
    OPERATION_CHOICES = (
        ('0', 'Приход'),
        ('1', 'Расход'),
        ('2', 'Коррекция'),
    )
    package = models.ForeignKey('Package', on_delete=models.CASCADE, verbose_name="Пакет")
    good = models.ForeignKey('Goods', on_delete=models.CASCADE, verbose_name="Товар")
    operation = models.CharField(choices=OPERATION_CHOICES, max_length=20, default='0', verbose_name="Операция")
    date = models.DateTimeField(auto_now_add=True, blank=True, verbose_name="Дата")
    unit = models.ForeignKey('tables.Unit', on_delete=models.CASCADE, verbose_name="Ед. изм.")
    amount = models.FloatField(default=0, verbose_name="Количество")
    cost = models.FloatField(default=0, blank=True, verbose_name="Стоимость")
    last_value = models.FloatField(default=0, blank=True, verbose_name="Последнее значение")
    def __str__(self):
        return str(self.date.replace(tzinfo=pytz.utc).astimezone(local_tz)) + ' ' + str(self.pk) + ' ' + str(self.good)
    def get_good_name(self):
        return Demand_good.objects.filter(demand__pk = self.cause_id, good = self.good)[0].name

    class Meta:
        ordering = ['-date']
        verbose_name_plural = "Журнал операций"
        verbose_name = "Операция"

class Stock_good(models.Model):
    stock = models.ForeignKey('Stock', on_delete=models.CASCADE, verbose_name="Склад")
    good = models.ForeignKey('Goods', on_delete=models.CASCADE, verbose_name="Товар")
    unit = models.ForeignKey('tables.Unit', on_delete=models.CASCADE, verbose_name="Ед. изм.")
    amount = models.FloatField(default=0, verbose_name="Количество")
    cost = models.FloatField(default=0, blank=True, verbose_name="Стоимость")
    def __str__(self):
        return str(self.stock) + ' ' + str(self.good)
    def get_price(self):
        if self.amount != 0:
            return self.cost / self.amount
        else:
            price = 0
            last_cost = Stock_operation.objects.filter(good=self.good).exclude(cost=0).order_by(
                '-date').first()
            if last_cost is not None:
                price = last_cost.cost
            return price

    class Meta:
        verbose_name_plural = "Товары на складах"
        verbose_name = "Товар на складе"

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
    access = models.CharField(choices=ACCESS_CHOICES, max_length=20, default='0', verbose_name="Доступ")
    cause = models.CharField(choices=CAUSE_CHOICES, max_length=20, default='0', verbose_name="Операция")
    cause_id = models.IntegerField(default=0, null = True, verbose_name="id операции")
    name = models.CharField(max_length=500, null=True, verbose_name="Наименование")
    def __str__(self):
        return self.access
    class Meta:
        verbose_name_plural = "Матрицы"
        verbose_name = "Матрица"


class Order(models.Model):
    STATUS_CHOICES = (
        ('0', 'Свободно'),
        ('1', 'Заполнение'),
        ('2', 'Завершено')
    )
    CAUSE_CHOICES = (
        ('0', 'Перемещение'),
        ('1', 'Производство'),
        ('2', 'Списание'),
        ('3', 'Поступление')
    )
    cause = models.CharField(choices=CAUSE_CHOICES, max_length=20, default='0', verbose_name="Основание")
    stock = models.ForeignKey('Stock', on_delete=models.CASCADE, verbose_name="Склад")
    matrix = models.ForeignKey('Matrix', on_delete=models.CASCADE, verbose_name="Матрица")
    isDonor = models.BooleanField(verbose_name="Донор?")
    date = models.DateField(auto_now_add=True, blank=True, verbose_name="Дата")
    status = models.CharField(choices=STATUS_CHOICES, max_length=20, default='0', verbose_name="Статус")
    def __str__(self):
        return str(self.stock) + ' ' + str(self.matrix)
    class Meta:
        verbose_name_plural = "Ордеры"
        verbose_name = "Ордер"

class Package(models.Model):
    stock = models.ForeignKey('Stock', on_delete=models.CASCADE, verbose_name="Склад")
    matrix = models.ForeignKey('Matrix', on_delete=models.CASCADE, verbose_name="Матрица")
    date = models.DateTimeField(blank=True, verbose_name="Дата")
    vin = models.IntegerField(blank=True, verbose_name="ВИН")
    def __str__(self):
        return str(self.stock) + ' ' + str(self.matrix)
    class Meta:
        verbose_name_plural = "Пакеты"
        verbose_name = "Пакет"

class Inventory(models.Model):
    date = models.DateTimeField(blank=True, auto_now_add=True, verbose_name="Дата")
    stock = models.ForeignKey('Stock', on_delete=models.CASCADE, verbose_name="Склад")
    is_finished = models.BooleanField(verbose_name="Завершена")
    def __str__(self):
        return str(self.date) + ' ' + str(self.stock)
    class Meta:
        verbose_name_plural = "Инвентаризации"
        verbose_name = "Инвентаризация"

class Inventory_good(models.Model):
    good = models.ForeignKey('Goods', on_delete=models.CASCADE, verbose_name="Товар")
    inventory = models.ForeignKey('Inventory', on_delete=models.CASCADE, verbose_name="Инвентаризация")
    amount = models.FloatField(default=0, verbose_name="Количество")
    def __str__(self):
        return str(self.inventory) + ' ' + str(self.good)
    class Meta:
        verbose_name_plural = "Товары инвентаризаций"
        verbose_name = "Товар инвентаризации"

class Constant(models.Model):
    name = models.CharField(max_length=200, verbose_name="Наименование")
    value = models.FloatField(default='0', verbose_name="Значение")
    def __str__(self):
        if self is None:
            return "-"
        else:
            return self.name

    class Meta:
        verbose_name_plural = "Константы"
        verbose_name = "Константа"

class Projection(models.Model):
    name = models.CharField(max_length=200, verbose_name="Наименование")
    property = models.ForeignKey('Property', on_delete=models.CASCADE, verbose_name="Свойство")
    def __str__(self):
        if self is None:
            return "-"
        else:
            return self.property.name + '.' + self.name

    class Meta:
        verbose_name_plural = "Проекции"
        verbose_name = "Проекция"

class Projection_value(models.Model):
    projection = models.ForeignKey('Projection', on_delete=models.CASCADE, verbose_name="Проекция")
    property_var = models.ForeignKey('Property_var', on_delete=models.CASCADE, verbose_name="Вариант свойства")
    value = models.FloatField(default=0, verbose_name="Значение")
    def __str__(self):
        return str(self.projection.name) + ' ' + str(self.property_var.name)
    class Meta:
        verbose_name_plural = "Значения проекций"
        verbose_name = "Значение проекции"