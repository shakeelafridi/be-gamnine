# Generated by Django 3.2.11 on 2022-01-24 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_phonenumberotp_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phonenumberotp',
            name='phone_number',
            field=models.CharField(max_length=15, verbose_name='phone number'),
        ),
    ]
