# Generated by Django 4.0.2 on 2022-03-31 08:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0004_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='slug',
        ),
    ]
