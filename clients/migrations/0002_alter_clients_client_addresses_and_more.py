# Generated by Django 5.0.3 on 2024-04-04 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clients',
            name='client_addresses',
            field=models.TextField(blank=True, verbose_name='Адреса клиента'),
        ),
        migrations.AlterField(
            model_name='clients',
            name='client_orders',
            field=models.TextField(blank=True, verbose_name='Заказы клиента'),
        ),
    ]
