# Generated by Django 3.0.4 on 2020-03-06 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0004_auto_20200306_1440'),
    ]

    operations = [
        migrations.AlterField(
            model_name='firm',
            name='note',
            field=models.TextField(verbose_name='Дополнительная информация'),
        ),
    ]