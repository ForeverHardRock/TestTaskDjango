# Generated by Django 5.0.3 on 2024-04-04 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0002_remove_orders_buyer_mail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='order_time',
            field=models.DateTimeField(verbose_name='Время заказа'),
        ),
    ]
