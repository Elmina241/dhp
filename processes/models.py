from django.db import models
from tables.models import Composition, Material

class Loading_list(models.Model):
    date = models.DateField()
    composition = models.ForeignKey('tables.Composition')
    ammount = models.FloatField()
    def __str__(self):
        return self.composition.name

class List_component(models.Model):
    list = models.ForeignKey('Loading_list')
    mat = models.ForeignKey('tables.Material')
    ammount = models.FloatField()
    def __str__(self):
        return self.mat.name
