# Generated by Django 3.0.4 on 2020-03-18 16:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0021_auto_20200318_1859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='tour',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tours.Tour', verbose_name='Тур'),
        ),
    ]