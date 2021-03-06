# Generated by Django 3.0.4 on 2020-03-15 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0014_auto_20200315_1339'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя')),
                ('surname', models.CharField(max_length=255, verbose_name='Фамилия')),
                ('mail', models.EmailField(max_length=254, verbose_name='Почта')),
                ('phone', models.CharField(max_length=255, verbose_name='Телефон')),
                ('place', models.IntegerField(verbose_name='Количество мест')),
            ],
        ),
    ]
