# Generated by Django 3.2.9 on 2022-01-25 11:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school_app', '0011_alter_teacher_group_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timetable',
            name='class_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='school_app.groups'),
        ),
    ]
