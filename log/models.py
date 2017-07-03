from django.db import models
from tables.models import Material

class Material_log(models.Model):
    mat = models.ForeignKey('tables.Material')
    date = models.DateField()
    amount = models.FloatField()
    def __str__(self):
        return self.mat.name
