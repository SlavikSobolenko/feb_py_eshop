# Generated by Django 2.2.4 on 2020-04-04 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
        ('orders', '0004_auto_20200404_2331'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='product',
            field=models.ManyToManyField(db_table='OrderItem', to='products.Product'),
        ),
    ]
