# Generated by Django 3.2.8 on 2021-11-11 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours_app', '0005_alter_bookings_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='first name'),
        ),
        migrations.AlterField(
            model_name='users',
            name='last_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='last name'),
        ),
    ]
