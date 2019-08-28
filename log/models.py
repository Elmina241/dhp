from django.db import models
from tables.models import Material

class Material_log(models.Model):
    mat = models.ForeignKey('tables.Material', on_delete=models.CASCADE)
    date = models.DateField()
    amount = models.FloatField()
    def __str__(self):
        return self.mat.name

class Operation(models.Model):
    name = models.CharField(max_length=80)
    def __str__(self):
        return self.name

class Packaged(models.Model):
    rec = models.ForeignKey('Movement_rec', null=True, on_delete=models.CASCADE)
    amount = models.FloatField(null=True)
    def __str__(self):
        return "test"

class Movement_rec(models.Model):
    batch = models.ForeignKey('processes.Batch', null=True, on_delete=models.CASCADE)
    product = models.ForeignKey('tables.Product', null=True, on_delete=models.CASCADE)
    amount = models.FloatField(null=True)
    date = models.DateField(auto_now_add=True)
    operation = models.ForeignKey('Operation', on_delete=models.CASCADE)
    is_printed = models.BooleanField(default = False)
    def __str__(self):
        return str(self.product) + " " + str(self.date) + " " + str(self.operation)
    def get_batch(self):
        num = 'П-' + str(round(self.batch.kneading.batch_num))
        return num

class Packing_divergence(models.Model):
    reactor = models.ForeignKey('tables.Reactor', null=True, on_delete=models.CASCADE)
    tank = models.ForeignKey('tables.Tank', null=True, on_delete=models.CASCADE)
    batch = models.ForeignKey('processes.Batch', on_delete=models.CASCADE)
    start_amm = models.FloatField()
    pack_amm = models.FloatField()
    date = models.DateField(auto_now_add=True, null=True)
    product = models.ForeignKey('tables.Product', on_delete=models.CASCADE)
    prod_num = models.FloatField()
    pack_amm_set = models.CharField(max_length=80)
    def __str__(self):
        return "test"

class Acceptance(models.Model):
    code = models.IntegerField()
    prod = models.ForeignKey('Movement_rec', on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    def __str__(self):
        return str(self.code)
