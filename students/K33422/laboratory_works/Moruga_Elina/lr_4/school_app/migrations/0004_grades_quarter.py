# Generated by Django 3.2.8 on 2021-11-29 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_app', '0003_auto_20211129_1123'),
    ]

    operations = [
        migrations.AddField(
            model_name='grades',
            name='quarter',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], default=1, max_length=1),
            preserve_default=False,
        ),
    ]
