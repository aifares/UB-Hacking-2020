# Generated by Django 3.0.7 on 2020-10-24 20:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('EasyOrder', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurant',
            name='Product',
        ),
    ]
