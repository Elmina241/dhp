# -*- coding: utf-8 -*-
from django.db import models
from tables.models import Composition, Compl_comp, Material, Formula, Reactor, Characteristic, Set_var


# Макет загрузочного листа. Объём компонентов в процентах
class Model_list(models.Model):
    formula = models.ForeignKey('tables.Formula', on_delete=models.CASCADE, verbose_name="Состав")

    def __str__(self):
        return self.formula.get_name()

    class Meta:
        verbose_name_plural = "Модели загрузочных листов"
        verbose_name = "Модель загрузочного листа"


class Model_component(models.Model):
    list = models.ForeignKey('Model_list', on_delete=models.CASCADE, verbose_name="Модель")
    formula = models.ForeignKey('tables.Formula', blank=True, default=None, null=True, on_delete=models.CASCADE,
                                verbose_name="Составной компонент")
    mat = models.ForeignKey('tables.Material', blank=True, default=None, null=True, on_delete=models.CASCADE,
                            verbose_name="Реактив")
    ammount = models.FloatField(verbose_name="Количество, %")

    def __str__(self):
        return self.mat.name

    class Meta:
        verbose_name_plural = "Компоненты моделей загрузочных листов"
        verbose_name = "Компонент модели загрузочного листа"


# Загрузочный лист
class Loading_list(models.Model):
    formula = models.ForeignKey('tables.Formula', on_delete=models.CASCADE, verbose_name="Состав")
    ammount = models.FloatField(verbose_name="Объём")

    def __str__(self):
        return self.formula.get_name()

    class Meta:
        verbose_name_plural = "Загрузочные листы"
        verbose_name = "Загрузочный лист"


class List_component(models.Model):
    list = models.ForeignKey('Loading_list', on_delete=models.CASCADE, verbose_name="Загрузочный лист")
    compl = models.ForeignKey('tables.Compl_comp', blank=True, default=None, null=True, on_delete=models.CASCADE,
                              verbose_name="Существующая технологическая композиция")
    formula = models.ForeignKey('tables.Formula', blank=True, default=None, null=True, on_delete=models.CASCADE,
                                verbose_name="Технологическая композиция собственного производства")
    r_cont = models.ForeignKey('Reactor_content', blank=True, default=None, null=True, on_delete=models.CASCADE,
                               verbose_name="Композиция из реактора")
    t_cont = models.ForeignKey('Tank_content', blank=True, default=None, null=True, on_delete=models.CASCADE,
                               verbose_name="Композиция из танка")
    mat = models.ForeignKey('tables.Material', blank=True, default=None, null=True, on_delete=models.CASCADE,
                            verbose_name="Реактив")
    min = models.FloatField(blank=True, default=None, null=True, verbose_name="Минимум")
    max = models.FloatField(blank=True, default=None, null=True, verbose_name="Максимум")
    ammount = models.FloatField(verbose_name="Количество")
    loaded = models.BooleanField(default=False, verbose_name="Загружена?")

    def __str__(self):
        return self.mat.name

    class Meta:
        verbose_name_plural = "Компоненты загрузочных листов"
        verbose_name = "Компонент загрузочного листа"


# Процесс смешения
class Kneading(models.Model):
    list = models.ForeignKey('Loading_list', on_delete=models.CASCADE, verbose_name="Загрузочный лист")
    batch_num = models.FloatField(default=0, verbose_name="Номер партии")
    start_date = models.DateField(verbose_name="Дата начала")
    finish_date = models.DateField(verbose_name="Дата завершения")
    reactor = models.ForeignKey('tables.Reactor', on_delete=models.CASCADE, verbose_name="Реактор")
    isValid = models.BooleanField(default=False, verbose_name="Соответствует контролю качества?")
    isFinished = models.BooleanField(default=False, verbose_name="Завершён?")

    def __str__(self):
        return self.list.formula.get_name()

    def get_state(self):
        log = State_log.objects.filter(kneading=self).last()
        name = log.get_state()
        return name

    def get_state_id(self):
        log = State_log.objects.filter(kneading=self).last()
        return log.state.id

    class Meta:
        verbose_name_plural = "Процессы смешения"
        verbose_name = "Процесс смешения"


# Партия
class Batch(models.Model):
    kneading = models.OneToOneField('Kneading', on_delete=models.CASCADE, verbose_name="Процесс смешения")
    finish_date = models.DateField(auto_now_add=True, verbose_name="Дата завершения")

    def __str__(self):
        return str(self.id) + " " + str(self.kneading.pk) + " " + str(self.kneading)

    class Meta:
        verbose_name_plural = "Партии"
        verbose_name = "Партия"


# Состав партии
class Batch_comp(models.Model):
    batch = models.ForeignKey('Batch', on_delete=models.CASCADE, verbose_name="Партия")
    mat = models.ForeignKey('tables.Material', on_delete=models.CASCADE, verbose_name="Реактив")
    ammount = models.FloatField(verbose_name="Количество")

    def __str__(self):
        return str(self.pk) + self.mat.name

    class Meta:
        verbose_name_plural = "Компоненты партий"
        verbose_name = "Компонент партии"


