# Generated by Django 4.0 on 2022-01-30 17:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_deals', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='propertyhouse',
            old_name='bathroom',
            new_name='bathrooms',
        ),
    ]