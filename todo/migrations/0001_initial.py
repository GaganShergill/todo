# Generated by Django 3.0.3 on 2020-08-20 12:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ToDoList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('todo', models.CharField(max_length=256)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_completed', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
