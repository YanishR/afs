# Generated by Django 3.0.6 on 2020-06-17 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp', '0003_auto_20200617_1521'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='saved',
            field=models.BooleanField(default=True),
        ),
    ]
