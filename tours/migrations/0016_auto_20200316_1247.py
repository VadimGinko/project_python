# Generated by Django 3.0.4 on 2020-03-16 09:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0015_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tour',
            name='firm',
        ),
        migrations.DeleteModel(
            name='Firm',
        ),
    ]