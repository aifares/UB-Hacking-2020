# Generated by Django 3.0.7 on 2020-10-24 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EasyOrder', '0003_menu_products'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='RestaurantCode',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
