# Generated by Django 3.0.7 on 2020-10-25 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EasyOrder', '0002_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[], max_length=128),
        ),
    ]
