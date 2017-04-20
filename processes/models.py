from django.db import models
from tables.models import Composition, Material, Formula, Reactor, Characteristic, Set_var

class Loading_list(models.Model):
    formula = models.ForeignKey('tables.Formula')
    ammount = models.FloatField()
    def __str__(self):
        return self.formula.get_name()

class List_component(models.Model):
    list = models.ForeignKey('Loading_list')
    mat = models.ForeignKey('tables.Material')
    ammount = models.FloatField()
    loaded = models.BooleanField(default = False)
    def __str__(self):
        return self.mat.name

class Kneading(models.Model):
    list = models.ForeignKey('Loading_list')
    start_date = models.DateField()
    finish_date = models.DateField()
    reactor = models.ForeignKey('tables.Reactor')
    def __str__(self):
        return self.list.formula.get_name()


class Batch(models.Model):
    kneading = models.OneToOneField('Kneading')
    def __str__(self):
        return self.id


# удалить
class Batch_characteristic(models.Model):
    batch = models.ForeignKey('Batch')
    #characteristic = models.ForeignKey('tables.Characteristic')
    def __str__(self):
        return self.batch

class State(models.Model):
    name = models.CharField(max_length=80)
    def __str__(self):
        return self.name

class State_log(models.Model):
    kneading = models.ForeignKey('Kneading')
    date = models.DateField(auto_now_add=True)
    state = models.ForeignKey('State')
    def __str__(self):
        return str(self.id) + ' ' + self.state.name + ' ' + str(self.date)
    def get_state(self):
        return self.state.name

# Модели для характеристик партии

class Kneading_char(models.Model):
    kneading = models.ForeignKey('Kneading')
    characteristic = models.ForeignKey('tables.Characteristic')
    def __str__(self):
        return self.characteristic.name
    def get_name(self):
        return self.kneading.name + ' ' + self.characteristic.name

class Kneading_char_number(Kneading_char):
    number = models.FloatField()
    def __str__(self):
        return self.get_name()

class Kneading_char_var(models.Model):
    kneading_char = models.ForeignKey('Kneading_char')
    char_var = models.ForeignKey('tables.Set_var')
    def __str__(self):
        return self.comp_char.get_name() + ' ' + self.char_var.name
