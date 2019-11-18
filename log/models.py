from django.db import models
from tables.models import Material

class Material_log(models.Model):
    mat = models.ForeignKey('tables.Material', on_delete=models.CASCADE, verbose_name="Реактив")
    date = models.DateField(verbose_name="Дата")
    amount = models.FloatField(verbose_name="Количество")
    def __str__(self):
        return self.mat.name

class Operation(models.Model):
    name = models.CharField(max_length=80, verbose_name="Наименование")
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Операции"
        verbose_name = "Операция"

class Packaged(models.Model):
    rec = models.ForeignKey('Movement_rec', null=True, on_delete=models.CASCADE, verbose_name="Запись")
    amount = models.FloatField(null=True, verbose_name="Количество")
    def __str__(self):
        return "test"
    class Meta:
        verbose_name_plural = "Фасовки"
        verbose_name = "Фасовка"

class Movement_rec(models.Model):
    batch = models.ForeignKey('processes.Batch', null=True, on_delete=models.CASCADE, verbose_name="Партия")
    product = models.ForeignKey('tables.Product', null=True, on_delete=models.CASCADE, verbose_name="Продукт")
    amount = models.FloatField(null=True, verbose_name="Количество")
    date = models.DateField(auto_now_add=True, verbose_name="Дата")
    operation = models.ForeignKey('Operation', on_delete=models.CASCADE, verbose_name="Операция")
    is_printed = models.BooleanField(default = False, verbose_name="Напечатан паспорт?")
    def __str__(self):
        return str(self.product) + " " + str(self.date) + " " + str(self.operation)
    def get_batch(self):
        num = 'П-' + str(round(self.batch.kneading.batch_num))
        return num
    class Meta:
        verbose_name_plural = "Записи о перемещении"
        verbose_name = "Запись о перемещении"

class Packing_char(models.Model):
    char = models.ForeignKey('processes.Kneading_char_number', on_delete=models.CASCADE, verbose_name="Характеристика")
    packing = models.ForeignKey('Packing_divergence', on_delete=models.CASCADE, verbose_name="Фасовка")
    value = models.FloatField(verbose_name="Значение")
    def __str__(self):
        return str(self.packing.product) + " " + str(self.char)
    class Meta:
        verbose_name_plural = "Числовые характеристики фасовок"
        verbose_name = "Числовая характеристика фасовки"


class Packing_divergence(models.Model):
    reactor = models.ForeignKey('tables.Reactor', null=True, on_delete=models.CASCADE, verbose_name="Реактор")
    tank = models.ForeignKey('tables.Tank', null=True, on_delete=models.CASCADE, verbose_name="Танк")
    batch = models.ForeignKey('processes.Batch', on_delete=models.CASCADE, verbose_name="Партия")
    start_amm = models.FloatField(verbose_name="Начальное количество")
    pack_amm = models.FloatField(verbose_name="Фасуемое количество")
    date = models.DateField(auto_now_add=True, null=True, verbose_name="Дата")
    product = models.ForeignKey('tables.Product', on_delete=models.CASCADE, verbose_name="Продукт")
    prod_num = models.FloatField(verbose_name="Количество продуктов")
    pack_amm_set = models.CharField(max_length=80, null=True, blank=True, verbose_name="Множество фасуемых объёмов")
    def __str__(self):
        return str(self.date) + " " + str(self.product)
    def get_package_pass(self):
        amms = self.pack_amm_set.split('_')
        length = len(amms)
        i = 1
        res = self.product.production.composition.package + " по "
        for a in amms:
            res = res + a
            if i == length:
                res = res + " г"
            else:
                res = res + " или "
            i = i + 1
        return res
    class Meta:
        verbose_name_plural = "Разница в фасовке"
        verbose_name = "Разница в фасовке"


class Acceptance(models.Model):
    code = models.IntegerField(verbose_name="Код")
    prod = models.ForeignKey('Movement_rec', on_delete=models.CASCADE, verbose_name="Запись")
    date = models.DateField(auto_now_add=True, verbose_name="Дата")
    def __str__(self):
        return str(self.code)
    class Meta:
        verbose_name_plural = "Акты"
        verbose_name = "Акт"
