# Generated by Django 4.2.3 on 2023-08-20 20:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('report_comment', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='public_uuid',
            new_name='public_id',
        ),
    ]
