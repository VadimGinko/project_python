# Generated by Django 3.0.4 on 2020-03-08 10:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0008_auto_20200308_1320'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='tour_name',
            new_name='name',
        ),
    ]
