# Generated by Django 3.0.7 on 2020-10-24 17:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('EasyOrder', '0004_menu_restaurantcode'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='Products',
        ),
        migrations.AddField(
            model_name='menu',
            name='Products',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='EasyOrder.Product'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='RestaurantMenu',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='EasyOrder.Restaurant'),
        ),
    ]
