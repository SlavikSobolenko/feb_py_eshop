# Generated by Django 2.2.12 on 2020-05-02 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shipments', '0005_auto_20200502_1553'),
    ]

    operations = [
        migrations.AddField(
            model_name='shipment',
            name='invoice_id',
            field=models.CharField(default=None, max_length=200, null=True, verbose_name='Document Number'),
        ),
    ]