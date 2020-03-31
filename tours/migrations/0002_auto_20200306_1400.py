# Generated by Django 3.0.4 on 2020-03-06 11:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tour',
            old_name='riddle',
            new_name='firm',
        ),
        migrations.AddField(
            model_name='tour',
            name='hotem',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='tours.Hotel'),
            preserve_default=False,
        ),
    ]