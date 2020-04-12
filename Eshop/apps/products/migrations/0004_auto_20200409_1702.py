# Generated by Django 2.2.4 on 2020-04-09 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_vendor_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='description',
        ),
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(default='', max_length=5000, verbose_name='Опис'),
            preserve_default=False,
        ),
    ]