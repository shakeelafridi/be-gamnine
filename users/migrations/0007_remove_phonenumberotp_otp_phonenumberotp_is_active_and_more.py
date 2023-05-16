# Generated by Django 4.0 on 2022-01-29 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_phonenumberotp_otp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='phonenumberotp',
            name='otp',
        ),
        migrations.AddField(
            model_name='phonenumberotp',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='is_active'),
        ),
        migrations.AddField(
            model_name='phonenumberotp',
            name='otp_type',
            field=models.CharField(choices=[('signup_otp', 'Signup OTP'), ('forgot_password_otp', 'Forgot Password OTP'), ('change_number_otp', 'Change Number OTP')], default='signup_otp', max_length=50),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='is_active'),
        ),
    ]