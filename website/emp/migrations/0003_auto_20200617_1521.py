# Generated by Django 3.0.6 on 2020-06-17 11:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('emp', '0002_auto_20200609_1206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='maiden_name',
            field=models.CharField(blank=True, default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='employee',
            name='middle_name',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='employee',
            name='nic',
            field=models.CharField(max_length=12),
        ),
        migrations.AlterField(
            model_name='job',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='employee tasked'),
        ),
    ]
