# Generated by Django 2.2.4 on 2020-04-08 19:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notify_method', models.CharField(choices=[('mail', 'Mail'), ('sms', 'SMS'), ('telegram', 'Telegram'), ('viber', 'Viber')], default='mail', max_length=10)),
                ('notify_title', models.CharField(max_length=100, null=None)),
                ('notify_message', models.CharField(max_length=200)),
                ('notify_date', models.DateTimeField(verbose_name='date published')),
                ('notify_receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
