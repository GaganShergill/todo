# Generated by Django 3.0.3 on 2020-08-20 12:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_auto_20200820_1815'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='todo',
            new_name='task',
        ),
    ]
