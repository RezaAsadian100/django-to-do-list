# Generated by Django 3.0.3 on 2020-03-19 23:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('todolist_app', '0002_auto_20200320_0012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dolist',
            name='date_edited',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
