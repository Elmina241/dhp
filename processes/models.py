from django.db import models
from tables.models import Composition, Material, Formula, Reactor

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

class Characteristic_type(models.Model):
    name = models.CharField(max_length=80)
    def __str__(self):
        return self.name

class Characteristic(models.Model):
    name = models.CharField(max_length=80)
    type = models.ForeignKey('Characteristic_type')
    def __str__(self):
        return self.name

class Characteristic_set(Characteristic):
    var_name = models.CharField(max_length=80)
    def __str__(self):
        return self.var_name

class Characteristic_range(Characteristic):
    inf = models.FloatField()
    sup = models.FloatField()
    def __str__(self):
        return self.name

class Characteristic_number(Characteristic):
    number = models.FloatField()
    def __str__(self):
        return self.name

class Formula_characteristic(models.Model):
    formula = models.ForeignKey('tables.Formula')
    characteristic = models.ForeignKey('Characteristic')
    def __str__(self):
        return self.characteristic

class Batch(models.Model):
    kneading = models.OneToOneField('Kneading')
    def __str__(self):
        return self.id

class Batch_characteristic(models.Model):
    batch = models.ForeignKey('Batch')
    characteristic = models.ForeignKey('Characteristic')
    def __str__(self):
        return self.characteristic

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
