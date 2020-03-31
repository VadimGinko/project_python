# Generated by Django 3.0.4 on 2020-03-06 11:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0002_auto_20200306_1400'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tour',
            name='hotem',
        ),
        migrations.RemoveField(
            model_name='tour',
            name='prise',
        ),
        migrations.AddField(
            model_name='firm',
            name='firm_mail',
            field=models.EmailField(default='', max_length=254, verbose_name='Почта фирмы'),
        ),
        migrations.AddField(
            model_name='hotel',
            name='hotel_mail',
            field=models.EmailField(default='', max_length=254, verbose_name='Почта отеля'),
        ),
        migrations.AddField(
            model_name='tour',
            name='count_of_days',
            field=models.SmallIntegerField(default=0, verbose_name='Количество дней'),
        ),
        migrations.AddField(
            model_name='tour',
            name='hotel',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='tours.Hotel', verbose_name='Отель'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tour',
            name='price',
            field=models.IntegerField(default=0, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='firm',
            name='firm_adress',
            field=models.CharField(max_length=255, verbose_name='Адрес'),
        ),
        migrations.AlterField(
            model_name='firm',
            name='firm_name',
            field=models.CharField(max_length=255, unique=True, verbose_name='Название фирмы'),
        ),
        migrations.AlterField(
            model_name='firm',
            name='firm_phone',
            field=models.CharField(max_length=255, verbose_name='Контакты'),
        ),
        migrations.AlterField(
            model_name='firm',
            name='note',
            field=models.TextField(verbose_name='Страна'),
        ),
        migrations.AlterField(
            model_name='firm',
            name='working_hours',
            field=models.CharField(max_length=20, verbose_name='Время работы'),
        ),
        migrations.AlterField(
            model_name='firm',
            name='year_count',
            field=models.IntegerField(default=0, verbose_name='Количество лет работы'),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='bar_free',
            field=models.BooleanField(default=False, verbose_name='Наличие бесплатного бара'),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='beach',
            field=models.BooleanField(default=False, verbose_name='Наличие пляжа(рядом)'),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='hotel_name',
            field=models.CharField(max_length=255, unique=True, verbose_name='Название отеля'),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='pool',
            field=models.BooleanField(default=False, verbose_name='Наличие бассейна'),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='stars_count',
            field=models.IntegerField(default=0, verbose_name='Количество звёзд'),
        ),
        migrations.AlterField(
            model_name='tour',
            name='count_of_free_place',
            field=models.IntegerField(default=0, verbose_name='Количество свободных мест'),
        ),
        migrations.AlterField(
            model_name='tour',
            name='country',
            field=models.CharField(max_length=40, verbose_name='Страна'),
        ),
        migrations.AlterField(
            model_name='tour',
            name='departure_point',
            field=models.CharField(max_length=40, verbose_name='Место отправления'),
        ),
        migrations.AlterField(
            model_name='tour',
            name='firm',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tours.Firm', verbose_name='Фирма'),
        ),
        migrations.AlterField(
            model_name='tour',
            name='tour_finish',
            field=models.DateTimeField(verbose_name='Конец тура'),
        ),
        migrations.AlterField(
            model_name='tour',
            name='tour_name',
            field=models.CharField(max_length=255, unique=True, verbose_name='Название тура'),
        ),
        migrations.AlterField(
            model_name='tour',
            name='tour_start',
            field=models.DateTimeField(verbose_name='Начало тура'),
        ),
    ]
