# Generated by Django 4.0 on 2022-01-30 17:35

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0009_alter_phonenumberotp_is_active_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('purpose', models.CharField(max_length=50)),
                ('property_type', models.CharField(choices=[('HOUSE', 'House'), ('PLOT', 'Plot'), ('COMMERCIAL', 'Commercial')], max_length=50)),
                ('category', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('location', models.TextField()),
                ('unit', models.FloatField(max_length=50)),
                ('marla', models.FloatField()),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=15)),
                ('contact_name', models.CharField(max_length=50)),
                ('contact_number', models.CharField(max_length=50)),
                ('is_notified', models.BooleanField(default=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Whishlist',
            fields=[
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('deals', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_deals.property')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PropertyPlot',
            fields=[
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('series_from', models.CharField(max_length=150)),
                ('series_to', models.CharField(max_length=150)),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plots', to='user_deals.property')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PropertyHouse',
            fields=[
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('house', models.CharField(max_length=250)),
                ('street', models.CharField(max_length=250)),
                ('bedrooms', models.IntegerField()),
                ('bathroom', models.IntegerField()),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='houses', to='user_deals.property')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
