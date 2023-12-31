# Generated by Django 4.2.3 on 2023-08-10 10:51

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report_user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_manager',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='employee_id',
            field=models.IntegerField(unique=True, validators=[django.core.validators.MaxValueValidator(99999)]),
        ),
    ]
