from django.db import models
from tables.models import Material

class Material_log(models.Model):
    mat = models.ForeignKey('tables.Material')
    date = models.DateField()
    amount = models.FloatField()
    def __str__(self):
        return self.mat.name

class Operation(models.Model):
    name = models.CharField(max_length=80)
    def __str__(self):
        return self.name

class Movement_rec(models.Model):
    batch = models.ForeignKey('processes.Batch', null=True)
    amount = models.FloatField(null=True)
    date = models.DateField()
    operation = models.ForeignKey('Operation')
    def __str__(self):
        return str(date) + ' ' + str(self.batch)
