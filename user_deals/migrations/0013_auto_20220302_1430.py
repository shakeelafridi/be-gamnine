# Generated by Django 3.2.7 on 2022-03-02 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_deals', '0012_auto_20220302_1430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='from_price',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=15),
        ),
        migrations.AlterField(
            model_name='property',
            name='to_price',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=15),
        ),
    ]
