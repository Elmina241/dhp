# Generated by Django 2.2.1 on 2021-03-06 06:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='box_group',
            options={'verbose_name': 'Группа упаковки', 'verbose_name_plural': 'Группы упаковки'},
        ),
        migrations.AlterModelOptions(
            name='boxing',
            options={'verbose_name': 'Упаковка', 'verbose_name_plural': 'Упаковка'},
        ),
        migrations.AlterModelOptions(
            name='boxing_mat',
            options={'verbose_name': 'Материал упаковки', 'verbose_name_plural': 'Материалы упаковки'},
        ),
        migrations.AlterModelOptions(
            name='cap',
            options={'verbose_name': 'Укупорка', 'verbose_name_plural': 'Укупорка'},
        ),
        migrations.AlterModelOptions(
            name='cap_group',
            options={'verbose_name': 'Группа укупорки', 'verbose_name_plural': 'Группы укупорки'},
        ),
        migrations.AlterModelOptions(
            name='char_group',
            options={'verbose_name': 'Группа характеристики', 'verbose_name_plural': 'Группы характеристик'},
        ),
        migrations.AlterModelOptions(
            name='characteristic',
            options={'verbose_name': 'Характеристика', 'verbose_name_plural': 'Характеристики'},
        ),
        migrations.AlterModelOptions(
            name='characteristic_number',
            options={'verbose_name': 'Числовая характеристика', 'verbose_name_plural': 'Числовые характеристики'},
        ),
        migrations.AlterModelOptions(
            name='characteristic_range',
            options={'verbose_name': 'Диапазон характеристики', 'verbose_name_plural': 'Диапазоны характеристик'},
        ),
        migrations.AlterModelOptions(
            name='characteristic_set_var',
            options={'verbose_name': 'Вариант характеристики', 'verbose_name_plural': 'Варианты характеристик'},
        ),
        migrations.AlterModelOptions(
            name='characteristic_type',
            options={'verbose_name': 'Тип характеристики', 'verbose_name_plural': 'Типы характеристик'},
        ),
        migrations.AlterModelOptions(
            name='colour',
            options={'verbose_name': 'Цвет', 'verbose_name_plural': 'Цвета'},
        ),
        migrations.AlterModelOptions(
            name='comp_char_number',
            options={'verbose_name': 'Числовая характеристика композиций', 'verbose_name_plural': 'Числовые характеристики композиций'},
        ),
        migrations.AlterModelOptions(
            name='comp_char_range',
            options={'verbose_name': 'Диапазонная характеристика композиции', 'verbose_name_plural': 'Диапазонные характеристики композиций'},
        ),
        migrations.AlterModelOptions(
            name='comp_char_var',
            options={'verbose_name': 'Множественная характеристика композиции', 'verbose_name_plural': 'Множественные характеристики композиций'},
        ),
        migrations.AlterModelOptions(
            name='comp_prop_number',
            options={'verbose_name': 'Видовая числовая характеристика', 'verbose_name_plural': 'Видовые числовые характеристики'},
        ),
        migrations.AlterModelOptions(
            name='comp_prop_var',
            options={'verbose_name': 'Видовая множественная характеристика', 'verbose_name_plural': 'Видовые множественные характеристики'},
        ),
        migrations.AlterModelOptions(
            name='compl_comp',
            options={'verbose_name': 'Технологическая композиция', 'verbose_name_plural': 'Технологические композиции'},
        ),
        migrations.AlterModelOptions(
            name='compl_comp_comp',
            options={'verbose_name': 'Компонент технологической композиции', 'verbose_name_plural': 'Компоненты технологических композиций'},
        ),
        migrations.AlterModelOptions(
            name='components',
            options={'verbose_name': 'Компонент рецепта', 'verbose_name_plural': 'Компоненты рецептов'},
        ),
        migrations.AlterModelOptions(
            name='composition',
            options={'verbose_name': 'Рецепт', 'verbose_name_plural': 'Рецепты'},
        ),
        migrations.AlterModelOptions(
            name='composition_char',
            options={'verbose_name': 'Характеристика композиции', 'verbose_name_plural': 'Характеристики композиций'},
        ),
        migrations.AlterModelOptions(
            name='composition_group',
            options={'verbose_name': 'Группа рецептов', 'verbose_name_plural': 'Группы рецептов'},
        ),
        migrations.AlterModelOptions(
            name='container',
            options={'verbose_name': 'Тара', 'verbose_name_plural': 'Тара'},
        ),
        migrations.AlterModelOptions(
            name='container_group',
            options={'verbose_name': 'Группа тары', 'verbose_name_plural': 'Группы тары'},
        ),
        migrations.AlterModelOptions(
            name='container_mat',
            options={'verbose_name': 'Материал тары', 'verbose_name_plural': 'Материалы тары'},
        ),
        migrations.AlterModelOptions(
            name='formula',
            options={'verbose_name': 'Вариант состава', 'verbose_name_plural': 'Варианты составов'},
        ),
        migrations.AlterModelOptions(
            name='formula_component',
            options={'verbose_name': 'Компонент состава', 'verbose_name_plural': 'Компоненты составов'},
        ),
        migrations.AlterModelOptions(
            name='mat_char_number',
            options={'verbose_name': 'Группа реактива', 'verbose_name_plural': 'Группы реактивов'},
        ),
        migrations.AlterModelOptions(
            name='mat_char_var',
            options={'verbose_name': 'Группа реактива', 'verbose_name_plural': 'Группы реактивов'},
        ),
        migrations.AlterModelOptions(
            name='material',
            options={'verbose_name': 'Реактив', 'verbose_name_plural': 'Реактивы'},
        ),
        migrations.AlterModelOptions(
            name='material_char',
            options={'verbose_name': 'Группа реактива', 'verbose_name_plural': 'Группы реактивов'},
        ),
        migrations.AlterModelOptions(
            name='material_group',
            options={'verbose_name': 'Группа реактива', 'verbose_name_plural': 'Группы реактивов'},
        ),
        migrations.AlterModelOptions(
            name='prefix',
            options={'verbose_name': 'Префикс', 'verbose_name_plural': 'Префиксы'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Продукция', 'verbose_name_plural': 'Продукция'},
        ),
        migrations.AlterModelOptions(
            name='product_form',
            options={'verbose_name': 'Форма продукции', 'verbose_name_plural': 'Формы продукции'},
        ),
        migrations.AlterModelOptions(
            name='product_group',
            options={'verbose_name': 'Группа продукции', 'verbose_name_plural': 'Группы продукции'},
        ),
        migrations.AlterModelOptions(
            name='product_mark',
            options={'verbose_name': 'Марка продукции', 'verbose_name_plural': 'Марки продукции'},
        ),
        migrations.AlterModelOptions(
            name='product_use',
            options={'verbose_name': 'Назначение продукции', 'verbose_name_plural': 'Назначения продукции'},
        ),
        migrations.AlterModelOptions(
            name='production',
            options={'verbose_name': 'Комплект', 'verbose_name_plural': 'Комплекты'},
        ),
        migrations.AlterModelOptions(
            name='reactor',
            options={'verbose_name': 'Реактор', 'verbose_name_plural': 'Реакторы'},
        ),
        migrations.AlterModelOptions(
            name='set_var',
            options={'verbose_name': 'Вариант', 'verbose_name_plural': 'Варианты характеристик типа Множество'},
        ),
        migrations.AlterModelOptions(
            name='sticker',
            options={'verbose_name': 'Этикетка', 'verbose_name_plural': 'Этикетки'},
        ),
        migrations.AlterModelOptions(
            name='sticker_part',
            options={'verbose_name': 'Часть этикетки', 'verbose_name_plural': 'Части этикетки'},
        ),
        migrations.AlterModelOptions(
            name='tank',
            options={'verbose_name': 'Танк', 'verbose_name_plural': 'Танки'},
        ),
        migrations.AlterModelOptions(
            name='unit',
            options={'verbose_name': 'Единица измерения', 'verbose_name_plural': 'Единицы измерения'},
        ),
        migrations.AddField(
            model_name='boxing',
            name='price',
            field=models.FloatField(default=0, verbose_name='Цена'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cap',
            name='price',
            field=models.FloatField(default=0, verbose_name='Цена'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='container',
            name='price',
            field=models.FloatField(default=0, verbose_name='Цена'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sticker',
            name='price',
            field=models.FloatField(default=0, verbose_name='Цена'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='box_group',
            name='name',
            field=models.CharField(max_length=80, verbose_name='Наименование'),
        ),
        migrations.AlterField(
            model_name='boxing',
            name='code',
            field=models.CharField(max_length=80, verbose_name='Артикул'),
        ),
        migrations.AlterField(
            model_name='boxing',
            name='colour',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tables.Colour', verbose_name='Цвет'),
        ),
        migrations.AlterField(
            model_name='boxing',
            name='form',
            field=models.CharField(max_length=80, verbose_name='Форма'),
        ),
        migrations.AlterField(
            model_name='boxing',
            name='group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tables.Box_group', verbose_name='Группа'),
        ),
        migrations.AlterField(
            model_name='boxing',
            name='mat',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tables.Boxing_mat', verbose_name='Материал'),
        ),
        migrations.AlterField(
            model_name='boxing_mat',
            name='name',
            field=models.CharField(max_length=80, verbose_name='Наименование'),
        ),
        migrations.AlterField(
            model_name='cap',
            name='code',
            field=models.CharField(max_length=80, verbose_name='Наименование'),
        ),
        migrations.AlterField(
            model_name='cap',
            name='colour',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tables.Colour', verbose_name='Цвет'),
        ),
        migrations.AlterField(
            model_name='cap',
            name='form',
            field=models.CharField(max_length=80, verbose_name='Форма'),
        ),
        migrations.AlterField(
            model_name='cap',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tables.Cap_group', verbose_name='Группа'),
        ),
        migrations.AlterField(
            model_name='cap',
            name='mat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tables.Container_mat', verbose_name='Материал'),
        ),
        migrations.AlterField(
            model_name='cap_group',
            name='name',
            field=models.CharField(max_length=80, verbose_name='Наименование'),
        ),
        migrations.AlterField(
            model_name='char_group',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Наименование'),
        ),
        migrations.AlterField(
            model_name='characteristic',
            name='char_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='tables.Characteristic_type', verbose_name='Тип'),
        ),
        migrations.AlterField(
            model_name='characteristic',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tables.Char_group', verbose_name='Группа'),
        ),
        migrations.AlterField(
            model_name='characteristic',
            name='is_general',
            field=models.BooleanField(default=True, verbose_name='Видовое свойство?'),
        ),
        migrations.AlterField(
            model_name='characteristic',
            name='name',
            field=models.CharField(max_length=80, verbose_name='Наименование'),
        ),
        migrations.AlterField(
            model_name='characteristic_number',
            name='inf',
            field=models.FloatField(verbose_name='Минимум'),
        ),
        migrations.AlterField(
            model_name='characteristic_number',
            name='sup',
            field=models.FloatField(verbose_name='Максимум'),
        ),
        migrations.AlterField(
            model_name='characteristic_range',
            name='inf',
            field=models.FloatField(verbose_name='Минимум'),
        ),
        migrations.AlterField(
            model_name='characteristic_range',
            name='sup',
            field=models.FloatField(verbose_name='Максимум'),
        ),
        migrations.AlterField(
            model_name='characteristic_set_var',
            name='char_set',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tables.Characteristic', verbose_name='Характеристика'),
        ),
        migrations.AlterField(
            model_name='characteristic_set_var',
            name='char_var',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tables.Set_var', verbose_name='Вариант'),
        ),
        migrations.AlterField(
            model_name='characteristic_type',
            name='name',
            field=models.CharField(max_length=80, verbose_name='Наименование'),
        ),
        migrations.AlterField(
            model_name='colour',
            name='name',
            field=models.CharField(max_length=80, verbose_name='Наименование'),
        ),
        migrations.AlterField(
            model_name='comp_char_number',
            name='number',
            field=models.FloatField(verbose_name='Число'),
        ),
        migrations.AlterField(
            model_name='comp_char_range',
            name='inf',
            field=models.FloatField(verbose_name='Минимум'),
        ),
        migrations.AlterField(
            model_name='comp_char_range',
            name='sup',
            field=models.FloatField(verbose_name='Максимум'),
        ),
        migrations.AlterField(
            model_name='comp_char_var',
            name='char_var',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tables.Set_var', verbose_name='Вариант'),
        ),
        migrations.AlterField(
            model_name='comp_char_var',
            name='comp_char',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tables.Composition_char', verbose_name='Характеристика'),
        ),
        migrations.AlterField(
            model_name='comp_prop_number',
            name='number',
            field=models.FloatField(verbose_name='Число'),
        ),
        migrations.AlterField(
            model_name='comp_prop_var',
            name='char_var',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tables.Set_var', verbose_name='Вариант'),
        ),
        migrations.AlterField(
            model_name='comp_prop_var',
            name='comp_prop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tables.Composition_char', verbose_name='Характеристика'),
        ),
        migrations.AlterField(
            model_name='compl_comp',
            name='ammount',
            field=models.FloatField(verbose_name='Количество'),
        ),
        migrations.AlterField(
            model_name='compl_comp',
            name='code',
            field=models.CharField(max_length=80, verbose_name='Артикул'),
        ),
        migrations.AlterField(
            model_name='compl_comp',
            name='form',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tables.Product_form', verbose_name='Форма'),
        ),
        migrations.AlterField(
            model_name='compl_comp',
            name='formula',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='tables.Formula', verbose_name='Состав'),
        ),
        migrations.AlterField(
            model_name='compl_comp',
            name='name',
            field=models.CharField(max_length=80, verbose_name='Наименование'),
        ),
        migrations.AlterField(
            model_name='compl_comp',
            name='reserved',
            field=models.FloatField(default=0, verbose_name='Зарезервировано'),
        ),
        migrations.AlterField(
            model_name='compl_comp',
            name='store_amount',
            field=models.FloatField(default=0, verbose_name='Количество в упаковке'),
        ),
        migrations.AlterField(
            model_name='compl_comp_comp',
            name='ammount',
            field=models.FloatField(verbose_name='Количество'),
        ),
        migrations.AlterField(
            model_name='compl_comp_comp',
            name='compl',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tables.Compl_comp', verbose_name='Технологическая композиция'),
        ),
        migrations.AlterField(
            model_name='compl_comp_comp',
            name='mat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tables.Material', verbose_name='Реактив'),
        ),
        migrations.AlterField(
            model_name='components',
            name='comp',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tables.Composition', verbose_name='Рецепт'),
        ),
        migrations.AlterField(
            model_name='components',
            name='mat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tables.Material', verbose_name='Реактив'),
        ),
        migrations.AlterField(
            model_name='components',
            name='max',
            field=models.FloatField(verbose_name='Макс. %'),
        ),
        migrations.AlterField(
            model_name='components',
            name='min',
            field=models.FloatField(verbose_name='Мин. %'),
        ),
        migrations.AlterField(
            model_name='composition',
            name='certificate',
            field=models.CharField(max_length=80, null=True, verbose_name='Свидетельство о гос. регистрации'),
        ),
        migrations.AlterField(
            model_name='composition',
            name='code',
            field=models.CharField(max_length=80, verbose_name='Код'),
        ),
        migrations.AlterField(
            model_name='composition',
            name='cur_batch',
            field=models.FloatField(default=1, verbose_name='Текущий номер партии'),
        ),
        migrations.AlterField(
            model_name='composition',
            name='date',
            field=models.DateField(null=True, verbose_name='Дата СГР'),
        ),
        migrations.AlterField(
            model_name='composition',
            name='declaration',
            field=models.CharField(max_length=80, null=True, verbose_name='Требования качества продукции'),
        ),
        migrations.AlterField(
            model_name='composition',
            name='form',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tables.Product_form', verbose_name='Форма'),
        ),
        migrations.AlterField(
            model_name='composition',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tables.Composition_group', verbose_name='Группа'),
        ),
        migrations.AlterField(
            model_name='composition',
            name='isFinal',
            field=models.BooleanField(default=True, verbose_name='Не технологическая?'),
        ),
        migrations.AlterField(
            model_name='composition',
            name='name',
            field=models.CharField(max_length=80, verbose_name='Наименование'),
        ),
        migrations.AlterField(
            model_name='composition',
            name='package',
            field=models.CharField(max_length=80, null=True, verbose_name='Упаковка'),
        ),
        migrations.AlterField(
            model_name='composition',
            name='sgr',
            field=models.CharField(max_length=80, verbose_name='СГР'),
        ),
        migrations.AlterField(
            model_name='composition',
            name='sh_life',
            field=models.IntegerField(default=24, verbose_name='Срок годности'),
        ),
        migrations.AlterField(
            model_name='composition',
            name='standard',
            field=models.CharField(max_length=80, null=True, verbose_name='Стандарт'),
        ),
        migrations.AlterField(
            model_name='composition_char',
            name='characteristic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tables.Characteristic', verbose_name='Характеристика'),
        ),
        migrations.AlterField(
            model_name='composition_char',
            name='comp',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tables.Composition', verbose_name='Рецепт'),
        ),
        migrations.AlterField(
            model_name='composition_group',
            name='name',
            field=models.CharField(max_length=80, verbose_name='Наименование'),
        ),
        migrations.AlterField(
            model_name='container',
            name='code',
            field=models.CharField(max_length=80, verbose_name='Наименование'),
        ),
        migrations.AlterField(
            model_name='container',
            name='colour',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tables.Colour', verbose_name='Цвет'),
        ),
        migrations.AlterField(
            model_name='container',
            name='form',
            field=models.CharField(max_length=80, verbose_name='Форма'),
        ),
        migrations.AlterField(
            model_name='container',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tables.Container_group', verbose_name='Группа'),
        ),
        migrations.AlterField(
            model_name='container',
            name='mat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tables.Container_mat', verbose_name='Материал'),
        ),
        migrations.AlterField(
            model_name='container_group',
            name='name',
            field=models.CharField(max_length=80, verbose_name='Наименование'),
        ),
        migrations.AlterField(
            model_name='container_mat',
            name='name',
            field=models.CharField(max_length=80, verbose_name='Наименование'),
        ),
        migrations.AlterField(
            model_name='formula',
            name='code',
            field=models.CharField(max_length=80, verbose_name='Код'),
        ),
        migrations.AlterField(
            model_name='formula',
            name='composition',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tables.Composition', verbose_name='Рецепт'),
        ),
        migrations.AlterField(
            model_name='formula',
            name='cur_batch',
            field=models.FloatField(default=1, verbose_name='Текущая партия'),
        ),
        migrations.AlterField(
            model_name='formula',
            name='name',
            field=models.CharField(max_length=80, null=True, verbose_name='Краткое наименование'),
        ),
        migrations.AlterField(
            model_name='formula_component',
            name='ammount',
            field=models.FloatField(verbose_name='Количество'),
        ),
        migrations.AlterField(
            model_name='formula_component',
            name='formula',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tables.Formula', verbose_name='Состав'),
        ),
        migrations.AlterField(
            model_name='formula_component',
            name='mat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tables.Material', verbose_name='Реактив'),
        ),
        migrations.AlterField(
            model_name='mat_char_number',
            name='number',
            field=models.FloatField(verbose_name='Наименование'),
        ),
        migrations.AlterField(
            model_name='mat_char_var',
            name='char_var',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tables.Set_var', verbose_name='Наименование'),
        ),
        migrations.AlterField(
            model_name='mat_char_var',
            name='mat_char',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tables.Material_char', verbose_name='Наименование'),
        ),
        migrations.AlterField(
            model_name='material',
            name='ammount',
            field=models.FloatField(verbose_name='Количество'),
        ),
        migrations.AlterField(
            model_name='material',
            name='code',
            field=models.CharField(max_length=80, verbose_name='Артикул'),
        ),
        migrations.AlterField(
            model_name='material',
            name='concentration',
            field=models.FloatField(verbose_name='Концентрация'),
        ),
        migrations.AlterField(
            model_name='material',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tables.Material_group', verbose_name='Группа'),
        ),
        migrations.AlterField(
            model_name='material',
            name='mark',
            field=models.CharField(max_length=80, verbose_name='Марка'),
        ),
        migrations.AlterField(
            model_name='material',
            name='name',
            field=models.CharField(max_length=80, verbose_name='Наименование'),
        ),
        migrations.AlterField(
            model_name='material',
            name='prefix',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tables.Prefix', verbose_name='Префикс'),
        ),
        migrations.AlterField(
            model_name='material',
            name='price',
            field=models.FloatField(verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='material',
            name='reserved',
            field=models.FloatField(default=0, verbose_name='Зарезервировано'),
        ),
        migrations.AlterField(
            model_name='material',
            name='unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tables.Unit', verbose_name='Ед. изм.'),
        ),
        migrations.AlterField(
            model_name='material_char',
            name='characteristic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tables.Characteristic', verbose_name='Наименование'),
        ),
        migrations.AlterField(
            model_name='material_char',
            name='mat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tables.Material', verbose_name='Наименование'),
        ),
        migrations.AlterField(
            model_name='material_group',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Наименование'),
        ),
        migrations.AlterField(
            model_name='prefix',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Наименование'),
        ),
        migrations.AlterField(
            model_name='product',
            name='code',
            field=models.CharField(max_length=13, verbose_name='Артикул'),
        ),
        migrations.AlterField(
            model_name='product',
            name='detail',
            field=models.CharField(max_length=80, verbose_name='Уточнение'),
        ),
        migrations.AlterField(
            model_name='product',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tables.Product_group', verbose_name='Группа'),
        ),
        migrations.AlterField(
            model_name='product',
            name='mark',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tables.Product_mark', verbose_name='Марка'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=80, verbose_name='Наименование'),
        ),
        migrations.AlterField(
            model_name='product',
            name='option',
            field=models.CharField(max_length=80, verbose_name='Варианты'),
        ),
        migrations.AlterField(
            model_name='product',
            name='production',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='tables.Production', verbose_name='Комплект'),
        ),
        migrations.AlterField(
            model_name='product',
            name='use',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tables.Product_use', verbose_name='Назначение'),
        ),
        migrations.AlterField(
            model_name='product_form',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Наименование'),
        ),
        migrations.AlterField(
            model_name='product_group',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Наименование'),
        ),
        migrations.AlterField(
            model_name='product_mark',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Наименование'),
        ),
        migrations.AlterField(
            model_name='product_use',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Наименование'),
        ),
        migrations.AlterField(
            model_name='production',
            name='boxing',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tables.Boxing', verbose_name='Упаковка'),
        ),
        migrations.AlterField(
            model_name='production',
            name='boxingAmount',
            field=models.FloatField(default=0, verbose_name='Количество упаковки'),
        ),
        migrations.AlterField(
            model_name='production',
            name='boxingUnit',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='boxing_unit', to='tables.Unit', verbose_name='Ед. изм. упаковки'),
        ),
        migrations.AlterField(
            model_name='production',
            name='cap',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tables.Cap', verbose_name='Укупорка'),
        ),
        migrations.AlterField(
            model_name='production',
            name='capAmount',
            field=models.FloatField(default=0, verbose_name='Количество укупорок'),
        ),
        migrations.AlterField(
            model_name='production',
            name='capUnit',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cap_unit', to='tables.Unit', verbose_name='Ед. изм. укупорок'),
        ),
        migrations.AlterField(
            model_name='production',
            name='compAmount',
            field=models.FloatField(default=0, verbose_name='Количество композиции'),
        ),
        migrations.AlterField(
            model_name='production',
            name='compUnit',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tables.Unit', verbose_name='Ед. изм. композиции'),
        ),
        migrations.AlterField(
            model_name='production',
            name='composition',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tables.Composition', verbose_name='Рецепт'),
        ),
        migrations.AlterField(
            model_name='production',
            name='contAmount',
            field=models.FloatField(default=0, verbose_name='Количество тары'),
        ),
        migrations.AlterField(
            model_name='production',
            name='contUnit',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cont_unit', to='tables.Unit', verbose_name='Ед. изм. тары'),
        ),
        migrations.AlterField(
            model_name='production',
            name='container',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tables.Container', verbose_name='Тара'),
        ),
        migrations.AlterField(
            model_name='production',
            name='sticker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tables.Sticker', verbose_name='Этикетка'),
        ),
        migrations.AlterField(
            model_name='production',
            name='stickerAmount',
            field=models.FloatField(default=0, verbose_name='Количество этикеток'),
        ),
        migrations.AlterField(
            model_name='production',
            name='stickerUnit',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sticker_unit', to='tables.Unit', verbose_name='Ед. изм. этикеток'),
        ),
        migrations.AlterField(
            model_name='reactor',
            name='code',
            field=models.CharField(max_length=80, verbose_name='Артикул'),
        ),
        migrations.AlterField(
            model_name='reactor',
            name='location',
            field=models.CharField(max_length=80, verbose_name='Расположение'),
        ),
        migrations.AlterField(
            model_name='reactor',
            name='max',
            field=models.FloatField(verbose_name='Макс.'),
        ),
        migrations.AlterField(
            model_name='reactor',
            name='min',
            field=models.FloatField(verbose_name='Мин.'),
        ),
        migrations.AlterField(
            model_name='reactor',
            name='name',
            field=models.CharField(max_length=80, verbose_name='Наименование'),
        ),
        migrations.AlterField(
            model_name='reactor',
            name='product',
            field=models.CharField(max_length=250, verbose_name='Продукция'),
        ),
        migrations.AlterField(
            model_name='reactor',
            name='ready',
            field=models.BooleanField(verbose_name='Готов?'),
        ),
        migrations.AlterField(
            model_name='set_var',
            name='name',
            field=models.CharField(max_length=80, verbose_name='Наименование'),
        ),
        migrations.AlterField(
            model_name='sticker',
            name='code',
            field=models.CharField(max_length=80, verbose_name='Артикул'),
        ),
        migrations.AlterField(
            model_name='sticker',
            name='part',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tables.Sticker_part', verbose_name='Часть'),
        ),
        migrations.AlterField(
            model_name='sticker',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tables.Product', verbose_name='Продукт'),
        ),
        migrations.AlterField(
            model_name='sticker_part',
            name='name',
            field=models.CharField(max_length=80, verbose_name='Наименование'),
        ),
        migrations.AlterField(
            model_name='tank',
            name='capacity',
            field=models.FloatField(verbose_name='Объём'),
        ),
        migrations.AlterField(
            model_name='tank',
            name='code',
            field=models.CharField(max_length=80, verbose_name='Артикул'),
        ),
        migrations.AlterField(
            model_name='tank',
            name='name',
            field=models.CharField(max_length=80, verbose_name='Наименование'),
        ),
        migrations.AlterField(
            model_name='tank',
            name='ready',
            field=models.BooleanField(verbose_name='Готов?'),
        ),
        migrations.AlterField(
            model_name='unit',
            name='name',
            field=models.CharField(max_length=80, verbose_name='Наименование'),
        ),
    ]
