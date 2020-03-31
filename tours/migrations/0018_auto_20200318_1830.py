# Generated by Django 3.0.4 on 2020-03-18 15:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0017_order_tour_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='tour_name',
        ),
        migrations.AddField(
            model_name='order',
            name='hotel',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='tours.Tour', verbose_name='Тур'),
            preserve_default=False,
        ),
    ]
