# Generated by Django 3.1.2 on 2020-10-12 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customers',
            name='ConfirmPassword',
            field=models.CharField(default='hello', max_length=20),
        ),
        migrations.AddField(
            model_name='customers',
            name='Password',
            field=models.CharField(default='hello', max_length=20),
        ),
    ]
