# -*- coding: utf-8 -*-
from django.db import models
from tables.models import Composition, Compl_comp, Material, Formula, Reactor, Characteristic, Set_var

#Макет загрузочного листа. Объём компонентов в процентах
class Model_list(models.Model):
    formula = models.ForeignKey('tables.Formula', on_delete=models.CASCADE)
    def __str__(self):
        return self.formula.get_name()

class Model_component(models.Model):
    list = models.ForeignKey('Model_list', on_delete=models.CASCADE)
    #compl = models.ForeignKey('tables.Compl_comp', blank=True, default = None, null=True)
    formula = models.ForeignKey('tables.Formula', blank=True, default = None, null=True, on_delete=models.CASCADE)
    mat = models.ForeignKey('tables.Material', blank=True, default = None, null=True, on_delete=models.CASCADE)
    ammount = models.FloatField()
    #min = models.FloatField(blank=True, default = 0, null=True)
    #max = models.FloatField(blank=True, default=0, null=True)
    def __str__(self):
        return self.mat.name

#Загрузочный лист
class Loading_list(models.Model):
    formula = models.ForeignKey('tables.Formula', on_delete=models.CASCADE)
    ammount = models.FloatField()
    def __str__(self):
        return self.formula.get_name()

class List_component(models.Model):
    list = models.ForeignKey('Loading_list', on_delete=models.CASCADE)
    compl = models.ForeignKey('tables.Compl_comp', blank=True, default = None, null=True, on_delete=models.CASCADE)
    formula = models.ForeignKey('tables.Formula', blank=True, default = None, null=True, on_delete=models.CASCADE)
    r_cont = models.ForeignKey('Reactor_content', blank=True, default = None, null=True, on_delete=models.CASCADE)
    t_cont = models.ForeignKey('Tank_content', blank=True, default = None, null=True, on_delete=models.CASCADE)
    mat = models.ForeignKey('tables.Material', blank=True, default = None, null=True, on_delete=models.CASCADE)
    min = models.FloatField(blank=True, default = None, null=True)
    max = models.FloatField(blank=True, default = None, null=True)
    ammount = models.FloatField()
    loaded = models.BooleanField(default = False)
    def __str__(self):
        return self.mat.name

#Процесс смешения
class Kneading(models.Model):
    list = models.ForeignKey('Loading_list', on_delete=models.CASCADE)
    batch_num = models.FloatField(default = 0)
    start_date = models.DateField()
    finish_date = models.DateField()
    reactor = models.ForeignKey('tables.Reactor', on_delete=models.CASCADE)
    isValid = models.BooleanField(default = False)
    isFinished = models.BooleanField(default = False)
    def __str__(self):
        return self.list.formula.get_name()
    def get_state(self):
        log = State_log.objects.filter(kneading = self).last()
        name = log.get_state()
        return name
    def get_state_id(self):
        log = State_log.objects.filter(kneading = self).last()
        return log.state.id

#Партия
class Batch(models.Model):
    kneading = models.OneToOneField('Kneading', on_delete=models.CASCADE)
    finish_date = models.DateField(auto_now_add=True)
    def __str__(self):
        return str(self.id) + " " + str(self.kneading.pk) + " " + str(self.kneading)

#Состав партии
class Batch_comp(models.Model):
    batch = models.ForeignKey('Batch', on_delete=models.CASCADE)
    mat = models.ForeignKey('tables.Material', on_delete=models.CASCADE)
    ammount = models.FloatField()
    def __str__(self):
        return str(self.pk) + self.mat.name


class State(models.Model):
    name = models.CharField(max_length=80)
    def __str__(self):
        return self.name

class State_log(models.Model):
    kneading = models.ForeignKey('Kneading', on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    state = models.ForeignKey('State', on_delete=models.CASCADE)
    def __str__(self):
        return str(self.id) + ' ' + self.state.name + ' ' + str(self.date)
    def get_state(self):
        return self.state.name

# Модели для характеристик партии

class Kneading_char(models.Model):
    kneading = models.ForeignKey('Kneading', on_delete=models.CASCADE)
    characteristic = models.ForeignKey('tables.Characteristic', on_delete=models.CASCADE)
    def __str__(self):
        return self.characteristic.name
    def get_name(self):
        return self.kneading.name + ' ' + self.characteristic.name

class Kneading_char_number(Kneading_char):
    number = models.FloatField()
    def __str__(self):
        return self.get_name()

class Kneading_char_var(models.Model):
    kneading_char = models.ForeignKey('Kneading_char', on_delete=models.CASCADE)
    char_var = models.ForeignKey('tables.Set_var', on_delete=models.CASCADE)
    def __str__(self):
        return self.comp_char.get_name() + ' ' + self.char_var.name

class Month_plan(models.Model):
    month = models.CharField(max_length=10)
    prod = models.ForeignKey('tables.Product', on_delete=models.CASCADE)
    num = models.FloatField()
    def __str__(self):
        return self.month + ' ' + str(self.prod)

#Модели для содержимого хранилищ
class Reactor_content(models.Model):
    reactor = models.ForeignKey('tables.Reactor', on_delete=models.CASCADE)
    content_type = models.FloatField(default = 3)
    reserved = models.FloatField(default = 0)
    amount = models.FloatField()
    date = models.DateField(auto_now_add=True)
    batch = models.ForeignKey('Batch', blank=True, default = None, null=True, on_delete=models.CASCADE)
    kneading = models.ForeignKey('Kneading', blank=True, default = None, null=True, on_delete=models.CASCADE)
    def __str__(self):
        return self.reactor.code + ' ' + self.reactor.name + ' ' + self.content_type
    def to_str(self):
        return str(self.reactor.code + ' ' + self.reactor.name + ' ' + str(self.content_type))
    def get_formula_id(self):
        if self.content_type == 3:
            return None
        else:
            if self.content_type == 1:
                return self.batch.kneading.list.formula.pk
            else:
                return self.kneading.list.formula.pk

class Tank_content(models.Model):
    tank = models.ForeignKey('tables.Tank', on_delete=models.CASCADE)
    content_type = models.FloatField(default = 3)
    amount = models.FloatField()
    reserved = models.FloatField(default = 0)
    date = models.DateField(auto_now_add=True)
    batch = models.ForeignKey('Batch', blank=True, default = None, null=True, on_delete=models.CASCADE)
    kneading = models.ForeignKey('Kneading', blank=True, default = None, null=True, on_delete=models.CASCADE)
    def __str__(self):
        return self.tank.code + ' ' + self.tank.name + ' ' + self.content_type
    def to_str(self):
        return str(self.tank.code + ' ' + self.tank.name + ' ' + str(self.content_type))

class Pack_process(models.Model):
    date = models.DateField()
    product = models.ForeignKey('tables.Product', on_delete=models.CASCADE)
    amount = models.IntegerField()
    reactor = models.ForeignKey('tables.Reactor', null=True, on_delete=models.CASCADE)
    tank = models.ForeignKey('tables.Tank', null=True, on_delete=models.CASCADE)
    finished = models.BooleanField(default = False)
    def __str__(self):
        return str(self.date) + " " + str(self.product)
