from django.db import models


# Модели для химвеществ
class Material_group(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Prefix(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Unit(models.Model):
    name = models.CharField(max_length=80)
    def __str__(self):
        return self.name

class Material(models.Model):
    code = models.CharField(max_length=80)
    name = models.CharField(max_length=80)
    group = models.ForeignKey('Material_group')
    prefix = models.ForeignKey('Prefix')
    mark = models.CharField(max_length=80)
    ammount = models.FloatField()
    unit = models.ForeignKey('Unit')
    concentration = models.FloatField()
    def __str__(self):
        full_name = ('' if self.prefix.name == 'отсутствует' else (self.prefix.name + ' ')) + self.name + ('' if self.mark == '-' else (' ' + self.mark))
        return full_name

# Модели для продукции
class Product_group(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Product_form(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Product_use(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Product_option(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Product_detail(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Product_mark(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Product(models.Model):
    code = models.CharField(max_length=13)
    name = models.CharField(max_length=80)
    group = models.ForeignKey('Product_group')
    form = models.ForeignKey('Product_form')
    use = models.ForeignKey('Product_use')
    option = models.ForeignKey('Product_option')
    detail = models.ForeignKey('Product_detail')
    mark = models.ForeignKey('Product_mark')
    def __str__(self):
        full_name = self.form.name + ' ' + self.use.name + ' ' + ('' if self.option.name == 'отсутствует' else (self.option.name + ' ')) + ('' if self.detail.name == 'отсутствует' else self.detail.name) + ' (' + self.mark.name + ')'
        return full_name
    def get_short_code(self):
        return self.code[9:]
