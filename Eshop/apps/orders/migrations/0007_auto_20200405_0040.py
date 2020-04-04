# Generated by Django 2.2.4 on 2020-04-04 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_order_amount_of_products'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='product',
        ),
        migrations.RemoveField(
            model_name='order',
            name='user',
        ),
        migrations.AlterField(
            model_name='order',
            name='order_number',
            field=models.PositiveSmallIntegerField(blank=True),
        ),
    ]
