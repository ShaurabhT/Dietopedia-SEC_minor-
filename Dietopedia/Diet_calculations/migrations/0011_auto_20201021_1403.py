# Generated by Django 3.1.2 on 2020-10-21 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Diet_calculations', '0010_auto_20201021_1353'),
    ]

    operations = [
        migrations.AddField(
            model_name='calculations',
            name='BDI',
            field=models.FloatField(default=None),
        ),
        migrations.AlterField(
            model_name='calculations',
            name='BMR',
            field=models.FloatField(default=None),
        ),
    ]
