# Generated by Django 3.0.7 on 2020-10-24 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EasyOrder', '0002_auto_20201024_1738'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='Products',
            field=models.ManyToManyField(to='EasyOrder.Product'),
        ),
    ]
