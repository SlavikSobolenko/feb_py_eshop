# Generated by Django 2.2.12 on 2020-06-28 06:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('galleries', '0005_auto_20200521_1731'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gallery',
            name='size',
        ),
        migrations.RemoveField(
            model_name='gallery',
            name='size_x',
        ),
        migrations.RemoveField(
            model_name='gallery',
            name='size_y',
        ),
        migrations.AlterField(
            model_name='gallery',
            name='created_by',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='galleries_gallery_created_by', to=settings.AUTH_USER_MODEL, verbose_name='Ким створено'),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Коли створено'),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='originals/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='updated_by',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='galleries_gallery_updated_by', to=settings.AUTH_USER_MODEL, verbose_name='Ким змінено'),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='updated_on',
            field=models.DateTimeField(auto_now=True, verbose_name='Коли змінено'),
        ),
    ]
