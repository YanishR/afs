# Generated by Django 3.0.6 on 2020-07-21 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visitor', '0005_servicedetail'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Homepage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('our_firm', models.CharField(max_length=2000, verbose_name='Our Firm')),
                ('about_us', models.CharField(max_length=2000, verbose_name='About Us')),
                ('resume', models.CharField(max_length=2000, verbose_name='Resume Of the Director')),
            ],
        ),
    ]