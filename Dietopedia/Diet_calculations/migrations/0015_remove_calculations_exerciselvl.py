# Generated by Django 3.1.3 on 2020-11-22 10:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Diet_calculations', '0014_calculations_exerciselvl'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='calculations',
            name='Exerciselvl',
        ),
    ]