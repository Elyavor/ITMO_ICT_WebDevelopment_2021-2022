# Generated by Django 3.2.8 on 2021-11-09 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours_app', '0004_alter_bookings_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookings',
            name='status',
            field=models.CharField(choices=[('confirmed', 'confirmed'), ('not confirmed', 'not confirmed')], default='not confirmed yet', max_length=30),
        ),
    ]
