# Generated by Django 3.1.2 on 2020-10-21 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Diet_calculations', '0012_auto_20201021_1405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calculations',
            name='BDI',
            field=models.FloatField(default=None, null=True),
        ),
    ]