class State(models.Model):
    name = models.CharField(max_length=80, verbose_name="Наименование")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Статусы"
        verbose_name = "Статус"


class State_log(models.Model):
    kneading = models.ForeignKey('Kneading', on_delete=models.CASCADE, verbose_name="Смешение")
    date = models.DateField(auto_now_add=True, verbose_name="Дата")
    state = models.ForeignKey('State', on_delete=models.CASCADE, verbose_name="Статус")

    def __str__(self):
        return str(self.id) + ' ' + self.state.name + ' ' + str(self.date)

    def get_state(self):
        return self.state.name

    class Meta:
        verbose_name_plural = "Логи процессов"
        verbose_name = "Лог процесса"


# Модели для характеристик партии

class Kneading_char(models.Model):
    kneading = models.ForeignKey('Kneading', on_delete=models.CASCADE, verbose_name="Процесс")
    characteristic = models.ForeignKey('tables.Characteristic', on_delete=models.CASCADE, verbose_name="Характеристика")

    def __str__(self):
        return self.characteristic.name

    def get_name(self):
        return self.kneading.name + ' ' + self.characteristic.name

    class Meta:
        verbose_name_plural = "Характеристики процессов"
        verbose_name = "Характеристика процесса"


class Kneading_char_number(Kneading_char):
    number = models.FloatField(verbose_name="Число")

    def __str__(self):
        return self.get_name()

    class Meta:
        verbose_name_plural = "Числовые характеристики партий"
        verbose_name = "Числовая характеристика партии"


class Kneading_char_var(models.Model):
    kneading_char = models.ForeignKey('Kneading_char', on_delete=models.CASCADE, verbose_name="Характеристика партии")
    char_var = models.ForeignKey('tables.Set_var', on_delete=models.CASCADE, verbose_name="Вариант")

    def __str__(self):
        return self.comp_char.get_name() + ' ' + self.char_var.name

    class Meta:
        verbose_name_plural = "Варианты характеристик партий"
        verbose_name = "Вариант характеристики партии"


class Month_plan(models.Model):
    month = models.CharField(max_length=10, verbose_name="Месяц")
    prod = models.ForeignKey('tables.Product', on_delete=models.CASCADE, verbose_name="Продукт")
    num = models.FloatField(verbose_name="Количество")

    def __str__(self):
        return self.month + ' ' + str(self.prod)

    class Meta:
        verbose_name_plural = "Планы на месяц"
        verbose_name = "План на месяц"


# Модели для содержимого хранилищ
class Reactor_content(models.Model):
    reactor = models.ForeignKey('tables.Reactor', on_delete=models.CASCADE, verbose_name="Реактор")
    content_type = models.FloatField(default=3, verbose_name="Тип содержимого")
    reserved = models.FloatField(default=0, verbose_name="Зарезервирован?")
    amount = models.FloatField(verbose_name="Количество")
    date = models.DateField(auto_now_add=True, verbose_name="Дата")
    batch = models.ForeignKey('Batch', blank=True, default=None, null=True, on_delete=models.CASCADE,
                              verbose_name="Партия")
    kneading = models.ForeignKey('Kneading', blank=True, default=None, null=True, on_delete=models.CASCADE,
                                 verbose_name="Процесс смешения")

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

    class Meta:
        verbose_name_plural = "Содержимое реакторов"
        verbose_name = "Содержимое реактора"


class Tank_content(models.Model):
    tank = models.ForeignKey('tables.Tank', on_delete=models.CASCADE, verbose_name="Танк")
    content_type = models.FloatField(default=3, verbose_name="Тип содержимого")
    amount = models.FloatField(verbose_name="Количество")
    reserved = models.FloatField(default=0, verbose_name="Зарезервировано?")
    date = models.DateField(auto_now_add=True, verbose_name="Дата")
    batch = models.ForeignKey('Batch', blank=True, default=None, null=True, on_delete=models.CASCADE,
                              verbose_name="Партия")
    kneading = models.ForeignKey('Kneading', blank=True, default=None, null=True, on_delete=models.CASCADE,
                                 verbose_name="Процесс смешения")

    def __str__(self):
        return self.tank.code + ' ' + self.tank.name + ' ' + self.content_type

    def to_str(self):
        return str(self.tank.code + ' ' + self.tank.name + ' ' + str(self.content_type))

    class Meta:
        verbose_name_plural = "Содержимое танков"
        verbose_name = "Содержимое танка"


class Pack_process(models.Model):
    date = models.DateField(verbose_name="Дата")
    product = models.ForeignKey('tables.Product', on_delete=models.CASCADE, verbose_name="Продукт")
    amount = models.IntegerField(verbose_name="Количество")
    reactor = models.ForeignKey('tables.Reactor', null=True, on_delete=models.CASCADE, verbose_name="Реактор")
    tank = models.ForeignKey('tables.Tank', null=True, on_delete=models.CASCADE, verbose_name="Танк")
    finished = models.BooleanField(default=False, verbose_name="Завершено?")

    def __str__(self):
        return str(self.date) + " " + str(self.product)

    class Meta:
        verbose_name_plural = "Процессы фасовки"
        verbose_name = "Процесс фасовки"
