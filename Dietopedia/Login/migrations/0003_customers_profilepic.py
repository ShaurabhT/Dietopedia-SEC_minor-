# Generated by Django 3.1.2 on 2020-10-13 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0002_auto_20201012_1216'),
    ]

    operations = [
        migrations.AddField(
            model_name='customers',
            name='ProfilePic',
            field=models.ImageField(blank=True, upload_to='Profile_image'),
        ),
    ]
