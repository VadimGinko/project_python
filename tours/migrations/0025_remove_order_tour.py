# Generated by Django 3.0.4 on 2020-03-18 16:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0024_auto_20200318_1904'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='tour',
        ),
    ]
