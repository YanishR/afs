# Generated by Django 3.0.6 on 2020-07-22 06:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('visitor', '0007_service_icont'),
    ]

    operations = [
        migrations.RenameField(
            model_name='service',
            old_name='icont',
            new_name='icon',
        ),
    ]
