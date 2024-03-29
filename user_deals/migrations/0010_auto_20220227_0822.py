# Generated by Django 3.2.7 on 2022-02-27 08:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user_deals', '0009_propertycomercial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='marla',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='whishlist',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='whishlists', to=settings.AUTH_USER_MODEL),
        ),
    ]
