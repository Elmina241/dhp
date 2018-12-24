from django.db import models


#Классы модели МЦ
class Product_model(models.Model):
    name = models.CharField(max_length=200)
    group = models.ForeignKey('Model_group')
    def __str__(self):
        return self.name


class Model_unit(models.Model):
    model = models.ForeignKey('Product_model')
    unit = models.ForeignKey('tables.Unit')
    coeff = models.FloatField()
    is_base = models.BooleanField()
    def __str__(self):
        return self.unit.name

class Model_group(models.Model):
    name = models.CharField(max_length=200)
    parent = models.ForeignKey('Model_group', null = True)
    def __str__(self):
        return self.name

class Property(models.Model):
    name = models.CharField(max_length=200)
    prop_type = models.PositiveSmallIntegerField()
    visible = models.BooleanField()
    editable = models.BooleanField()
    default = models.CharField(max_length=200, null = True)
    def __str__(self):
        return self.name

class Property_range(Property):
    inf = models.FloatField()
    sup = models.FloatField()
    def __str__(self):
        return self.name

class Property_string(Property):
    text = models.CharField(max_length=500)
    def __str__(self):
        return self.text

class Property_var(models.Model):
    prop = models.ForeignKey('Property')
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Model_property(models.Model):
    model = models.ForeignKey('Product_model')
    prop = models.ForeignKey('Property')
    def __str__(self):
        return self.name

#Модели МЦ

class Goods(models.Model):
    model = models.ForeignKey('Product_model')
    base_unit = models.ForeignKey('tables.Unit')
    supply_price = models.FloatField()
    income_price = models.FloatField()
    def __str__(self):
        return self.model.name

class Goods_property(models.Model):
    product = models.ForeignKey('Goods')
    property = models.ForeignKey('Property')
    applicable = models.BooleanField()
    def __str__(self):
        return str(self.product) + " " + str(self.property)

class Property_num(Goods_property):
    number = models.FloatField()
    def __str__(self):
        return self.number

class Goods_string(Goods_property):
    text = models.CharField(max_length=500)
    def __str__(self):
        return self.text

class Goods_var(Goods_property):
    var = models.ForeignKey('Property_var')
    def __str__(self):
        return str(self.var)






